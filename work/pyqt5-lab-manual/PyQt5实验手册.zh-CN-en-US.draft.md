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


# 第三章 PyQt5基础应用开发
3.1 窗口属性设置
### 3.1.1 实验目的
1）学习PyQt5窗口属性的设置方法。
2）通过PyQt5属性设置重新设计UI。
### 3.1.2 基础知识
窗口的对象名称，相当于窗口的标识，是唯一的，在编写代码时，对窗口的任何设置和使用都是通过该名称进行操作的。窗口可以通过Qt Designer界面中的属性编辑器进行调整，比如可以设置窗口的对象名称、标题、大小、图标等。
### 实验步骤
注意：本实验是在第二章新建的firstPyQt工程基础上进行操作的。
#### 3.1.3.1 设置窗口名称
选择窗口对象
在Qt Designer设计器的对象查看器中选择主窗体MainWindow。


修改窗口名称
在属性编辑器中将QObject->objectName属性修改为firstMain，并用组合快捷键Ctrl + S保存修改。


将.ui转换为.py
因为UI修改过，回到Pycharm软件使用pyUIC工具将新的firstPyQt.ui转换成firstPyQt.py，打开firstPyQt.py文件可以看到窗口名称已自动修改。


修改main.py
打开main.py文件，将下图修改对应行的代码。
ui = fUi.Ui_firstMain()


运行工程
直接运行代码如下图所示，因为只是修改窗口对象名称，所以在界面上没有变化，此时窗口大小为800 x 600像素。


#### 3.1.3.2 设置窗口标题栏
在属性编辑器中找到windowTitle选项，将其修改为myFirstPyQtAPP，然后通过组合快捷键Ctrl + S保存修改。


回到Pycharm软件使用pyUIC工具重新生成.py文件。
重新运行程序后界面如下，可以看到窗口标题已显示为myFirstPyQtAPP。


#### 3.1.3.3 设置窗口大小
在属性编辑器中找到geometry选项，将宽度和高度分别修改为400*300，然后通过组合快捷键Ctrl + S保存修改。


回到Pycharm软件使用pyUIC工具重新生成.py文件。
重新运行程序后界面如下，可以看到窗口明显缩小，大小为400 x 300像素。


#### 3.1.3.4 设置窗口图标
准备一张图标图片，将其放到工程路径下。

在属性编辑器中找到windowIcon选项，并点击右侧。

点击windowIcon选项右侧的按钮，在弹出的列表中选择“选择文件…”选项。

在弹出的选择一个像素映射的对话框中，浏览选择之前拷贝的qt.png文件，然后打开。

在Qt Designer中通过组合快捷键Ctrl + S保存修改。
回到Pycharm软件使用pyUIC工具重新生成.py文件。

### 实验结果
重新运行程序后界面如下，可以看到窗口左上角的图标已经发生了变化。

通过窗口属性设置的方法。修改了窗口名称、标题栏、窗口大小以及窗口的图标。



3.2 信号与槽
### 3.2.1 实验目的
1）学习PyQt5信号与槽窗的使用方法。
2）通过PyQt5信号与槽窗实现UI界面上的按钮触发动作。
3）掌握PyQt5中自定义槽函数的方法。
### 3.2.2 基础知识
信号（signal）与槽（slot）是Qt的核心机制，也是进行PyQt5编程时对象之间通信的基础。在PyQt5中，每一个QObject对象（包括各种窗口和控件）都支持信号与槽机制，通过信号与槽的关联，就可以实现对象之间的通信。当信号发射时，连接的槽函数（方法）将会自动执行。在PyQt5中，信号与槽是通过对象的signal.connect()方法进行连接的。

### 3.2.3 实验步骤
注意：本实验是在第二章新建的firstPyQt工程基础上进行操作的。
#### 3.2.3.1 编辑信号与槽
在Qt Designer设计器中查看器中选择pushButton。

在属性编辑器中找到text选项，将其内容改为“关闭”。


在菜单栏中选择“Edit -> 编辑信号/槽”选项。


此时工具箱等位置会变成灰色，用鼠标选中UI窗口中的按钮，然后长按鼠标左键拖动到空白位置。


在弹出的配置连接对话框中，勾选左下角的单选框，在左侧列表中选择clicked()，在右侧列表中选择close()，然后点击OK。


完成信号与槽的关联之后，预览窗口如下图所示。此时可以通过组合快捷键Ctrl + S保存修改。

回到Pycharm使用pyUIC工具重新生成.py文件，且该文件中自动添加了相关代码。

重新运行程序，点击关闭按钮后，程序界面窗口会自动关闭。


#### 3.2.3.2 自定义槽
自定义槽本质上就是自定义一个函数，函数来实现相应的功能，其操作方法如下：
取消原来信号与槽的关联
在Qt Designer中选择信号/槽编辑器，选择之前关联项，然后点击上面的“-”按钮进行删除。通过组合快捷键Ctrl + S保存修改，回到Pycharm使用pyUIC工具重新生成.py文件。


重写UI类
在main.py中重写继承关于ui的类，然后在函数入口通过重写的mainWindow()启动界面窗口，代码如下：
class mainWindow(QMainWindow, fUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainWindow()
    ui.show()
    sys.exit(app.exec_())

自定义槽函数
在类mainWindow中添加槽函数ClickEvent()，修改后代码如下：
class mainWindow(QMainWindow, fUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
    def ClickEvent(self):
        self.statusbar.showMessage("Hello World!")

关联信号与槽
在mainWindow类中完成clicked信号与槽函数ClickEvent()的关联，修改后代码如下：
class mainWindow(QMainWindow, fUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        #pushButton的clicked信号与槽ClickEvent关联
        self.pushButton.clicked.connect(self.ClickEvent)
    def ClickEvent(self):
        self.statusbar.showMessage("Hello World!")

以上几步代码编辑完成后如下图所示：



### 3.2.4 实验结果
直接运行代码，在弹出的窗口中点击关闭按钮后，窗口左下角会显示出“Hello World！”的字符串。




3.3 多窗口设计
### 3.3.1 实验目的
学习PyQt5多窗口的使用方法。
### 3.3.2 基础知识
一个完整的综合应用一般都是由多个窗口组成的，通过弹窗、或者窗口之间跳转等方式实现交互功能。
### 3.3.3 实验步骤
通过Pycharm软件新建一个名为multiWindow的工程。


通过External Tools打开Qt Designer设计器。

在默认弹窗中选择创建一个MainWindow，然后在菜单栏选择文件->新建(F)…选项，在弹窗中选择创建第二个MainWindow。


修改窗口属性
分别修改两个窗口的“objectName”为：mutliWindow1和mutliWindow2
分别修改两个窗口的“windowTitle”为：window1和window2
分别修改两个窗口的宽度和高度为：300 x 200
在mutliWindow1窗口中，添加一个pushButton按钮

两个窗口属性设置完成后界面如下，然后依次选中两个窗口通过Ctrl + S进行保存，分别命名为mutliwindow1.ui和mutliwindow2.ui。

回到Pycharm软件使用pyUIC工具依次将两个.ui文件转换成.py文件。

重写mainWindows
修改main.py代码，重写mainWindow类，通过它打开multiWindow1窗口，并且主函数启动程序时会调用它。
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import multiWindow1 as mUi1
import multiWindow2 as mUi2
class mainWindow(QMainWindow, mUi1.Ui_multiWindow1):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainWindow()
    ui.show()
    sys.exit(app.exec_())
重写window2
重写Window2类，通过它打开multiWindow2窗口。
class window2(QMainWindow, mUi2.Ui_multiWindow2):
def __init__(self):
        super(window2, self).__init__()
        self.setupUi(self)
关联槽函数
在mainWindow类中添加一个showWindow2的槽函数，并且将pushButton的clicked信号与之关联。
class mainWindow(QMainWindow, mUi1.Ui_multiWindow1):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        #pushButton的clicked信号与槽showWindow2关联
        self.pushButton.clicked.connect(self.showWindow2)
    def showWindow2(self):
        self.window2 = window2()
        self.window2.show()
10）代码编写完成后界面如下：


### 3.3.4 实验结果
运行程序后会打开窗口1，然后点击PushButton按钮会弹出窗口2。


3.4 控件设计-文本类
### 3.4.1 实验目的
1）了解PyQt文本类控件Label、TextEdit、SpinBox的重要属性和方法。
2）编写代码，掌握Label、TextEdit、SpinBox的重要属性的设置方法。
### 3.4.2 基础知识
Label控件，又称为标签控件，主要用于显示用户不能编辑的文本，标识窗体上的对象，它对应PyQt5中的QLabel类。
TextEdit控件是多行文本框控件，主要用来显示多行的文本内容，当文本的内容超出控件的显示范围时，该控件将显示垂直滚动条。
SpinBox控件是一个整数数字控件，允许用户选择一个整数值，通过单击向上/向下按钮或按键盘上的上/下箭头来增加/减少当前显示的值，当然用户也可以输入值。

### 3.4.3 实验步骤
#### 3.4.3.1 Label
参照第2章在Pycharm软件中新建一个textPyQt工程，并将qt.png图片文件拷贝到工程的根目录（图片可在本章节的实验源代码中找到）。
在Qt Designer中创建一个MainWindow窗口，窗口尺寸为400 x 300，并通过工具箱添加两个Label组件，两个Label的objectName分别为label1和label2。

在Qt Designer中通过组合快捷键Ctrl + S保存为textPyQt.ui，然后回到Pycharm软件中使用pyUIC工具生成textPyQt.py文件。
修改main.py代码，直接通过setText方法让label1显示文本，让label2显示图片并指定坐标和大小，代码如下：
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
import textPyQt as textUi
class mainWindow(QMainWindow, textUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.label1.setText("你好！！！")
        self.label2.setGeometry(QtCore.QRect(160, 100, 60, 60))
        self.label2.setPixmap(QPixmap('qt.png'))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainWindow()
    ui.show()
    sys.exit(app.exec_())
代码修改后如下图所示：

直接运行程序，弹出窗口界面如下：


#### 3.4.3.2 TextEdit
说明：本小节直接在上一小节的实验代码的基础上进行操作。
在Qt Designer中为窗口添加一个TextEdit控件。

在Qt Designer中通过组合快捷键Ctrl + S保存textPyQt.ui，然后回到Pycharm软件中使用pyUIC工具重新生成textPyQt.py文件。
修改main.py代码，通过setPlainText方法为textEdit添加长字符串，修改后代码如下：
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
import textPyQt as textUi
class mainWindow(QMainWindow, textUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.label1.setText("你好！！！")
        self.label2.setGeometry(QtCore.QRect(160, 100, 60, 60))
        self.label2.setPixmap(QPixmap('qt.png'))
        self.textEdit.setPlainText("此去西洋，深知中国自强之计，舍此无所他求；背负国家之未来，取尽洋人之科学，赴七万里长途，别祖国父母之邦，奋然无悔。 ")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainWindow()
    ui.show()
    sys.exit(app.exec_())
运行程序窗口界面如下，拖动滑动条可以浏览全部文字。


#### 3.4.3.3 SpinBox
说明：本小节直接在上一小节的实验代码的基础上进行操作。
在Qt Designer中为窗口添加一个SpinBox控件。

在Qt Designer中通过组合快捷键Ctrl + S保存textPyQt.ui，然后回到Pycharm软件中使用pyUIC工具重新生成textPyQt.py文件。
修改main.py代码，直接通过setRange和setSingleStep方法为SpinBox控件设置范围和步长，修改后代码如下：
class mainWindow(QMainWindow, textUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.label1.setText("你好！！！")
        self.label2.setGeometry(QtCore.QRect(160, 100, 60, 60))
        self.label2.setPixmap(QPixmap('qt.png'))
        self.textEdit.setPlainText("此去西洋，深知中国自强之计，舍此无所他求；背负国家之未来，取尽洋人之科学，赴七万里长途，别祖国父母之邦，奋然无悔。 ")
        self.spinBox.setRange(0, 66)  # 设置范围
        self.spinBox.setSingleStep(3)  # 设置步长值

在mainWindow类中定义一个getvalue的槽函数
def getvalue(self):
        self.label1.setText(str(self.spinBox.value()))

将spinBox控件的valueChanged信号与自定义的getvalue()槽函数关联。
class mainWindow(QMainWindow, textUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.label1.setText("你好！！！")
        self.label2.setGeometry(QtCore.QRect(160, 100, 60, 60))
        self.label2.setPixmap(QPixmap('qt.png'))
        self.textEdit.setPlainText("此去西洋，深知中国自强之计，舍此无所他求；背负国家之未来，取尽洋人之科学，赴七万里长途，别祖国父母之邦，奋然无悔。 ")
        self.spinBox.setRange(0,66)      #设置范围
        self.spinBox.setSingleStep(3)   #设置步长值
        self.spinBox.valueChanged.connect(self.getvalue)
代码修改完成后如下图所示：




### 3.4.4 实验结果
程序窗口界面如下，点击SpinBox控件右侧的箭头，可以控制空间内的数据变化，从0开始，每次自增3，并且Lable1控件会通过信号与槽同步显示数字变化。


在窗体中创建了三种不同的文本类控件，并分别学习了这三种控件的使用方法。




3.5 控件设计-按钮类
### 3.5.1 实验目的
1）了解PyQt按钮类控件PushButton、CheckBox的重要属性和方法。
2）编写代码，掌握按钮类控件PushButton、CheckBox的重要属性的设置方法。
### 3.5.2 基础知识
PushButton控件是按钮控件，允许用户通过单击来执行操作。即可以显示文本内容，也可以显示图像。当控件被单击时，它的状态是按下然后被释放。
CheckBox控件是复选框控件，常用于为用户提供具有是/否或真/假值的选项，对应CheckBox类。

### 3.5.3 实验步骤
#### 3.5.3.1 PushButton
参照第2章在Pycharm软件中新建一个buttonPyQt工程，并将login.ico的图片拷贝到工程根目录下（图片可在本章节的实验源代码中找到）。
在Qt Designer中创建一个MainWindow窗口，窗口尺寸为400 x 300，并通过工具箱添加一个PushButton控件。

在Qt Designer中通过组合快捷键Ctrl + S保存为buttonPyQt.ui，然后回到Pycharm软件中使用pyUIC工具生成buttonPyQt.py文件。
修改main.py代码，直接通过setText方法修改按钮的文本显示，通过setIcon方法指定按钮的显示图片，修改后代码如下：
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import buttonPyQt as butUi
from PyQt5.QtGui import QIcon, QPixmap
class mainWindow(QMainWindow, butUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.setText("按钮")
        self.pushButton.setIcon(QIcon(QPixmap("login.ico")))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainWindow()
    ui.show()
    sys.exit(app.exec_())

运行程序窗口界面如下，PushButton控件上会显示特定的图片+文字。


#### 3.5.3.2 CheckBox
继续在buttonPyQt工程Qt Designer设计器中，添加一个CheckBox控件。

在Qt Designer中通过组合快捷键Ctrl + S保存buttonPyQt.ui，然后回到Pycharm软件中使用pyUIC工具重新生成buttonPyQt.py文件
修改main.py代码，添加如下代码为CheckBox控件控件设置文本和图片。
self.checkBox.setText("学习此技能")
self.checkBox.setIcon(QIcon(QPixmap("login.ico")))
在mainWindow类中定义一个槽函数setBtnText，代码如下：
def setBtnText(self):
    if self.checkBox.isChecked():
        self.pushButton.setText("已选中")
    else:
        self.pushButton.setText("未选中")
checkBox控件最常用的信号是stateChanged，用来在复选框的状态发生改变时发射。添加checkbox的stateChanged信号与槽函数setBtnText关联代码。
self.checkBox.setText("学习此技能")
self.checkBox.setIcon(QIcon(QPixmap("login.ico")))
self.checkBox.stateChanged.connect(self.setBtnText)
main.py完整代码如下。
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import buttonPyQt as butUi
from PyQt5.QtGui import QIcon, QPixmap
class mainWindow(QMainWindow, butUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.setText("按钮")
        self.pushButton.setIcon(QIcon(QPixmap("login.ico")))
        self.checkBox.setText("学习此技能")
        self.checkBox.setIcon(QIcon(QPixmap("login.ico")))
        self.checkBox.stateChanged.connect(self.setBtnText)
    def setBtnText(self):
        if self.checkBox.isChecked():
            self.pushButton.setText("已选中")
        else:
            self.pushButton.setText("未选中")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainWindow()
    ui.show()
    sys.exit(app.exec_())

### 3.5.4 实验结果
运行程序窗口界面如下。

当勾选checkBox控件时，PushButton按钮控件文本会变为“已选中”。

当取消勾选checkBox控件时，PushButton按钮控件文本会变为“未选中”。




3.6 控件设计-时间日期类
### 3.6.1 实验目的
1）了解PyQt日期时间类控件Data/TimeEdit的重要属性和方法。
2）编写代码，掌握日期时间类控件Data/TimeEdit的重要属性的设置方法。
### 3.6.2 基础知识
Data/TimeEdit控件对应的类是QDataTimeEdit，该控件可以同时显示和编辑日期时间，它最常用的信号是dataTimeChanged，用来在日期或时间发生改变时发射。
### 3.6.3 实验步骤
参照第2章在Pycharm软件中新建一个timePyQt工程。
在Qt Designer中创建一个MainWindow窗口，窗口尺寸为400 x 300，并通过工具箱添加一个Data/TimeEdit控件和一个Label控件。

在Qt Designer中通过组合快捷键Ctrl + S保存timePyQt.ui，然后回到Pycharm软件中使用pyUIC工具生成timePyQt.py文件。
修改main.py，在mainWindow类的__init__(self)方法中定义showChangeTime()槽函数，代码如下：
def showChangeTime(self):
    self.label.setText(self.dateTimeEdit.text())
添加Data/TimeEdit的dataTimeChanged信号与槽函数showChangeTime的关联，另外同步系统时间并设置时间日期的格式，代码如下：
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateTimeEdit.setDisplayFormat("yyyy/MM/dd hh:mm:ss")
        self.dateTimeEdit.dateTimeChanged.connect(self.showChangeTime)
代码修改完成如下图所示：

### 3.6.4 实验结果
运行程序窗口界面如下，Data/TimeEdit控件会显示当前日期和时间。

选择Data/TimeEdit控件内的日期或时间后，点击右侧的上下箭头，可以调整日期和时间，并且修改后的日期和时间会通过信号与槽同步显示到Label控件上。





3.7 控件设计-进度条类
### 3.7.1 实验目的
1）了解PyQt进度条类控件ProgressBar的重要属性和方法。
2）编写代码，掌握进度条类控件ProgressBar的重要属性的设置方法。
### 3.7.2 基础知识
ProgressBar控件对应的类是QProgressBar，该控件通常在执行长时间任务时，用进度条告诉用户当前的进展情况。它最常用的信号是valueChanged，在进度条的值发生改变时发射。
### 3.7.3 实验步骤
参照第2章在Pycharm软件中新建一个progressbarPyQt工程。
在Qt Designer中创建一个MainWindow窗口，窗口尺寸为400 x 300，并通过工具箱添加一个PushButton控件和一个ProgressBar控件。

通过组合快捷键Ctrl + S保存为progressbarPyQt.ui，然后回到Pycharm软件使用pyUIC工具生成progressbarPyQt.py文件。
在main.py代码类mainWindow中的__init__(self)方法中为进度条设置默认值为0%，另外更改PushButton控件的文本显示。
self.progressBar.setValue(0)  # 设置进度条的值
self.pushButton.setText("开始")
在main.py代码类mainWindow中的__init__(self)方法中编写槽函数running()，代码如下。
def running(self):
    global i
    self.progressBar.setMaximum(100)
    self.progressBar.setProperty("value", i)
    i += 10
    if i > 100:
        i = 0

添加PushButton的clicked信号与槽函数running关联，代码如下：
self.progressBar.setValue(0)  # 设置进度条的最小值
self.pushButton.setText("开始")
self.pushButton.clicked.connect(self.running)

编辑完成后代码如下：



### 3.7.4 实验结果
运行程序窗口界面如下：

点击界面上的开始按钮可以控制进度条变化，每点击一次进度+10%，当达到100%时再次点击按钮，进度条会归零即为0%。



3.8 控件设计-对话框类
### 3.8.1 实验目的
1）了解PyQt对话框类控件QMessageBox的重要属性和方法。
2）编写代码，掌握对话框类控件QMessageBox的重要属性的设置方法。
### 3.8.2 基础知识
QMessageBox控件表示对话框，内置了5种不同类型的对话框，分别是消息对话框、问答对话框、警告对话框、错误对话框和关于对话框。语法格式如下：
QMessageBox.information(QWidget=?, 'title', 'Content', buttons=?, defaultButton=? )
QWidget：self或者窗口对象，表示该对话框所属的窗口
Title：字符串，表示对话框的标题
Content：字符串，表示对话框的提示内容
Buttons：对话框中要添加的按钮
defaultButton：默认选中的按钮
### 3.8.3 实验步骤
参照第2章在Pycharm软件中新建一个messageboxPyQt工程。
在Qt Designer中创建一个MainWindow窗口，窗口尺寸为400 x 300，并通过工具箱添加5个PushButton控件。然后依次选中5个按钮，通过属性编辑器分别修改它们的属性：Qobject->objectName依次为：pushButton1、pushButton2、pushButton3、pushButton4、pushButton5；QAbstractButton->text依次为：消息框、警告框、问答框、错误框、关于框。

通过组合快捷键Ctrl + S保存为messageboxPyQt.ui，然后回到Pycharm软件使用pyUIC工具生成messageboxPyQt.py文件。
在main.py代码类mainWindow中的__init__(self)方法中编写五个对话框的槽函数，代码如下：
def info(self):
    QMessageBox.information(None, '消息', '消息对话框！！！', QMessageBox.Ok)
def waning(self):
    QMessageBox.warning(None, '警告', '警告对话框！！！', QMessageBox.Ok)
def question(self):
    QMessageBox.question(None, '问答', '问答对话框！！！', QMessageBox.Ok)
def wrong(self):
    QMessageBox.critical(None, '错误', '错误对话框！！！', QMessageBox.Ok)
def about(self):
    QMessageBox.about(None, '关于', '关于对话框！！！')
添加五个PushButton的clicked信号与槽函数关联，代码如下：
self.pushButton1.clicked.connect(self.info)
self.pushButton2.clicked.connect(self.waning)
self.pushButton3.clicked.connect(self.question)
self.pushButton4.clicked.connect(self.wrong)
self.pushButton5.clicked.connect(self.about)
代码完成后如下图所示：


运行程序窗口界面如下。




### 3.8.4 实验结果
依次点击界面上的5各按钮，弹出对话框效果如下：



3.9 布局管理-线性
### 3.9.1 实验目的
1）了解PyQt线性布局的重要属性和方法。
2）编写代码，实现线性布局的设置方法。
### 3.9.2 基础知识
线性布局是将放入其中的组件按照垂直或水平方向来布局。VerticalLayout的基类为：QVBoxLayout。而HorizontalLayout的基类为：QHBoxLayout。

### 3.9.3 实验步骤
注意：本节实验和之前操作不一样，不使用Qt Designer设计器来设计UI，而是直接通过代码的方式来进行UI设计。
#### 3.9.3.1 VerticalLayout垂直布局
参照第2章在Pycharm软件中新建一个vlayoutPyQt工程。
重写main.py代码，初始化时会调用自定义的initUI方法设置为垂直布局，代码如下：
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)
        self.initUI() # 初始化窗口
    def initUI(self):
        vlayout=QVBoxLayout()
        self.setLayout(vlayout)
if __name__=='__main__':
    import sys
    app=QApplication(sys.argv) # 创建窗口程序
    demo=Demo() # 创建窗口类对象
    demo.show() # 显示窗口
    sys.exit(app.exec_())
此时如果直接运行代码的话，效果如下：

接下来在initUI的vlayout垂直布局中添加三个按钮。这里需要使用addWidget()方法添加。同时，同时使用addSpacing()方法来设置控件之间的上下间距，代码如下：
def initUI(self):
    vlayout=QVBoxLayout()
    btn1 = QPushButton()
    btn1.setText('按钮1')
    btn2 = QPushButton()
    btn2.setText('按钮2')
    btn3 = QPushButton()
    btn3.setText('按钮3')
    vlayout.addWidget(btn1)
    vlayout.addSpacing(10)
    vlayout.addWidget(btn2)
    vlayout.addSpacing(30)
    vlayout.addWidget(btn3)
    self.setLayout(vlayout)
4）运行代码效果如下，3个按钮按照垂直方向进行依次排列。


#### 3.9.3.2 HorizontalLayout水平布局
参照第2章在Pycharm软件中新建一个hlayoutPyQt工程。
重写main.py代码，初始化时会调用自定义的initUI方法设置为水平布局，代码如下：
from PyQt5.QtWidgets import *
class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)
        self.initUI() # 初始化窗口
    def initUI(self):
        hlayout=QHBoxLayout()
        self.setLayout(hlayout)
if __name__=='__main__':
    import sys
    app=QApplication(sys.argv) # 创建窗口程序
    demo=Demo() # 创建窗口类对象
    demo.show() # 显示窗口
    sys.exit(app.exec_())
此时如果直接运行代码的话，效果如下：

接下来在initUI的hlayout垂直布局中添加三个按钮。这里需要使用addWidget()方法添加。同时，同时使用addSpacing()方法来设置控件之间的上下间距，代码如下：
def initUI(self):
    hlayout=QHBoxLayout()
    btn1 = QPushButton()
    btn1.setText('按钮1')
    btn2 = QPushButton()
    btn2.setText('按钮2')
    btn3 = QPushButton()
    btn3.setText('按钮3')
    hlayout.addWidget(btn1)
    hlayout.addSpacing(10)
    hlayout.addWidget(btn2)
    hlayout.addSpacing(30)
    hlayout.addWidget(btn3)
    self.setLayout(hlayout)

运行程序效果如下，3个按钮按照水平方向进行依次排列。




### 3.9.4 实验结果
运行第一个程序，效果如下，3个按钮按照垂直方向进行依次排列。


运行第二个程序，效果如下，3个按钮按照水平方向进行依次排列。



3.10 布局管理-网格
### 3.10.1 实验目的
1）了解PyQt网格布局的重要属性和方法。
2）编写代码，实现网格布局的设置方法。
### 3.10.2 基础知识
GridLayout被称为网格布局，它将位于其中的控件放入一个多行多列的网格中。GridLayout控件需要将提供给它的空间划分成行和列，并把每个控件插入到正确的单元格中，示意图如下：

GridLayout基类是QGridLayout，其常用的方法说明如下：
### 3.10.3 实验步骤
注意：本节实验和之前操作不一样，不使用Qt Designer设计器来设计UI，而是直接通过代码的方式来进行UI设计。
参照第2章在Pycharm软件中新建一个gridPyQt工程。
重写main.py代码，初始化时会调用自定义的initUI方法设置为网格布局，代码如下：
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)
        self.initUI() # 初始化窗口
    def initUI(self):
        grid=QGridLayout() # 创建网格布局
        self.setLayout(grid) # 设置网格布局
if __name__=='__main__':
    import sys
    app=QApplication(sys.argv) # 创建窗口程序
    demo=Demo() # 创建窗口类对象
    demo.show() # 显示窗口
    sys.exit(app.exec_())

接下来在initUI的gird网格布局中，实现一个登陆窗口。代码如下：
def initUI(self):
    grid=QGridLayout() # 创建网格布局
    # 创建并设置标签文本
    label1=QLabel()
    label1.setText("用户名:")
    # 创建输入文本框
    text1=QLineEdit()
    # 创建并设置标签文本
    label2 = QLabel()
    label2.setText("密码：")
    # 创建输入文本框
    text2 = QLineEdit()
    # 创建“登录”和“取消”按钮
    btn1=QPushButton()
    btn1.setText("登录")
    btn2 = QPushButton()
    btn2.setText("取消")
    # 第一行第一列添加标签控件，并设置左对齐
    grid.addWidget(label1,0,0,QtCore.Qt.AlignLeft)
    # 第一行第二列添加输入文本框控件，并设置左对齐
    grid.addWidget(text1, 0, 1, QtCore.Qt.AlignLeft)
    # 第二行第一列添加标签控件，并设置左对齐
    grid.addWidget(label2, 1, 0, QtCore.Qt.AlignLeft)
    # 第二行第二列添加输入文本框控件，并设置左对齐
    grid.addWidget(text2, 1, 1, QtCore.Qt.AlignLeft)
    # 第三行第一列添加按钮控件，并设置居中对齐
    grid.addWidget(btn1, 2, 0, QtCore.Qt.AlignCenter)
    # 第三行第二列添加按钮控件，并设置居中对齐
    grid.addWidget(btn2, 2, 1, QtCore.Qt.AlignCenter)
    self.setLayout(grid) # 设置网格布局


### 3.10.4 实验结果
运行程序效果如下，界面中各种控件通过网格布局进行定位和对齐。






# 第四章 PyQt5进阶应用开发
4.1 数据库操作
### 4.1.1 实验目的
1）了解PyQt数据库的重要属性和方法。
2）编写代码，完成数据库的新建、操作（新增、删除、修改、查询）等方法。
### 4.1.2 基础知识
Python操作数据库的流程如下：

SQLite不是一个客户端/服务器结构的数据库引擎，而是一种嵌入式数据库，该数据库本身就是一个文件。SQLite将整个数据库（包括定义、表、索引以及数据本身）作为一个单独的、可跨平台使用的文件存储在主机中。
Python中内置了SQLite3，所以在Python中使用SQLite数据库，不需要安装任何模块，可以直接使用。

创建数据库文件的流程如下图所示：

	数据库创建后就可以对数据进行增删改查等操作了。
操作数据库文件的流程如下图所示：

1）向数据表中新增数据可以使用SQL中的insert语句，语法如下：
2）查询数据表中数据可以使用SQL中的select语句，语法如下：
查询数据库时通常使用如下3种方式：
fetchone()：获取查询结果集中的下一条记录
fetchmany()：获取指定数量的记录
fetchall()：获取结构集的所有记录
3）修改数据表中数据可以使用SQL中的update语句，语法如下：
4）修改数据表中数据可以使用SQL中的delete语句，语法如下：

### 4.1.3 实验步骤
新建数据库
参照第2章在Pycharm软件中新建一个sqlitePyQt工程。
修改main.py的内容，首先创建一个mydb.db的数据库文件，然后执行SQL语句创建一个user（用户表），user表包含了id和name两个字段，代码如下：
import sqlite3
# 连接到SQLite数据库
# 数据库文件是mrsoft.db，如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('mydb.db')
# 创建一个Cursor
cursor = conn.cursor()
# 执行一条SQL语句，创建user表
cursor.execute('create  table  user (id int(10)  primary key, name varchar(20))')
# 关闭游标
cursor.close()
# 关闭Connection
conn.close()
此时运行程序，工程内会新增一个mydb.db数据库文件。


添加数据
接上一小节sqlitePyQt工程继续操作。因为已经创建了user表，所以可直接操作user表，向user表中插入3条用户信息，需要使用commit()方法提交事务。代码如下：
import sqlite3
# 连接到SQLite数据库
# 数据库文件是mydb.db，如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('mydb.db')
# 创建一个Cursor
cursor = conn.cursor()
# 执行一条SQL语句，创建user表
#cursor.execute('create  table  user (id int(10)  primary key, name varchar(20))')
# 执行一条SQL语句，插入一条记录
cursor.execute('insert into user (id, name) values ("1", "hello")')
cursor.execute('insert into user (id, name) values ("2", "python")')
cursor.execute('insert into user (id, name) values ("3", "qt")')
# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭Connection
conn.close()
2）上面代码中创建user表的语句（标记绿色的代码）被注释掉了，因为创建数据库和数据表的操作上一步已完成，如果不注释则会提示user数据表已存在。


查询数据
接上一小节sqlitePyQt工程继续操作，修改main.py注释掉之前的创建数据表、添加数据等代码，然后通过fetchone()方法查询数据并print打印出来。
import sqlite3
# 连接到SQLite数据库
# 数据库文件是mydb.db，如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('mydb.db')
# 创建一个Cursor
cursor = conn.cursor()
# 执行一条SQL语句，创建user表
# cursor.execute('create  table  user (id int(10)  primary key, name varchar(20))')
# 执行一条SQL语句，插入一条记录
# cursor.execute('insert into user (id, name) values ("1", "hello")')
# cursor.execute('insert into user (id, name) values ("2", "python")')
# cursor.execute('insert into user (id, name) values ("3", "qt")')
# 执行查询语句
cursor.execute('select * from user')
# 获取查询结果
result1 = cursor.fetchone()
print(result1)
# 关闭游标
cursor.close()
# 提交事务
#conn.commit()
# 关闭Connection
conn.close()
此时运行代码，在Pycharm软件底部的Run栏中会打印出使用fetchone()方法返回的一个元组。

继续修改main.py，注释掉之前的数据库操作代码，然后通过fetchmany()方法查询数据并print打印出来，打印如下：
import sqlite3
# 连接到SQLite数据库
# 数据库文件是mydb.db，如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('mydb.db')
# 创建一个Cursor
cursor = conn.cursor()
# 执行一条SQL语句，创建user表
# cursor.execute('create  table  user (id int(10)  primary key, name varchar(20))')
# 执行一条SQL语句，插入一条记录
# cursor.execute('insert into user (id, name) values ("1", "hello")')
# cursor.execute('insert into user (id, name) values ("2", "python")')
# cursor.execute('insert into user (id, name) values ("3", "qt")')
# 执行查询语句
cursor.execute('select * from user')
# 获取查询结果
#result1 = cursor.fetchone()
#print(result1)
result2 = cursor.fetchmany(2) # 使用fetchmany方法查询多条数据
print(result2)
# 关闭游标
cursor.close()
# 提交事务
#conn.commit()
# 关闭Connection
conn.close()
此时运行代码，在Pycharm软件底部的Run栏中会打印出fetchmany(2)返回列表中包含的2个元组。

继续修改main.py，注释掉之前的创建数据表、添加数据等代码，然后通过fetchall()方法查询数据并print打印出来。代码如下：
import sqlite3
# 连接到SQLite数据库
# 数据库文件是mydb.db，如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('mydb.db')
# 创建一个Cursor
cursor = conn.cursor()
# 执行一条SQL语句，创建user表
# cursor.execute('create  table  user (id int(10)  primary key, name varchar(20))')
# 执行一条SQL语句，插入一条记录
# cursor.execute('insert into user (id, name) values ("1", "hello")')
# cursor.execute('insert into user (id, name) values ("2", "python")')
# cursor.execute('insert into user (id, name) values ("3", "qt")')
# 执行查询语句
cursor.execute('select * from user')
# 获取查询结果
#result1 = cursor.fetchone()
#print(result1)
#result2 = cursor.fetchmany(2) # 使用fetchmany方法查询多条数据
#print(result2)
result3 = cursor.fetchall() # 使用fetchall方法查询多条数据
print(result3)
# 关闭游标
cursor.close()
# 提交事务
#conn.commit()
# 关闭Connection
conn.close()
此时运行代码，在Pycharm软件底部的Run栏中会打印出fetchall()方法返回列表中包含的所有user表中数据组成的元组。


修改数据
接上一小节继续操作，修改main.py通过updata命令更新user数据表中的第2条数据内容，然后重新查询并打印数据表，代码如下：
import sqlite3
# 连接到SQLite数据库
# 数据库文件是mydb.db，如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('mydb.db')
# 创建一个Cursor
cursor = conn.cursor()
cursor.execute('update user set name = ? where id = ?',('world',2))
cursor.execute('select * from user')
result = cursor.fetchall()
print(result)
# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭Connection
conn.close()
此时运行代码，在Pycharm软件底部的Run栏中会打印user表中的全部数据，可以看到第二条已被修改为“world”。


删除数据
接上一小节继续操作，修改main.py通过delete命令删除user数据表中的第1条数据，然后重新查询并打印数据表，代码如下：
import sqlite3
# 连接到SQLite数据库
# 数据库文件是mydb.db，如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('mydb.db')
# 创建一个Cursor
cursor = conn.cursor()
# 删除ID为1的用户
cursor.execute('delete from user where id = ?',(1,))
# 获取所有用户信息
cursor.execute('select * from user')
# 记录查询结果
result = cursor.fetchall()
print(result)
# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭Connection
conn.close()


### 4.1.4 实验结果
可以通过运行不同程序代码，在PyQt中创建+SQL数据库，并完成了新增、删除、修改、查询等多种数据库操作方法，在Pycharm软件底部的Run栏中会打印出user表中的全部数据。



4.2 文件操作
### 4.2.1 实验目的
1）了解PyQt内置文件操作的重要属性和方法。
2）编写代码，掌握内置文件操作的重要属性的设置方法。
### 4.2.2 基础知识
1）创建和打开文件
open()方法实现创建或打开文件对象，基本语法格式如下：
filename：要创建或打开的文件名称，需要使用单引号或双引号括起来。
mode：可选参数，用于指定文件的打开模式
2）写入文件
write()方法实现向文件中写入内容，基本语法格式如下：
3）读取文件
基本语法格式如下：
4）关闭文件
打开文件后，需要及时关闭，以免对文件造成不必要的破坏。close()语法的格式如下：

### 4.2.3 实验步骤
参照第2章在Pycharm软件中新建一个filePyQt工程。
在Qt Designer中创建一个MainWindow窗口，窗口尺寸为400 x 300，并通过工具箱添加一个PushButton控件和一个LineEdit控件。

通过组合快捷键Ctrl + S保存为filePyQt.ui，然后回到Pycharm软件使用pyUIC工具生成filePyQt.py文件。
修改main.py显示UI主窗口界面，并设定两个控件的初始文本状态，修改代码如下。
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import filePyQt as fileUi
class mainWindow(QMainWindow, fileUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.statusbar.showMessage("输入框为空：按钮为读取；输入框有字符串：按钮为写入")
        self.pushButton.setText('读取\写入')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainWindow()
    ui.show()
    sys.exit(app.exec_())
在mainWindow类的__init__(self)方法中自动创建info.txt文件，并写入内容。代码如下：
        … …
        file = open('info.txt','w')
        file.write("第一条数据。")
        file.close()
在mainWindow类中定义一个getText槽函数，将按钮的clicked信号与槽函数关联。代码如下：
        … …
        file = open('info.txt','w')
        file.write("第一条数据。")
        file.close()
        self.pushButton.clicked.connect(self.getText)
    def getText(self):
        str = self.lineEdit.text()
继续修改getText函数，对输入数据有效性进行判断。判断str为空时，则读取‘info.txt’文件内容，并通过状态栏statusbar显示出来；str不为空，则写入str到‘info.txt’文件，并通过状态栏statusbar显示‘写入成功’，代码如下：
def getText(self):
    str = self.lineEdit.text()
    if str == "":
        file = open('info.txt', 'r')
        info = file.read()
        file.close()
        self.statusbar.showMessage("读取成功："+info)
    else:
        file = open('info.txt', 'w')
        file.write(str)
        file.close()
        self.statusbar.showMessage("写入成功")


### 4.2.4 实验结果
运行程序窗口界面如下，不输入内容直接点击按钮，会读到“第一条数据”。

输入文本内容后点击按钮，会将输入内容写入到文件。再次不输入内容直接点击按钮，会读到新的文件内容，与写入时输入的内容一致。



4.3 多线程-Qtimer
### 4.3.1 实验目的
1）了解PyQt定时器QTimer的重要属性和方法。
2）编写代码，掌握定时器QTimer操作的重要属性的设置方法。
### 4.3.2 基础知识
在PyQt5中，如果需要周期性地执行某项操作，就可以使用QTimer类实现，QTimer类表示计时器，它可以定期发射timeout信号，时间间隔的长度在start()方法中指定，已毫秒为单位，如果要停止计时器，则需要使用方法stop()方法。
在使用QTimer类时，首先需要进行导入，代码如下：
### 4.3.3 实验步骤
参照第2章在Pycharm软件中新建一个qtimePyQt工程。
在Qt Designer中创建一个MainWindow窗口，窗口尺寸为400 x 300，并通过工具箱添加一个PushButton控件和一个ProgressBar控件，通过属性编辑器设置进度条的初始值和按钮的显示文本。

通过组合快捷键Ctrl + S保存为qtimePyQt.ui，然后回到Pycharm软件使用pyUIC工具生成qtimePyQt.py文件。
修改main.py显示UI主窗口界面，代码如下：
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import qtimePyQt as qtimeUi
class mainWindow(QMainWindow, qtimeUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainWindow()
    ui.show()
    sys.exit(app.exec_())
在mainWindow类中定义一个running槽函数，然后将按钮的clicked信号与之关联。代码如下：
btnStatus = False
class mainWindow(QMainWindow, qtimeUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.running)
    def running(self):
        global btnStatus
        if btnStatus:
            self.pushButton.setText("开始")
            btnStatus = False
        else:
            self.pushButton.setText("停止")
            btnStatus = True
编写QTimer相关代码，实现如下功能：
点击开始按钮启动定时器，通过信号timeout与槽函数timeOutFun()关联，定时器每间隔200ms触发一次定时器槽函数，则progressbar进度加1，当到进度达到100%时，则归0。
点击停止按钮后停止定时器。
from PyQt5.QtCore import QTimer
btnStatus = False
i = 0
class mainWindow(QMainWindow, qtimeUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.running)
    def running(self):
        global btnStatus
        if btnStatus:
            self.pushButton.setText("开始")
            btnStatus = False
            self.timer.stop()
        else:
            self.pushButton.setText("停止")
            btnStatus = True
            self.timer = QTimer(self)
            self.timer.start(200)
           self.timer.timeout.connect(self.timOutFun)
    def timOutFun(self):
        global i
        self.progressBar.setProperty("value", i)
        i+=1
        if i > 100:
            i = 0

### 4.3.4 实验结果
运行程序后，点击界面上的开始按钮，进度条控件会自动增加，可以点击停止按钮让进度条暂停，当进度条达到100%后会自动归零。







4.4 多线程-QThread
### 4.4.1 实验目的
1）了解PyQt线程类QThread的重要属性和方法。
2）编写代码，掌握线程类QThread操作的重要属性的设置方法。
### 4.4.2 基础知识
在PyQt5中，要实现一个线程，需要创建QThread类的一个子类，并且实现其run()方法。在使用QThread类时，首先需要进行导入，代码如下：
QThread类常用方法说明：
QThread类的常用信号及说明：
线程的生命周期：

### 4.4.3 实验步骤
参照第2章在Pycharm软件中新建一个qthreadPyQt工程。
在Qt Designer中创建一个MainWindow窗口，窗口尺寸为400 x 300，并通过工具箱添加一个PushButton控件，设置进度条的初始值。

通过组合快捷键Ctrl + S保存为qthreadPyQt.ui，然后回到Pycharm软件使用pyUIC工具生成qthreadPyQt.py文件。
修改main.py显示UI主窗口界面，修改代码如下：
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import qthreadPyQt as qthreadUi
class mainWindow(QMainWindow, qthreadUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainWindow()
    ui.show()
    sys.exit(app.exec_())
修改main.py添加一个PBarThread线程，在该线程中进行计数，并且在窗口启动时调用该线程。
from PyQt5.QtCore import QThread, pyqtSignal
class PBarThread(QThread):
    def __init__(self):
        super(PBarThread, self).__init__()
    def run(self):
        num = 0
        while True:
            num += 1
            QThread.msleep(100)
            if num > 100:
                num = 0
class mainWindow(QMainWindow, qthreadUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.thread = PBarThread()
        self.thread.start()
修改main.py，在PBarThread线程中定时发送sigOut信号。然后定义一个showPBbar槽函数，用于接收PBarThread中emit传送过来的num，并根据num动态显示进度条。并且在__init__(self)方法中将信号与槽函数进行关联。
class PBarThread(QThread):
    sigOut = pyqtSignal(str)
    def __init__(self):
        super(PBarThread, self).__init__()
    def run(self):
        num = 0
        while True:
            num += 1
            self.sigOut.emit(str(num))
            QThread.msleep(100)
            if num > 100:
                num = 0
class mainWindow(QMainWindow, qthreadUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.thread = PBarThread()
        self.thread.sigOut.connect(self.showPBbar)
        self.thread.start()
    def showPBbar(self, str):
        self.progressBar.setProperty("value", int(str))


### 4.4.4 实验结果
运行程序后进度条会自动从0%到100%循环自增变化。





4.5 网络编程-TCP
### 4.5.1 实验目的
1）掌握PyQt网络Socket编程方法。
2）编写TCP客户端进行网络通信。
### 4.5.2 基础知识
Socket模块
Python提供了两个基本的socket模块：
1）socket模块，提供了标准的BSD Sockets API
2）SocketServer模块，提供了服务器中心类，可以简化网络服务器的开发
本节实验，主要是完成socket模块的TCP客户端编程。
socket()函数
Python 中，我们用 socket()函数来创建套接字，语法格式如下：
参数说明：
family: 套接字家族可以使用AF_UNIX或者AF_INET。
type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM。
protocol: 一般不填默认为 0。
Socket 对象(内建)方法
1）服务器端套接字
2）客户端套接字
3）公共用途的套接字函数

### 4.5.3 实验步骤
参照第2章在Pycharm软件中新建一个socketClientPyQt工程。
在Qt Designer中创建一个MainWindow窗口，窗口尺寸为500 x 350，并通过工具箱添加三个Label控件、三个PushButton控件、一个TextBrower控件、一个TextEdit控件，摆到下图中对应的位置，并且设置文本显示初始值。

上图界面中除了接收区和发送区两个Label控件以外，其他的控件在代码中都需要使用，所以要为这些控制设置objectName便于后面代码的编写，依次按照下表中填写objectName，另外控件尺寸也可以参考下表：
通过组合快捷键Ctrl + S保存为socketClientPyQt.ui，然后回到Pycharm软件使用pyUIC工具生成socketClientPyQt.py文件。
修改main.py显示UI主窗口界面，代码如下：
import socket
import sys
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow
import socketClientPyQt as scUi

class mainWindow(QMainWindow, scUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainWindow()
    ui.show()
    sys.exit(app.exec_())
定义个initView函数，初始化连接服务器的Ip地址和端口的显示。
ServerIP = '127.0.0.1'
Port = 8899

class mainWindow(QMainWindow, scUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)

        self.initView()

    def initView(self):
        self.lab_serverinfo.setText("  IP地址：  " + ServerIP + "   端口：" + str(Port))
此时运行代码效果如下：

定义btnConnect、btnDisConnect、btnSend槽函数，然后分别通过“连接服务器”、“断开服务器”和“发送数据”按钮的clicked信号与它们关联。代码如下：
def initView(self):
    self.lab_serverinfo.setText("  IP地址：  " + ServerIP + "   端口：" + str(Port))
    self.pbtn_connect.clicked.connect(self.btnConnect)
    self.pbtn_disconnect.clicked.connect(self.btnDisConnect)
    self.pbtn_disconnect.setEnabled(False)
    self.pbtn_send.clicked.connect(self.btnSend)

def btnConnect(self):
    pass
def btnDisConnect(self):
    pass
def btnSend(self):
    pass
先定义连接的socket以及状态标志位变量，然后分别实现btnConnect、btnDisConnect、btnSend这三个槽函数的功能：
定义变量
class mainWindow(QMainWindow, scUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)

        self.client_th = None
        self.socketClientID = None
        self.socketStatus = False

        self.initView()
实现连接服务器按钮功能
通过socket连接对应IP和端口的服务器，连接成功后提示信息，创建子线程用于接收服务器数据，并将连接状态标志位设为真。
def btnConnect(self):
        self.socketClientID = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            address = (ServerIP, Port)
            self.socketClientID.connect(address)
        except Exception as ret:
            self.statusbar.showMessage('无法连接目标服务器!!!')
            self.socketStatus = False
        else:
            msg = 'TCP客户端已连接IP:%s端口:%s\n' % address
            self.statusbar.showMessage(msg)

            #用于TCP客户端创建子线程的方法，阻塞式接收数据
            self.client_th = threading.Thread(target=self.tcp_client_recv,args=(address,))
            self.client_th.start()
            self.socketStatus = True
            self.pbtn_connect.setEnabled(False)
            self.pbtn_disconnect.setEnabled(True)
实现断开服务器按钮功能
修改连接状态标志位，设置连接和断开按钮的状态，关闭socket。
def btnDisConnect(self):
    try:
        if self.socketStatus:
            self.socketStatus = False
            self.pbtn_connect.setEnabled(True)
            self.pbtn_disconnect.setEnabled(False)
            self.socketClientID.close()
            msg = '已断开网络'
            self.statusbar.showMessage(msg)
    except Exception as ret:
        pass
实现发送数据按钮功能
如果服务器已连接，则获取文本输入框的内容，通过send方法发送给服务器。
def btnSend(self):
    if self.socketStatus is False:
        msg = '请先连接网络服务器'
    else:
        try:
            send_msg = (str(self.textEdit.toPlainText())).encode('utf-8')
            self.socketClientID.send(send_msg)
            msg = 'TCP客户端已发送'
        except Exception as ret:
            msg = '发送失败'
    self.statusbar.showMessage(msg)
实现tcp_client_recv线程，用于处理服务器发送过来的数据，并将接收到的数据在textBrowser中显示出来。
def tcp_client_recv(self,address):
    # 用于TCP客户端创建子线程的方法，阻塞式接收
    while True:
        recv_msg = self.socketClientID.recv(1024)
        if recv_msg:
            msg = recv_msg.decode('utf-8')
            self.textBrowser.insertPlainText(msg)
        else:
            self.socketClientID.close()
            msg = '从服务器断开连接\n'
            self.statusbar.showMessage(msg)
            break


### 4.5.4 实验结果
运行程序界面如下：

可以在光盘开发环境目录中找到SocketTool工具，打开工具选择TCP Server选项，然后点击创建按钮，输入监听端口后确认，端口号需要与代码中一致即可。这样就创建一个TCP服务端。

TCP服务端创建后会自动启动TCP的监听。

这时点击程序的连接服务器按钮，连接后程序连接按钮会变灰，在服务端也会显示已连接。

连接成功后程序和测试工具之间可以通过TCP进行数据收发。


# 附录
附1.1 平台启动
1）将标准220V电源线插入箱体背面的220V电源接口。

2）再将实验平台箱体左侧的220V电源开关从“O”拨到“—”状态，此时箱体内的电源模块会给大底板供电。

3）如果开启电源设备没正常启动，请检查大底板左下角的电源开关是否开启（拨到ON）。另外实验需要使用到摄像头，确保USB SELECT开关拨到右侧（ARM端）。

4）实验平台开机后显示器上会有启动打印，等待系统启动，确保Orin nano边缘计算网关运行的系统是我们提供的Ubuntu 20.04.5 LTS desktop系统（网关系统内已集成各种开发环境，其中Python版本为3.8.10）。系统启动后界面如下：

5）进行系统后，检查无线鼠标及键盘是否能正常使用（蓝牙接收器已接上，鼠标和键盘开关已打开并确保有电）


附1.2 网络连接
PC端开发的PyQt5程序需要通过sftp等工具拷贝到边缘计算网关上运行，所以边缘计算网关与电脑的之间网络通畅是必要条件。边缘计算网关的网络连接可以采用有线或Wifi，确保边缘计算网关和PC在一个局域网内。

以Wifi联网方式为例，具体联网方式如下：
1）点击实验平台屏幕右上角的网络图标，并在弹出网络列表中选择一个Wifi热点名称。（使用试验箱自带的鼠标操作。）

2）在弹出对话框中输入对应Wifi热点的登录密码。（使用试验箱自带的键盘操作。）

3）点击左侧软件列表中的Terminal程序，在弹出窗口中输入ifconfig命令查询网关的IP地址。

4）输入命令后打印如下，其中名为wlan0的即为Wifi的IP地址。如果采用有线方式连接则查看eth0网卡中的IP地址，若未分配IP地址，可以使用指令手动配置IP地址。
ifconfig eth0 192.168.31.146 netmask 255.255.255.0      //手动设置有线网络IP

附1.3 SSH登录
1）运行产品光盘\02-软件环境中的MobaXterm 软件，点击左上角的Session按钮。


2）在弹出的对话框中选择SSH协议，然后点击OK按钮。


3）在SSH的Remote host栏填写网关的IP地址，然后点击OK按钮。


4）然后提示输入登录的账户和密码，用户名为：jetson，密码为：12345678。


5）如果登录的账户和密码验证通过，则会进入到OrinNano网关系统的系统命令行，同时在MobaXterm 软件左侧Stfp栏中可以看到系统的目录结构，可以通过它来双向拷贝文件。




附1.4 文件拷贝
1）MobaXterm软件左侧的Stfp可以显示网关的系统的文件目录，还可以用于文件拷贝，可以提前新建一个文件夹用于存放文件，点击工具栏刷新按钮就可以在目录中找到新增的文件夹。
mkdir test
chmod -R 777 test/

2）然后长按鼠标左键拖动PC端文件至MobaXterm软件左侧的Stfp栏中对应文件夹路径下。


3）拷贝后在Stfp栏中能看到从PC电脑复制过来的文件，在命令行中输入ls命令同样可以查看该文件。


4）MobaXterm软件中的Stfp工具支持单文件、多文件或文件夹拖拽，同时也支持双向拖拽，即可以将网关上的文件反向拖拽至PC电脑。

