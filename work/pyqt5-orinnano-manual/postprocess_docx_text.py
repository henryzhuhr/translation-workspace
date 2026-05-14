from __future__ import annotations

import re
import tempfile
import zipfile
from pathlib import Path

from lxml import etree


ROOT = Path(__file__).resolve().parents[2]
PROJECT = "pyqt5-orinnano-manual"
DOCX = ROOT / "output" / "doc" / PROJECT / "PyQt5 Application Development Lab Manual - OrinNano_v2.0.en-001.docx"
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

REPLACEMENTS = {
    "安全提示": "Safety Instructions",
    "安全": "Safety",
    "提示": "Instructions",
    "目录": "Table of Contents",
    "第一章 PyQt5应用开发基础": "Chapter 1 Basics of PyQt5 Application Development",
    "1.1 PyQt5简介": "1.1 Introduction to PyQt5",
    "1.2 实验平台硬件介绍": "1.2 Experiment Platform Hardware Introduction",
    "第二章 PyQt5环境搭建与使用": "Chapter 2 PyQt5 Environment Setup and Use",
    "2.1 PyQt5环境搭建": "2.1 PyQt5 Environment Setup",
    "2.2 PyQt5应用开发流程": "2.2 PyQt5 Application Development Process",
    "2.3 导入PyQt5实验实例工程": "2.3 Importing PyQt5 Experiment Example Projects",
    "第三章 PyQt5基础应用开发": "Chapter 3 Basic PyQt5 Application Development",
    "3.1 窗口属性设置": "3.1 Window Property Settings",
    "3.2 信号与槽": "3.2 Signals and Slots",
    "3.3 多窗口设计": "3.3 Multi-window Design",
    "3.4 控件设计-文本类": "3.4 Widget Design - Text Widgets",
    "3.5 控件设计-按钮类": "3.5 Widget Design - Button Widgets",
    "3.6 控件设计-时间日期类": "3.6 Widget Design - Time and Date Widgets",
    "3.7 控件设计-进度条类": "3.7 Widget Design - Progress Bar Widgets",
    "3.8 控件设计-对话框类": "3.8 Widget Design - Dialog Widgets",
    "3.9 布局管理-线性": "3.9 Layout Management - Linear",
    "3.10 布局管理-网格": "3.10 Layout Management - Grid",
    "第四章 PyQt5进阶应用开发": "Chapter 4 Advanced PyQt5 Application Development",
    "4.1 数据库操作": "4.1 Database Operations",
    "4.2 文件操作": "4.2 File Operations",
    "4.3 多线程-Qtimer": "4.3 Multithreading - QTimer",
    "4.4 多线程-QThread": "4.4 Multithreading - QThread",
    "4.5 网络编程-TCP": "4.5 Network Programming - TCP",
    "附录": "Appendix",
    "附1.1 平台启动": "Appendix 1.1 Platform Startup",
    "附1.2 网络连接": "Appendix 1.2 Network Connection",
    "附1.3 SSH登录": "Appendix 1.3 SSH Login",
    "附1.4 文件拷贝": "Appendix 1.4 File Copy",
    "附1": "Appendix 1",
    "第一章": "Chapter 1",
    "第二章": "Chapter 2",
    "第三章": "Chapter 3",
    "第四章": "Chapter 4",
    "应用开发基础": "Application Development Basics",
    "简介": "Introduction",
    "实验平台硬件介绍": "Experiment Platform Hardware Introduction",
    "环境搭建与使用": "Environment Setup and Use",
    "环境搭建": "Environment Setup",
    "应用开发流程": "Application Development Process",
    "导入PyQt5实验实例工程": "Import PyQt5 Experiment Example Projects",
    "导入": "Import ",
    "实验实例工程": " experiment example projects",
    "基础应用开发": "Basic Application Development",
    "窗口属性设置": "Window Property Settings",
    "信号与槽": "Signals and Slots",
    "多窗口设计": "Multi-window Design",
    "控件设计-文本类": "Widget Design - Text Widgets",
    "控件设计-Button类": "Widget Design - Button Widgets",
    "控件设计-按钮类": "Widget Design - Button Widgets",
    "控件设计-时间日期类": "Widget Design - Time and Date Widgets",
    "控件设计-进度条类": "Widget Design - Progress Bar Widgets",
    "控件设计-对话框类": "Widget Design - Dialog Widgets",
    "布局管理-线性": "Layout Management - Linear",
    "布局管理-网格": "Layout Management - Grid",
    "进阶应用开发": "Advanced Application Development",
    "数据库操作": "Database Operations",
    "文件操作": "File Operations",
    "多线程-Qtimer": "Multithreading - QTimer",
    "多线程-QThread": "Multithreading - QThread",
    "网络编程-TCP": "Network Programming - TCP",
    "多线程": "Multithreading",
    "网络编程": "Network Programming",
    "网络连接": "Network Connection",
    "文件拷贝": "File Copy",
    "强大的包管理（Conda）": "Powerful package management (Conda)",
    "连接到SQLite数据库": "Connect to the SQLite database",
    "连接到SQLiteDatabase": "Connect to the SQLite database",
    "Connect到SQLitedatabase": "Connect to the SQLite database",
    "到": " to ",
    "连接": "Connect",
    "数据库": "database",
    "数据库文件是mydb": "The database file is mydb",
    "数据库文件是mrsoft": "The database file is mrsoft",
    "数据库文件是": "The database file is ",
    "如果文件不存在，会自动在当前目录创建": "If the file does not exist, it is automatically created in the current directory",
    "创建一个Cursor": "Create a Cursor",
    "Create一个Cursor": "Create a Cursor",
    "一个": "a ",
    "关闭游标": "Close the cursor",
    "关闭Connection": "Close the Connection",
    "关闭": "Close",
    "提交事务": "Commit the transaction",
    "执行一条SQL语句，创建user表": "Execute an SQL statement to create the user table",
    "执行一条SQL语句，Createuser表": "Execute an SQL statement to create the user table",
    "执行一条SQL语句，插入一条记录": "Execute an SQL statement to insert a record",
    "执行一条SQL语句": "Execute an SQL statement",
    "执行": "Execute",
    "一条": " an ",
    "语句": " statement",
    "执行一条SQL语句，Createuser表": "Execute an SQL statement to create the user table",
    "执行一条SQL语句，insert a record": "Execute an SQL statement to insert a record",
    "插入一条记录": "insert a record",
    "创建user表": "create the user table",
    "表": " table",
    "执行查询语句": "Execute the query statement",
    "获取查询结果": "Get the query result",
    "使用fetchmany方法查询多条数据": "Use the fetchmany method to query multiple records",
    "使用fetchall方法查询多条数据": "Use the fetchall method to query multiple records",
    "查询多条数据": "query multiple records",
    "使用": "Use",
    "方法": "method",
    "删除ID为1的用户": "Delete the user with ID 1",
    "DeleteID为1的user": "Delete the user with ID 1",
    "为": " ",
    "的": " ",
    "删除": "Delete",
    "用户": "user",
    "获取所有用户信息": "Retrieve all user information",
    "记录查询结果": "Record the query result",
    "初始化窗口": "Initialize the window",
    "创建窗口程序": "Create the window application",
    "创建窗口类对象": "Create the window class object",
    "显示窗口": "Display the window",
    "的clicked信号与槽showWindow2关联": " clicked signal is associated with the showWindow2 slot",
    "你好！！！": "Hello!!!",
    "此去西洋，深知中国自强之计，舍此无所他求；背负国家之未来，取尽洋人之科学，赴七万里长途，别祖国父母之邦，奋然无悔": "Going to the West, I know that this is the way for China to strengthen itself; I seek nothing else. Bearing the future of the nation, I will learn all the science of the West, travel seventy thousand li, leave my homeland and parents, and move forward without regret",
    "设置范围": "Set the range",
    "设置步长值": "Set the step value",
    "按钮1": "Button 1",
    "按钮2": "Button 2",
    "按钮3": "Button 3",
    "按钮": "Button",
    "学习此技能": "Learn this skill",
    "已选中": "Selected",
    "未选中": "Not selected",
    "消息对话框！！！": "Message dialog!!!",
    "警告对话框！！！": "Warning dialog!!!",
    "问答对话框！！！": "Question dialog!!!",
    "错误对话框！！！": "Error dialog!!!",
    "关于对话框！！！": "About dialog!!!",
    "消息": "Message",
    "警告": "Warning",
    "问答": "Question",
    "错误": "Error",
    "关于": "About",
    "创建网格布局": "Create a grid layout",
    "设置网格布局": "Set the grid layout",
    "创建并设置标签文本": "Create and set the label text",
    "创建输入文本框": "Create an input text box",
    "用户名:": "Username:",
    "密码：": "Password:",
    "登录": "Log in",
    "取消": "Cancel",
    "第一行第一列添加标签控件，并设置左对齐": "Add a label widget in row 1, column 1 and align it left",
    "第一行第二列添加输入文本框控件，并设置左对齐": "Add an input text box widget in row 1, column 2 and align it left",
    "第二行第一列添加标签控件，并设置左对齐": "Add a label widget in row 2, column 1 and align it left",
    "第二行第二列添加输入文本框控件，并设置左对齐": "Add an input text box widget in row 2, column 2 and align it left",
    "第三行第一列添加按钮控件，并设置居中对齐": "Add a button widget in row 3, column 1 and align it to the centre",
    "第三行第二列添加按钮控件，并设置居中对齐": "Add a button widget in row 3, column 2 and align it to the centre",
    "读取\\写入": "Read/Write",
    "第一条数据": "First data item",
    "读取成功：": "Read successfully: ",
    "写入成功": "Written successfully",
    "开始": "Start",
    "停止": "Stop",
    "地址：  ": "address:  ",
    "IP地址：  ": "IP address:  ",
    "地址": "address",
    "端口：": "port:",
    "无法连接目标服务器!!!": "Unable to connect to the target server!!!",
    "客户端已连接IP:": "TCP client connected to IP:",
    "端口:": "port:",
    "用于TCP客户端创建子线程的方法，阻塞式接收数据": "Method used by the TCP client to create a child thread and receive data in blocking mode",
    "已断开网络": "Network disconnected",
    "请先连接网络服务器": "Please connect to the network server first",
    "客户端已发送": "TCP client sent",
    "发送失败": "Sending failed",
    "用于TCP客户端创建子线程的方法，阻塞式接收": "Method used by the TCP client to create a child thread and receive in blocking mode",
    "从服务器断开连接\\n": "Disconnected from the server\\n",
    "和": "and",
    "创建": "Create",
}


def process_xml(data: bytes) -> tuple[bytes, int]:
    parser = etree.XMLParser(remove_blank_text=False, recover=True)
    root = etree.fromstring(data, parser=parser)
    changed = 0
    for node in root.xpath(".//w:t", namespaces={"w": W_NS}):
        text = node.text
        if not text or not re.search(r"[\u3400-\u9fff]", text):
            continue
        new_text = text
        for source, target in sorted(REPLACEMENTS.items(), key=lambda item: len(item[0]), reverse=True):
            new_text = new_text.replace(source, target)
        if new_text != text:
            node.text = new_text
            changed += 1
    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=False), changed


def main() -> None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp_path = Path(tmp.name)
    changed_total = 0
    with zipfile.ZipFile(DOCX, "r") as zin, zipfile.ZipFile(tmp_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename.startswith("word/") and item.filename.endswith(".xml"):
                data, changed = process_xml(data)
                changed_total += changed
            zout.writestr(item, data)
    tmp_path.replace(DOCX)
    print(f"postprocessed text nodes: {changed_total}")


if __name__ == "__main__":
    main()
