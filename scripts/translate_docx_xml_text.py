#!/usr/bin/env python3
import argparse
import json
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parent))
from translate_docx_openai import cache_key, call_openai, should_translate  # noqa: E402


W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
CJK_RE = re.compile(r"[\u3400-\u9fff]")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--cache", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--api-key-env", required=True)
    parser.add_argument("--batch-chars", type=int, default=600)
    parser.add_argument("--batch-items", type=int, default=12)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--retries", type=int, default=5)
    parser.add_argument("--include-code-comments", action="store_true")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    cache_path = Path(args.cache)
    cache = json.loads(cache_path.read_text(encoding="utf-8")) if cache_path.exists() else {}

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        with zipfile.ZipFile(input_path) as z:
            z.extractall(tmp)

        nodes = []
        for xml_path in sorted((tmp / "word").rglob("*.xml")):
            try:
                tree = ET.parse(xml_path)
            except ET.ParseError:
                continue
            root = tree.getroot()
            changed = False
            for node in root.iter(W_NS + "t"):
                text = node.text or ""
                if CJK_RE.search(text) and (args.include_code_comments or should_translate(text)):
                    key = cache_key(text, args.model)
                    if key in cache:
                        node.text = cache[key]
                        changed = True
                    else:
                        nodes.append((xml_path, tree, node, text, key))
            if changed:
                tree.write(xml_path, encoding="utf-8", xml_declaration=True)

        print(f"uncached_xml_text_nodes={len(nodes)}")
        batch = []
        metas = []
        chars = 0
        done = 0
        dirty_trees = {}

        def flush():
            nonlocal batch, metas, chars, done
            if not batch:
                return
            translations = call_openai(batch, args.model, args.timeout, args.retries, args.base_url, args.api_key_env)
            for (xml_path, tree, node, _text, key), translated in zip(metas, translations):
                node.text = str(translated).strip()
                cache[key] = node.text
                dirty_trees[xml_path] = tree
            done += len(batch)
            print(f"translated_xml_nodes={done}/{len(nodes)} cache={len(cache)}")
            batch = []
            metas = []
            chars = 0

        for meta in nodes:
            text = meta[3]
            if batch and (chars + len(text) > args.batch_chars or len(batch) >= args.batch_items):
                flush()
            batch.append(text)
            metas.append(meta)
            chars += len(text)
        flush()

        for xml_path, tree in dirty_trees.items():
            tree.write(xml_path, encoding="utf-8", xml_declaration=True)
        cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")

        if output_path.exists():
            output_path.unlink()
        with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
            for path in tmp.rglob("*"):
                if path.is_file():
                    z.write(path, path.relative_to(tmp))


if __name__ == "__main__":
    main()
