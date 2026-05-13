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

