# Chapter 4: Advanced PyQt5 Application Development
4.1 Database Operations
### 4.1.1 Objective
1) Understand the important properties and methods of PyQt databases.
2) Write code to implement database creation and operations (insert, delete, update, query).

### 4.1.2 Background
The workflow for operating databases in Python is as follows:

SQLite is not a client/server database engine, but an embedded database that exists as a single file. SQLite stores the entire database (including definitions, tables, indexes, and the data itself) as a standalone, cross-platform file on the host machine.
SQLite3 is built into Python, so no additional modules need to be installed to use an SQLite database in Python.

The workflow for creating a database file is shown below:

Once the database is created, CRUD operations can be performed on the data.
The workflow for operating on a database file is shown below:

1) To insert new data into a table, use the SQL INSERT statement. The syntax is as follows:
2) To query data from a table, use the SQL SELECT statement. The syntax is as follows:
The following three methods are commonly used for database queries:
fetchone(): Retrieves the next record from the query result set.
fetchmany(): Retrieves a specified number of records.
fetchall(): Retrieves all records from the result set.
3) To modify data in a table, use the SQL UPDATE statement. The syntax is as follows:
4) To delete data from a table, use the SQL DELETE statement. The syntax is as follows:

### 4.1.3 Procedure
Create a New Database
Refer to Chapter 2 to create a new `sqlitePyQt` project in PyCharm.
Modify `main.py`. First, create a database file named `mydb.db`, then execute an SQL statement to create a `user` table containing two fields: `id` and `name`. The code is as follows:
import sqlite3
# Connect to SQLite database
# The database file is mrsoft.db; if it does not exist, it will be automatically created in the current directory
conn = sqlite3.connect('mydb.db')
# Create a Cursor
cursor = conn.cursor()
# Execute an SQL statement to create the user table
cursor.execute('create table user (id int(10) primary key, name varchar(20))')
# Close the cursor
cursor.close()
# Close the Connection
conn.close()
Running the program will create a new `mydb.db` database file in the project.

Insert Data
Continue from the `sqlitePyQt` project in the previous section. Since the `user` table has already been created, you can operate on it directly. Insert three user records into the `user` table. The `commit()` method must be called to commit the transaction. The code is as follows:
import sqlite3
# Connect to SQLite database
# The database file is mydb.db; if it does not exist, it will be automatically created in the current directory
conn = sqlite3.connect('mydb.db')
# Create a Cursor
cursor = conn.cursor()
# Execute an SQL statement to create the user table
# cursor.execute('create table user (id int(10) primary key, name varchar(20))')
# Execute an SQL statement to insert a record
cursor.execute('insert into user (id, name) values ("1", "hello")')
cursor.execute('insert into user (id, name) values ("2", "python")')
cursor.execute('insert into user (id, name) values ("3", "qt")')
# Close the cursor
cursor.close()
# Commit transaction
conn.commit()
# Close the Connection
conn.close()
2) In the code above, the statement for creating the `user` table (shown in green) has been commented out because the database and table were already created in the previous step. If not commented out, an error would indicate that the `user` table already exists.

Query Data
Continue from the `sqlitePyQt` project in the previous section. Modify `main.py` to comment out the code for creating the table and inserting data. Then use the `fetchone()` method to query data and print it out.
import sqlite3
# Connect to SQLite database
# The database file is mydb.db; if it does not exist, it will be automatically created in the current directory
conn = sqlite3.connect('mydb.db')
# Create a Cursor
cursor = conn.cursor()
# Execute an SQL statement to create the user table
# cursor.execute('create table user (id int(10) primary key, name varchar(20))')
# Execute an SQL statement to insert a record
# cursor.execute('insert into user (id, name) values ("1", "hello")')
# cursor.execute('insert into user (id, name) values ("2", "python")')
# cursor.execute('insert into user (id, name) values ("3", "qt")')
# Execute a query statement
cursor.execute('select * from user')
# Get the query result
result1 = cursor.fetchone()
print(result1)
# Close the cursor
cursor.close()
# Commit transaction
# conn.commit()
# Close the Connection
conn.close()
Running the code will print a tuple returned by the `fetchone()` method in the Run panel at the bottom of PyCharm.

Continue modifying `main.py` to comment out the previous database operation code. Then use the `fetchmany()` method to query data and print it out as follows:
import sqlite3
# Connect to SQLite database
# The database file is mydb.db; if it does not exist, it will be automatically created in the current directory
conn = sqlite3.connect('mydb.db')
# Create a Cursor
cursor = conn.cursor()
# Execute an SQL statement to create the user table
# cursor.execute('create table user (id int(10) primary key, name varchar(20))')
# Execute an SQL statement to insert a record
# cursor.execute('insert into user (id, name) values ("1", "hello")')
# cursor.execute('insert into user (id, name) values ("2", "python")')
# cursor.execute('insert into user (id, name) values ("3", "qt")')
# Execute a query statement
cursor.execute('select * from user')
# Get the query result
# result1 = cursor.fetchone()
# print(result1)
result2 = cursor.fetchmany(2) # Use fetchmany to query multiple records
print(result2)
# Close the cursor
cursor.close()
# Commit transaction
# conn.commit()
# Close the Connection
conn.close()
Running the code will print 2 tuples contained in the list returned by `fetchmany(2)` in the Run panel at the bottom of PyCharm.

Continue modifying `main.py` to comment out the previous code for creating the table and inserting data. Then use the `fetchall()` method to query data and print it out. The code is as follows:
import sqlite3
# Connect to SQLite database
# The database file is mydb.db; if it does not exist, it will be automatically created in the current directory
conn = sqlite3.connect('mydb.db')
# Create a Cursor
cursor = conn.cursor()
# Execute an SQL statement to create the user table
# cursor.execute('create table user (id int(10) primary key, name varchar(20))')
# Execute an SQL statement to insert a record
# cursor.execute('insert into user (id, name) values ("1", "hello")')
# cursor.execute('insert into user (id, name) values ("2", "python")')
# cursor.execute('insert into user (id, name) values ("3", "qt")')
# Execute a query statement
cursor.execute('select * from user')
# Get the query result
# result1 = cursor.fetchone()
# print(result1)
# result2 = cursor.fetchmany(2) # Use fetchmany to query multiple records
# print(result2)
result3 = cursor.fetchall() # Use fetchall to query multiple records
print(result3)
# Close the cursor
cursor.close()
# Commit transaction
# conn.commit()
# Close the Connection
conn.close()
Running the code will print all records from the `user` table as tuples contained in the list returned by `fetchall()` in the Run panel at the bottom of PyCharm.

Modify Data
Continue from the previous section. Modify `main.py` to use the UPDATE command to update the second record in the `user` table. Then re-query and print the table. The code is as follows:
import sqlite3
# Connect to SQLite database
# The database file is mydb.db; if it does not exist, it will be automatically created in the current directory
conn = sqlite3.connect('mydb.db')
# Create a Cursor
cursor = conn.cursor()
cursor.execute('update user set name = ? where id = ?', ('world', 2))
cursor.execute('select * from user')
result = cursor.fetchall()
print(result)
# Close the cursor
cursor.close()
# Commit transaction
conn.commit()
# Close the Connection
conn.close()
Running the code will print all data from the `user` table in the Run panel at the bottom of PyCharm. The second record should now be updated to "world".

Delete Data
Continue from the previous section. Modify `main.py` to use the DELETE command to delete the first record in the `user` table. Then re-query and print the table. The code is as follows:
import sqlite3
# Connect to SQLite database
# The database file is mydb.db; if it does not exist, it will be automatically created in the current directory
conn = sqlite3.connect('mydb.db')
# Create a Cursor
cursor = conn.cursor()
# Delete the user with ID 1
cursor.execute('delete from user where id = ?', (1,))
# Get all user information
cursor.execute('select * from user')
# Record the query result
result = cursor.fetchall()
print(result)
# Close the cursor
cursor.close()
# Commit transaction
conn.commit()
# Close the Connection
conn.close()

### 4.1.4 Results
By running different program code, an SQLite database can be created in PyQt, and various database operations such as insert, delete, update, and query can be performed. All data from the `user` table will be printed in the Run panel at the bottom of PyCharm.

4.2 File Operations
### 4.2.1 Objective
1) Understand the important properties and methods of PyQt's built-in file operations.
2) Write code to master the configuration of important properties for built-in file operations.

### 4.2.2 Background
1) Creating and Opening Files
The `open()` method is used to create or open a file object. The basic syntax is as follows:
filename: The name of the file to create or open, which must be enclosed in single or double quotes.
mode: An optional parameter that specifies the file opening mode.
2) Writing to a File
The `write()` method is used to write content to a file. The basic syntax is as follows:
3) Reading a File
The basic syntax is as follows:
4) Closing a File
After opening a file, it must be closed promptly to avoid unnecessary damage to the file. The syntax for `close()` is as follows:

### 4.2.3 Procedure
Refer to Chapter 2 to create a new `filePyQt` project in PyCharm.
Create a `MainWindow` window in Qt Designer with dimensions of 400 x 300, and add a `PushButton` control and a `LineEdit` control from the toolbox.

Press Ctrl + S to save it as `filePyQt.ui`, then return to PyCharm and use the `pyUIC` tool to generate the `filePyQt.py` file.
Modify `main.py` to display the main UI window and set the initial text state of the two controls. The modified code is as follows:
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import filePyQt as fileUi
class mainWindow(QMainWindow, fileUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.statusbar.showMessage("Input box empty: button reads; Input box has text: button writes")
        self.pushButton.setText('Read/Write')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainWindow()
    ui.show()
    sys.exit(app.exec_())
In the `__init__(self)` method of the `mainWindow` class, automatically create the `info.txt` file and write content to it. The code is as follows:
        ... ...
        file = open('info.txt', 'w')
        file.write("First piece of data.")
        file.close()
Define a `getText` slot function in the `mainWindow` class, and connect the button's `clicked` signal to this slot function. The code is as follows:
        ... ...
        file = open('info.txt', 'w')
        file.write("First piece of data.")
        file.close()
        self.pushButton.clicked.connect(self.getText)
    def getText(self):
        str = self.lineEdit.text()
Continue modifying the `getText` function to validate the input data. If `str` is empty, read the content of `info.txt` and display it via the `statusbar`. If `str` is not empty, write `str` to `info.txt` and display "Write successful" via the `statusbar`. The code is as follows:
def getText(self):
    str = self.lineEdit.text()
    if str == "":
        file = open('info.txt', 'r')
        info = file.read()
        file.close()
        self.statusbar.showMessage("Read successful: " + info)
    else:
        file = open('info.txt', 'w')
        file.write(str)
        file.close()
        self.statusbar.showMessage("Write successful")

### 4.2.4 Results
The program window interface is shown below. Clicking the button without entering any content will read "First piece of data."

After entering text and clicking the button, the input content will be written to the file. Clicking the button again without entering any content will read the new file content, which matches the previously entered text.

4.3 Multithreading - QTimer
### 4.3.1 Objective
1) Understand the important properties and methods of the PyQt `QTimer` timer class.
2) Write code to master the configuration of important properties for timer operations using `QTimer`.

### 4.3.2 Background
In PyQt5, if you need to execute an operation periodically, you can use the `QTimer` class. `QTimer` represents a timer that periodically emits the `timeout` signal. The time interval is specified in milliseconds in the `start()` method. To stop the timer, use the `stop()` method.
When using the `QTimer` class, it must first be imported. The code is as follows:

### 4.3.3 Procedure
Refer to Chapter 2 to create a new `qtimePyQt` project in PyCharm.
Create a `MainWindow` window in Qt Designer with dimensions of 400 x 300, and add a `PushButton` control and a `ProgressBar` control from the toolbox. Set the initial value of the progress bar and the display text of the button using the Property Editor.

Press Ctrl + S to save it as `qtimePyQt.ui`, then return to PyCharm and use the `pyUIC` tool to generate the `qtimePyQt.py` file.
Modify `main.py` to display the main UI window. The code is as follows:
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
Define a `running` slot function in the `mainWindow` class, and connect the button's `clicked` signal to it. The code is as follows:
btnStatus = False
class mainWindow(QMainWindow, qtimeUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.running)
    def running(self):
        global btnStatus
        if btnStatus:
            self.pushButton.setText("Start")
            btnStatus = False
        else:
            self.pushButton.setText("Stop")
            btnStatus = True
Write the `QTimer`-related code to implement the following functionality:
Click the Start button to start the timer. Connect the `timeout` signal to the `timeOutFun()` slot function. The timer triggers the slot function every 200 ms, incrementing the progress bar value by 1. When the progress reaches 100%, it resets to 0.
Click the Stop button to stop the timer.
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
            self.pushButton.setText("Start")
            btnStatus = False
            self.timer.stop()
        else:
            self.pushButton.setText("Stop")
            btnStatus = True
            self.timer = QTimer(self)
            self.timer.start(200)
            self.timer.timeout.connect(self.timOutFun)
    def timOutFun(self):
        global i
        self.progressBar.setProperty("value", i)
        i += 1
        if i > 100:
            i = 0

### 4.3.4 Results
After running the program, clicking the Start button on the interface will cause the progress bar to increase automatically. The Stop button can be clicked to pause the progress bar. When the progress bar reaches 100%, it will automatically reset to zero.

4.4 Multithreading - QThread
### 4.4.1 Objective
1) Understand the important properties and methods of the PyQt `QThread` thread class.
2) Write code to master the configuration of important properties for thread operations using `QThread`.

### 4.4.2 Background
In PyQt5, to implement a thread, you need to create a subclass of `QThread` and implement its `run()` method. When using the `QThread` class, it must first be imported. The code is as follows:
Common methods of the `QThread` class:
Common signals of the `QThread` class and their descriptions:
Thread lifecycle:

### 4.4.3 Procedure
Refer to Chapter 2 to create a new `qthreadPyQt` project in PyCharm.
Create a `MainWindow` window in Qt Designer with dimensions of 400 x 300, and add a `PushButton` control from the toolbox. Set the initial value of the progress bar.

Press Ctrl + S to save it as `qthreadPyQt.ui`, then return to PyCharm and use the `pyUIC` tool to generate the `qthreadPyQt.py` file.
Modify `main.py` to display the main UI window. The modified code is as follows:
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
Modify `main.py` to add a `PBarThread` thread that performs counting and is started when the window launches.
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
Modify `main.py` to send the `sigOut` signal periodically from the `PBarThread` thread. Then define a `showPBbar` slot function to receive the `num` value emitted by `PBarThread` and dynamically update the progress bar accordingly. Connect the signal to the slot function in the `__init__(self)` method.
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

### 4.4.4 Results
After running the program, the progress bar will automatically cycle from 0% to 100% and repeat.

4.5 Network Programming - TCP
### 4.5.1 Objective
1) Master PyQt network Socket programming methods.
2) Write a TCP client for network communication.

### 4.5.2 Background
Socket Module
Python provides two basic socket modules:
1) The `socket` module, which provides the standard BSD Sockets API.
2) The `SocketServer` module, which provides server-centric classes that simplify network server development.
This section focuses on TCP client programming using the `socket` module.

socket() Function
In Python, the `socket()` function is used to create a socket. The syntax is as follows:
Parameter description:
family: The socket family can be AF_UNIX or AF_INET.
type: The socket type can be SOCK_STREAM (connection-oriented) or SOCK_DGRAM (connectionless).
protocol: Generally left unspecified, defaults to 0.
Socket Object (Built-in) Methods
1) Server-side socket methods
2) Client-side socket methods
3) Common-purpose socket functions

### 4.5.3 Procedure
Refer to Chapter 2 to create a new `socketClientPyQt` project in PyCharm.
Create a `MainWindow` window in Qt Designer with dimensions of 500 x 350, and add three `Label` controls, three `PushButton` controls, one `TextBrowser` control, and one `TextEdit` control from the toolbox. Position them appropriately and set the initial display text.

In the interface above, aside from the two `Label` controls for the receive area and send area, all other controls need to be used in the code. Therefore, set `objectName` for these controls to facilitate coding. Refer to the table below for `objectName` values and control dimensions:
Press Ctrl + S to save it as `socketClientPyQt.ui`, then return to PyCharm and use the `pyUIC` tool to generate the `socketClientPyQt.py` file.
Modify `main.py` to display the main UI window. The code is as follows:
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
Define an `initView` function to initialize the display of the server IP address and port.
ServerIP = '127.0.0.1'
Port = 8899

class mainWindow(QMainWindow, scUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)

        self.initView()

    def initView(self):
        self.lab_serverinfo.setText("  IP Address:  " + ServerIP + "    Port: " + str(Port))
Running the code yields the following result:

Define the `btnConnect`, `btnDisConnect`, and `btnSend` slot functions, then connect them to the `clicked` signals of the "Connect Server", "Disconnect Server", and "Send Data" buttons respectively. The code is as follows:
def initView(self):
    self.lab_serverinfo.setText("  IP Address:  " + ServerIP + "    Port: " + str(Port))
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
First, define the socket connection variable and status flag. Then implement the functionality for the three slot functions `btnConnect`, `btnDisConnect`, and `btnSend`:
Define variables
class mainWindow(QMainWindow, scUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)

        self.client_th = None
        self.socketClientID = None
        self.socketStatus = False

        self.initView()
Implement the Connect Server button functionality
Connect to the server at the specified IP and port via socket. On successful connection, display a confirmation message, create a child thread to receive server data, and set the connection status flag to true.
def btnConnect(self):
    self.socketClientID = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        address = (ServerIP, Port)
        self.socketClientID.connect(address)
    except Exception as ret:
        self.statusbar.showMessage('Unable to connect to target server!!!')
        self.socketStatus = False
    else:
        msg = 'TCP client connected to IP: %s Port: %s\n' % address
        self.statusbar.showMessage(msg)

        # Method for creating a child thread in the TCP client for blocking data reception
        self.client_th = threading.Thread(target=self.tcp_client_recv, args=(address,))
        self.client_th.start()
        self.socketStatus = True
        self.pbtn_connect.setEnabled(False)
        self.pbtn_disconnect.setEnabled(True)
Implement the Disconnect Server button functionality
Modify the connection status flag, update the state of the connect and disconnect buttons, and close the socket.
def btnDisConnect(self):
    try:
        if self.socketStatus:
            self.socketStatus = False
            self.pbtn_connect.setEnabled(True)
            self.pbtn_disconnect.setEnabled(False)
            self.socketClientID.close()
            msg = 'Disconnected from network'
            self.statusbar.showMessage(msg)
    except Exception as ret:
        pass
Implement the Send Data button functionality
If the server is connected, retrieve the content from the text input box and send it to the server using the `send` method.
def btnSend(self):
    if self.socketStatus is False:
        msg = 'Please connect to the network server first'
    else:
        try:
            send_msg = (str(self.textEdit.toPlainText())).encode('utf-8')
            self.socketClientID.send(send_msg)
            msg = 'TCP client has sent data'
        except Exception as ret:
            msg = 'Send failed'
    self.statusbar.showMessage(msg)
Implement the `tcp_client_recv` thread to handle data sent from the server and display the received data in the `textBrowser`.
def tcp_client_recv(self, address):
    # Method for creating a child thread in the TCP client for blocking reception
    while True:
        recv_msg = self.socketClientID.recv(1024)
        if recv_msg:
            msg = recv_msg.decode('utf-8')
            self.textBrowser.insertPlainText(msg)
        else:
            self.socketClientID.close()
            msg = 'Disconnected from server\n'
            self.statusbar.showMessage(msg)
            break

### 4.5.4 Results
The program interface is shown below:

The SocketTool tool can be found in the development environment directory on the product disc. Open the tool, select the TCP Server option, click the Create button, enter the listening port, and confirm. The port number must match the one in the code. This creates a TCP server.

Once the TCP server is created, it will automatically start listening.

At this point, click the Connect Server button in the program. After connecting, the Connect button will become grayed out, and the server will also display a connected status.

After a successful connection, data can be sent and received between the program and the test tool via TCP.

# Appendix
A1.1 Platform Startup
1) Insert the standard 220V power cable into the 220V power interface on the back of the enclosure.

2) Switch the 220V power switch on the left side of the experimental platform enclosure from "O" to "—". At this point, the power module inside the enclosure will supply power to the main board.

3) If the device does not start properly after powering on, check whether the power switch on the lower left corner of the main board is turned on (switch to ON). Additionally, since the experiment requires the use of a camera, ensure the USB SELECT switch is set to the right side (ARM side).

4) After the experimental platform is powered on, startup messages will appear on the display. Wait for the system to boot. Ensure the Orin Nano edge computing gateway is running our provided Ubuntu 20.04.5 LTS desktop system (various development environments are pre-installed in the gateway system, with Python version 3.8.10). The system interface after startup is shown below:

5) After logging into the system, check that the wireless mouse and keyboard are functioning properly (the Bluetooth receiver is plugged in, the mouse and keyboard switches are turned on, and they have sufficient power).

A1.2 Network Connection
PyQt5 programs developed on the PC need to be copied to the edge computing gateway via SFTP or similar tools. Therefore, a stable network connection between the edge computing gateway and the PC is essential. The edge computing gateway can connect to the network via wired Ethernet or Wi-Fi. Ensure the gateway and PC are on the same local area network.

Using Wi-Fi as an example, the connection process is as follows:
1) Click the network icon in the upper right corner of the experimental platform screen, and select a Wi-Fi hotspot from the pop-up network list. (Use the mouse provided with the experimental kit.)

2) Enter the corresponding Wi-Fi hotspot password in the pop-up dialog box. (Use the keyboard provided with the experimental kit.)

3) Click the Terminal program in the software list on the left. In the pop-up window, enter the `ifconfig` command to query the gateway's IP address.

4) The output after entering the command is shown below. The interface named `wlan0` is the Wi-Fi IP address. If using a wired connection, check the IP address on the `eth0` network interface. If no IP address has been assigned, you can manually configure it using the following command:
ifconfig eth0 192.168.31.146 netmask 255.255.255.0      // Manually set the wired network IP

A1.3 SSH Login
1) Run the MobaXterm software located in `\02-Software Environment` on the product disc. Click the Session button in the upper left corner.

2) In the pop-up dialog box, select the SSH protocol, then click the OK button.

3) Enter the gateway's IP address in the Remote host field under SSH, then click the OK button.

4) You will then be prompted to enter the login username and password. The username is: jetson, and the password is: 12345678.

5) If the login credentials are verified successfully, you will enter the system command line of the Orin Nano gateway. Additionally, you can view the system's directory structure in the SFTP panel on the left side of MobaXterm, which allows for bidirectional file transfers.

A1.4 File Copy
1) The SFTP panel on the left side of MobaXterm displays the gateway system's file directory and can also be used for file transfer. You can create a new folder in advance to store files. Click the refresh button on the toolbar to see the newly created folder in the directory.
mkdir test
chmod -R 777 test/

2) Then, hold down the left mouse button and drag files from the PC to the corresponding folder path in the SFTP panel on the left side of MobaXterm.

3) After copying, the file transferred from the PC will be visible in the SFTP panel. You can also view the file by entering the `ls` command in the terminal.

4) The SFTP tool in MobaXterm supports dragging single files, multiple files, or entire folders, as well as bidirectional dragging, meaning files can be dragged from the gateway back to the PC.
