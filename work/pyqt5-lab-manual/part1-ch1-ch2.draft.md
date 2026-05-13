# PyQt5 Application Development Lab Manual — OrinNano v2.0
## Translation Draft: zh-CN → en-US

---







OrinNano人工智能实验平台
——《PyQt5、应用开发》实验手册






















# 安全提示

本文档为OrinNano物联网人工智能实验平台的《PyQt5应用开发》手册，使用此产品前必须仔细阅读本文档，为了保证产品正常安全运行，请注意以下事项：
1）在使用本机之前，请仔细阅读本用户手册并小心保存以供参考，本用户手册中的图解和说明与实物可能会有稍许差异，请以实物为准。
2）设备应运行干燥和空气流通环境下，严禁在高温高压、强磁场、腐蚀等恶劣环境下工作。
3）由于电子产品的特殊性，请勿使水、油、化学试剂等导电液体或腐蚀性液体流到PCB板上，避免在潮湿环境下使用本产品。
4）实验平台须使用配套的电源适配器，不能将其他不同参数的电源接入本设备使用。
5）在每次对模块进行插拔或连接前必须断电状态下操作，以免出现触电危险或让设备短路。
6）在使用产品过程中出现危险情况，请及时切断电源以免造成更大的损失。
7）必须严格遵守本机以及用户手册上的警告指示，电子产品应由技术人员进行维护修理，任何非专业人员对本手册涉及的产品进行维护和修理将有可能对产品造成严重伤害。










# 目录
安全提示	2
目录	3
第一章 PyQt5应用开发基础	5
1.1 PyQt5简介	5
1.2 实验平台硬件介绍	6
第二章 PyQt5环境搭建与使用	7
2.1 PyQt5环境搭建	7
2.2 PyQt5应用开发流程	30
2.3 导入PyQt5实验实例工程	43
第三章 PyQt5基础应用开发	49
3.1 窗口属性设置	49
3.2 信号与槽	55
3.3 多窗口设计	62
3.4 控件设计-文本类	68
3.5 控件设计-按钮类	75
3.6 控件设计-时间日期类	80
3.7 控件设计-进度条类	83
3.8 控件设计-对话框类	86
3.9 布局管理-线性	90
3.10 布局管理-网格	94
第四章 PyQt5进阶应用开发	97
4.1 数据库操作	97
4.2 文件操作	104
4.3 多线程-Qtimer	108
4.4 多线程-QThread	111
4.5 网络编程-TCP	115
附录	124
附1.1 平台启动	124
附1.2 网络连接	126
附1.3 SSH登录	127
附1.4 文件拷贝	131

# 第一章 PyQt5应用开发基础
1.1 PyQt5简介
PyQt5是基于Digia公司强大的图形程序框架Qt的Python接口，由一组Python模块构成，它是一个创建GUI应用程序的工具包，由Phil Thompson进行开发。
自从1998年，首次将Qt移植到Python上形成PyQt以来，已经发布了PyQt3、PyQt4和PyQt5等三个主要版本。

PyQt5的主要特点如下：
1）对Qt库进行完全封装
2）使用信号/槽机制进行通信
3）提供了一整套进行GUI程序开发的窗口控件
4）本身拥有超过620个类和近6000个函数及方法
5）可以跨平台运行在所有主要的操作系统上，包括UNIX、Windows和Mac OS等。
6）支持使用Qt的可视化设计器进行图形界面设计，并能够自主生成Python代码。





1.2 实验平台硬件介绍
人工智能机器视觉实验平台采用OrinNano边缘计算网关作为主控，又加入了麦克风阵列、六轴机械臂、无线传感网节点、嵌入式实验单元以及人机交互单元等硬件模块。可用于人工智能领域机器视觉、自然语言等方向的教学或科研，利用平台上丰富的实验单元可以进行人工智能场景化的应用开发，比如门禁人脸识别系统、物品分拣等。实验平台请以实物为准。







# 第二章 PyQt5环境搭建与使用
2.1 PyQt5环境搭建
### 2.1.1 Anaconda3
1.Anaconda3简介
Anaconda3 是一个开源的 Python 和 R 数据科学平台，专注于简化包管理、环境管理和科学计算任务。它集成了 Conda（跨平台包和环境管理器）、Jupyter Notebook、Spyder IDE 等工具，广泛应用于 数据分析、机器学习、科学计算等领域。

2.核心特点：
1）	强大的包管理（Conda）
支持 Python 和 R 的库安装与管理（如 NumPy、Pandas、TensorFlow）。
自动解决依赖关系，避免版本冲突。
提供 conda install 和 pip install 两种方式管理包。

虚拟环境管理
可创建独立的 Python 环境，不同项目可使用不同版本的 Python 和库：

预装 1500+ 科学计算库
数据分析：Pandas、NumPy、Matplotlib
机器学习：Scikit-learn、TensorFlow、PyTorch
大数据处理：Dask、Vaex
可视化：Seaborn、Plotly

 集成开发工具
Jupyter Notebook（交互式编程和可视化）
Spyder（类似 MATLAB 的科学计算 IDE）
VS Code / PyCharm 兼容

跨平台支持
Windows / macOS / Linux 全平台兼容

3.Anaconda3安装
1）在产品光盘->开发环境->PyQt5中找到Anaconda3-2020.11-Windows-x86_64.exe文件，右键选择“以管理员身份运行”选项开始安装，会出现如下界面，选择Next。


2）在下面界面中选择I Agree选项。


3）在下面界面中选择Next选项。


4）在下面界面中通过Browse…按键浏览选择安装路径，然后选择Next选项。


5）在下面界面中选择Install选项。


6）耐心等待Anaconda3安装进度的完成。


7）在下面界面中选择Next选项。

8) 在下面界面中选择Next选项。


9) 在下面界面中选择Finish选项，完成Anaconda3的安装。


### 2.1.2 tf2虚拟环境
1.tf2虚拟环境简介
TensorFlow 2 (TF2) 虚拟环境是一种隔离的 Python 运行环境，专门用于开发和运行 TensorFlow 2.x 相关项目。使用虚拟环境可以避免不同项目间的依赖冲突，保持开发环境的整洁和可复现性。

2.tf2的作用
版本隔离：不同 TensorFlow 项目可能需要不同版本的 TF 或依赖库
避免污染系统环境：防止安装的包影响系统其他 Python 项目
项目可复现性：可以精确记录项目所需的所有依赖
多项目并行开发：同时开发多个 TF2 项目而互不干扰

3.tf2的搭建
1）在产品光盘->开发环境->PyQt5中找到tf2.zip的压缩包文件，并将其解压到Anaconda3\envs文件夹下。


2）在开始菜单中找到Anaconda Prompt（Anaconda3）选项。


2）会弹出cmd命令行窗口，在其中输入如下命令查看环境是否包含tf2包。
conda info --envs                


3）输入如下命令可以进入tf2虚拟环境。
conda activate tf2                


4）在tf2虚拟环境中输入如下命令可以查看python版本并进入python命令行。
python

使用快捷键 Ctrl + Z可以退出环境。

### 2.1.3 pyqt5及工具安装
1）在tf2命令行中输入如下命令安装 PyQt5。
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ pyqt5==5.15.2      


2）继续在tf2命令中输入如下命令安装 pyqt5-tools包。
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ pyqt5-tools

3）继续在tf2命令中输入如下命令安装pyinstaller工具包。
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller



### 2.1.4 PyCharm安装与配置
1）在产品光盘->开发环境->PyQt5中找到pycharm-community-2020.3.2.exe文件，右键选择“以管理员身份运行”选项开始安装，会出现如下界面，选择Next。

2）在下面界面中通过Browse…按键浏览选择安装路径，然后选择Next选项。


3）在下面界面中勾选左侧的3个单选框，然后选择Next选项。


4）在下面界面中选择Install选项。


5）耐心等待Pycharm安装进度的完成。


6）在下面界面中选择Finish选项，完成Pycharm的安装。


7）此时桌面上会自动创建快捷方式，双击打开即可运行Pycharm。


8）首次运行Pycharm会弹出如下提示，勾选同意后选择Continue选项。


9）在下面界面中选择Don`t Send选项。


10）Pycharm软件欢迎界面如下，选择New Project选项。

11）新建工程时首先在Location选项中选择保存路径，然后勾选Previously configured interpreter单选框，然后点击Interpreter选项后面…按钮。


12）然后会进入如下界面，继续点击Interpreter选项后面…按钮。


13）在弹出的对话框中浏览选择Anaconda3\envs\tf2\python.exe，然后点击OK保存。


14）回到新建工程界面中后，可以看到Interpreter选项中已选择python，然后选择Create。

15）工程新建完成后界面如下。


16）为了使用方便可以调整一下Pycharm软件的界面风格。首先，在菜单栏选择File->Settings…选项打开设置界面。


17）在设置界面中找到Appearance选项中的Theme主题选项，通过下拉菜单选择IntelliJ Light选项后，点击OK保存。


18）主题修改后Pycharm软件会变成白色风格。

19）如果Pycharm软件运行时出现如下错误，解决方法如下：

在运行中输入Regedit命令打开注册表编辑器，依次定位到HKEY_CURRENT_USER＼Software＼Microsoft＼Windows＼Windows Error Reporting选项，并修改DontshowUI的值为1。

### 2.1.5 PyQt5设计器配置
QtDesigner配置
1）在菜单栏选择File->Settings…选项打开设置界面。

2）在设置界面中找到Tools->External Tools选项，并点击+按键添加Qt Designer。


3）点击“+”后会弹出“Create Tool”窗口，按照下表依次填入内容，点击OK按钮保存。


4）保存后在Tools->External Tools选项中可以看到新添加的Qt Designer工具。


PyUIC工具配置
5）继续在Tools->External Tools选项中点击+按键添加PyUIC工具。


6）点击“+”后会弹出“Create Tool”窗口，按照下表依次填入内容，点击OK按钮保存。


7）保存后在Tools->External Tools选项中可以看到新添加的PyUIC工具。


8）Qt Designer和PyUIC工具配置完成后，在Pycharm软件的Tools->External Tools菜单中会出现之前创建的Qt Designer和pyUIC工具。



2.2 PyQt5应用开发流程
### 2.2.1 PyCharm新建工程
1）在Pycharm软件欢迎界面选择New Project选项新建工程。

2）在新建工程界面中，在Localtion中选择工程路径，勾选Previously configured interpreter单选框，然后选择Interpreter为Anaconda3\envs\tf2\python.exe，最后点击Create。


### 2.2.2 QtDesigner设计UI
1.启动Qt Designer
1）在Pycharm软件的Tools->External Tools菜单中选择之前创建的Qt Designer工具，打开Qt Designer设计器。


2）这时会启动一个名为Qt设计师-Qt Designer界面，如下图所示：


2.新建主窗口
1）在“新建窗体”窗口中，选择“Main Window”选项，然后点击创建按钮。
在PyQt5中最常用的窗口有三种，说明如下：
Main Window：主窗口，提供一个带有菜单栏、工具栏和状态栏的窗口
Widget：通用窗口，没有嵌入其他控件的窗口
Dialog：对话框窗口，主要用来执行短期任务，或者与用户进行交互，没有菜单栏、工具栏和状态栏。


2）创建后Qt Designer界面中间会多出一块名为MainWindow的窗口设计区。Qt Designer界面分为菜单栏、工具栏、工具箱、窗口设计区、对象查看器、属性查看器、信号与槽编辑器、动作编辑器、资源管理器等，它们的布局如下。


3.设计主窗口
1）创建完主窗口后，主窗口后默认只有一个菜单栏和一个状态栏，在左侧的Widget Box工具箱中找到PushButton控件，选中它并按住鼠标左键，将其拖放到主窗口内即可，如下图所示：


2）因为新增了UI设计，所以在MainWindow-untiled后尾有个“*”号，表示工程未保存，此时选择文件->保存菜单。


3）点击保存后，会弹出对话框，默认会选择保存到工程路径下，修改文件名为firstPyQt.ui，即与工程同名。

4）UI文件保存完成后，切换到Pycharm软件中时，可以看到firstPyQt.ui文件自动出现在了工程文件列表中。

### 2.2.3 将.ui转换为.py
1）选中firstPyQt.ui文件，然后在菜单栏选择Tools->External Tools->pyUIC选项进行转换。


2）转换完成后在工程文件列表中会多出来一个firstPyQt.py文件，双击打开它之后可以查看其文件内容。


### 2.2.4 编写main.py
1）通过上面的步骤已经将firstPyQt.ui转换成firstPyQt.py，但是因为firstPyQt.py文件没有程序入口，所以不能直接运行。因此我们需要修改main.py文件，将其作为程序入口，通过它来调用firstPyQt.py运行。
在main.py中添加代码内容如下，它通过__main__来设置程序入口，并通过MainWindow()对象调用show()函数来显示firstPyQt的UI窗口。
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import firstPyQt as fUi
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = fUi.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
代码添加后如下图所示：


2）然后在菜单栏选择File->Save All选项对修改进行保存。

### 2.2.5 PC端运行PyQt应用
1）在菜单栏选择Run->Run‘main’选项运行程序，或者直接在右上角的工具栏点击绿色的运行图标运行程序。

程序运行后会弹出一个窗口，其界面与之前设计的一致。


### 2.2.6 PC端PyQt5应用打包
如果PyQt5应用工程已经设计完成，可以通过pyinstaller工具将工程打包成在PC端的.exe可执行程序，操作步骤如下：
1）首先，为了操作方便，将firstPyQt工程文件夹拷贝到磁盘根目录，比如D盘根目录。

2）打开Anaconda3的命令行，通过如下命令切换至tf2虚拟环境。
conda activate tf2

3）打开cmd命令行进入工程目录，比如下图中的D:\firstPyQt文件夹，操作命令如下。
D:
cd firstPyQt


4）输入如下命令，通过pyinstaller工具进行打包。
pyinstaller  -F main.py


5）在firstPyQt工程目录下会多出一个dist文件夹，其中main.exe为打包的可执行程序。

6）直接运行main.exe即可运行程序。


### 2.2.7 网关运行PyQt应用
1）启动实验平台，参照附录1.2连接好网络并查看IP地址，然后通过SSH工具远程登陆到OrinNano边缘计算网关Ubuntu系统的控制台终端。

2）参照附录1.3-1.4将工程文件夹firstPyQt拷贝至网关系统内某个目录下。


3）通过鼠标打开网关中的终端软件，如果左侧列表中没有该图标，点击左上角所有程序，然后搜索Terminal，将图标拖动至左侧栏即可。


4）通过键盘输入如下命令进入对应的拷贝的工程路径下，然后执行main.py程序。
cd test/firstPyQt                                                                 #请以实际的拷贝路径为准
python3 main.py


5）程序运行后，在网关屏幕上也会弹出一个Qt的界面，UI与之前设计的一致。

6）注意：如果直接在SSH工具中运行此程序，那么程序会在PC端显示。


2.3 导入PyQt5实验实例工程
### 2.3.1 运行实验实例工程
1）将光盘中提供的实验例程代码解压至默认的工程保存路径下（一般默认为C:\Users\用户名\PycharmProjects）。


2）在Pycharm软件的欢迎界面中点击Open。


3）浏览并选择工程的路径，然后点击OK。


4）工程打开后，Pycharm软件中会弹出提示“No Python interpreter configured for the project”，点击其后面的Configure Python interpreter选项。


5）在弹出的选项中选择Python 3.7 (tf2)选项。


6）错误消除后直接运行程序，可以看到导入的实例代码能够正常运行。



### 2.3.2 修改实验实例UI
在实例代码工程UI界面基础上进行修改，可以大大减少开发时间，具体操作如下：
1）在Pycharm软件的Tools->External Tools菜单中选择之前创建的Qt Designer工具，打开Qt Designer设计器。

2）Qt Designer设计器默认会弹出新建窗体的提示框。


3）因为实例代码工程的UI已经设计好了，所以这里就不再新建，而是选择打开。


4）浏览并选择工程中的 .ui文件，然后打开。


5）打开后我们就可以查看实验实例代码工程的UI界面效果，以及窗口和各种组件的属性、动作、槽等一些设置，可以调整参数或者在界面上增删组件。


6）修改UI之后，直接选择菜单栏文件->保存选项，即可覆盖原.ui文件。


7）最后在Pycharm软件中将.ui换成.py即可让修改的界面生效。


