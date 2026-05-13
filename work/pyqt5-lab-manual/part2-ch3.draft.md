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






