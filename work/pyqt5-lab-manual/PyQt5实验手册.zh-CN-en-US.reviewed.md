# Safety Notice

This document is the "PyQt5 Application Development" manual for the OrinNano IoT AI Experiment Platform. You must read this document carefully before using this product. To ensure normal and safe operation of the product, please note the following:
1) Read this user manual carefully before using the device and keep it for future reference. Illustrations and instructions in this manual may differ slightly from the actual product. The actual product shall prevail.
2) The device should operate in a dry and well-ventilated environment. Do not use it in harsh environments such as high temperature, high pressure, strong magnetic fields, or corrosive conditions.
3) Due to the special nature of electronic products, do not allow conductive liquids (such as water, oil, chemical reagents) or corrosive liquids to spill onto the PCB board. Avoid using this product in humid environments.
4) The experiment platform must use the provided power adapter. Do not connect power supplies with different parameters to this device.
5) Always disconnect power before plugging, unplugging, or connecting any module to avoid electric shock or device short circuits.
6) If a dangerous situation occurs while using the product, cut off the power immediately to prevent further loss.
7) All warning instructions on the device and in the user manual must be strictly followed. Electronic products should be maintained and repaired by qualified technical personnel. Any non-professional maintenance or repair of the products covered in this manual may cause serious damage.

# Table of Contents
Safety Notice	2
Table of Contents	3
Chapter 1 PyQt5 Application Development Basics	5
1.1 Introduction to PyQt5	5
1.2 Experiment Platform Hardware Overview	6
Chapter 2 PyQt5 Environment Setup and Usage	7
2.1 PyQt5 Environment Setup	7
2.2 PyQt5 Application Development Workflow	30
2.3 Importing PyQt5 Experiment Example Projects	43
Chapter 3 PyQt5 Basic Application Development	49
3.1 Window Property Settings	49
3.2 Signals and Slots	55
3.3 Multi-Window Design	62
3.4 Widget Design - Text	68
3.5 Widget Design - Buttons	75
3.6 Widget Design - Time and Date	80
3.7 Widget Design - Progress Bar	83
3.8 Widget Design - Dialogs	86
3.9 Layout Management - Linear	90
3.10 Layout Management - Grid	94
Chapter 4 PyQt5 Advanced Application Development	97
4.1 Database Operations	97
4.2 File Operations	104
4.3 Multithreading - QTimer	108
4.4 Multithreading - QThread	111
4.5 Network Programming - TCP	115
Appendix	124
A1.1 Platform Startup	124
A1.2 Network Connection	126
A1.3 SSH Login	127
A1.4 File Transfer	131

# Chapter 1 PyQt5 Application Development Basics
## 1.1 Introduction to PyQt5
PyQt5 is a Python interface to Digia's powerful graphical program framework Qt. It consists of a set of Python modules and serves as a toolkit for creating GUI applications, developed by Phil Thompson.

Since Qt was first ported to Python in 1998 to form PyQt, three major versions have been released: PyQt3, PyQt4, and PyQt5.

The main features of PyQt5 are as follows:
1) Full encapsulation of the Qt library
2) Communication using the Signals/Slots mechanism
3) Provides a complete set of window widgets for GUI application development
4) Contains over 620 classes and nearly 6,000 functions and methods
5) Cross-platform compatibility across all major operating systems, including UNIX, Windows, and Mac OS
6) Supports GUI design using Qt's visual designer, with the ability to auto-generate Python code

## 1.2 Experiment Platform Hardware Overview
The AI Machine Vision Experiment Platform uses the OrinNano edge computing gateway as its main controller and incorporates hardware modules such as a microphone array, a six-axis robotic arm, wireless sensor network nodes, embedded experiment units, and human-computer interaction units. It can be used for teaching or research in AI fields such as machine vision and natural language processing. The rich set of experiment units on the platform enables scenario-based AI application development, such as door access facial recognition systems and object sorting. The actual product shall prevail for the experiment platform.

# Chapter 2 PyQt5 Environment Setup and Usage
## 2.1 PyQt5 Environment Setup
### 2.1.1 Anaconda3
1. Introduction to Anaconda3
Anaconda3 is an open-source Python and R data science platform focused on simplifying package management, environment management, and scientific computing tasks. It integrates tools such as Conda (a cross-platform package and environment manager), Jupyter Notebook, and Spyder IDE, and is widely used in data analysis, machine learning, scientific computing, and other fields.

2. Key Features:
1) Powerful Package Management (Conda)
Supports installation and management of Python and R libraries (e.g., NumPy, Pandas, TensorFlow).
Automatically resolves dependencies to avoid version conflicts.
Provides both `conda install` and `pip install` for package management.

2) Virtual Environment Management
Allows creation of independent Python environments so different projects can use different Python versions and libraries:

3) Pre-installed 1500+ Scientific Computing Libraries
Data Analysis: Pandas, NumPy, Matplotlib
Machine Learning: Scikit-learn, TensorFlow, PyTorch
Big Data Processing: Dask, Vaex
Visualization: Seaborn, Plotly

4) Integrated Development Tools
Jupyter Notebook (interactive programming and visualization)
Spyder (MATLAB-like scientific computing IDE)
VS Code / PyCharm compatible

5) Cross-Platform Support
Windows / macOS / Linux full platform compatibility

3. Installing Anaconda3
1) In the product CD -> Development Environment -> PyQt5 directory, find the Anaconda3-2020.11-Windows-x86_64.exe file. Right-click and select "Run as administrator" to begin installation. The following interface will appear. Select Next.

2) On the following screen, select I Agree.

3) On the following screen, select Next.

4) On the following screen, use the Browse... button to select the installation path, then select Next.

5) On the following screen, select Install.

6) Wait for the Anaconda3 installation to complete.

7) On the following screen, select Next.

8) On the following screen, select Next.

9) On the following screen, select Finish to complete the Anaconda3 installation.

### 2.1.2 tf2 Virtual Environment
1. Introduction to the tf2 Virtual Environment
A TensorFlow 2 (TF2) virtual environment is an isolated Python runtime environment specifically designed for developing and running TensorFlow 2.x projects. Using a virtual environment prevents dependency conflicts between different projects and keeps the development environment clean and reproducible.

2. Purpose of tf2
Version Isolation: Different TensorFlow projects may require different versions of TF or its dependencies
Avoid System Environment Pollution: Prevents installed packages from affecting other Python projects on the system
Project Reproducibility: Allows precise recording of all project dependencies
Parallel Multi-Project Development: Enables simultaneous development of multiple TF2 projects without interference

3. Setting Up tf2
1) In the product CD -> Development Environment -> PyQt5 directory, find the tf2.zip compressed file, and extract it to the Anaconda3\envs folder.

2) In the Start menu, find the Anaconda Prompt (Anaconda3) option.

3) A cmd command prompt window will appear. Enter the following command to check whether the environment includes the tf2 package:
```
conda info --envs
```

4) Enter the following command to activate the tf2 virtual environment:
```
conda activate tf2
```

5) In the tf2 virtual environment, enter the following command to check the Python version and enter the Python command line:
```
python
```
Use the shortcut Ctrl + Z to exit the environment.

### 2.1.3 Installing PyQt5 and Tools
1) In the tf2 command line, enter the following command to install PyQt5:
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ pyqt5==5.15.2
```

2) Continue in the tf2 command line and enter the following command to install the pyqt5-tools package:
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ pyqt5-tools
```

3) Continue in the tf2 command line and enter the following command to install the pyinstaller tool package:
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller
```

### 2.1.4 PyCharm Installation and Configuration
1) In the product CD -> Development Environment -> PyQt5 directory, find the pycharm-community-2020.3.2.exe file. Right-click and select "Run as administrator" to begin installation. The following interface will appear. Select Next.

2) On the following screen, use the Browse... button to select the installation path, then select Next.

3) On the following screen, check the 3 checkboxes on the left, then select Next.

4) On the following screen, select Install.

5) Wait for the PyCharm installation to complete.

6) On the following screen, select Finish to complete the PyCharm installation.

7) A shortcut will be automatically created on the desktop. Double-click it to run PyCharm.

8) When running PyCharm for the first time, the following prompt will appear. Check the agreement box and select Continue.

9) On the following screen, select Don't Send.

10) The PyCharm welcome screen will appear. Select New Project.

11) When creating a new project, first select the save path in the Location option, then check the "Previously configured interpreter" radio button, and click the ... button next to the Interpreter option.

12) The following screen will appear. Continue by clicking the ... button next to the Interpreter option.

13) In the dialog that appears, browse and select Anaconda3\envs\tf2\python.exe, then click OK to save.

14) Back on the new project screen, the Interpreter option now shows python has been selected. Click Create.

15) After the project is created, the screen will appear as follows.

16) For convenience, you can adjust the PyCharm interface theme. First, select File -> Settings... from the menu bar to open the settings screen.

17) In the settings screen, find the Theme option under Appearance. Select IntelliJ Light from the dropdown menu, then click OK to save.

18) After changing the theme, PyCharm will display in a white color scheme.

19) If PyCharm encounters the following error during operation, the solution is as follows:

Enter `Regedit` in the Run dialog to open the Registry Editor. Navigate to `HKEY_CURRENT_USER\Software\Microsoft\Windows\Windows Error Reporting`, and modify the value of `DontshowUI` to 1.

### 2.1.5 PyQt5 Designer Configuration

**QtDesigner Configuration**
1) Select File -> Settings... from the menu bar to open the settings screen.

2) In the settings screen, find Tools -> External Tools, and click the + button to add Qt Designer.

3) After clicking "+", the "Create Tool" window will appear. Fill in the contents according to the table below, and click OK to save.

4) After saving, the newly added Qt Designer tool can be seen under Tools -> External Tools.

**PyUIC Tool Configuration**
5) Continue in the Tools -> External Tools section and click the + button to add the PyUIC tool.

6) After clicking "+", the "Create Tool" window will appear. Fill in the contents according to the table below, and click OK to save.

7) After saving, the newly added PyUIC tool can be seen under Tools -> External Tools.

8) Once Qt Designer and the PyUIC tool are configured, the previously created Qt Designer and PyUIC tools will appear in PyCharm's Tools -> External Tools menu.

## 2.2 PyQt5 Application Development Workflow
### 2.2.1 Creating a New Project in PyCharm
1) On the PyCharm welcome screen, select New Project to create a new project.

2) On the new project screen, select the project path in Location, check the "Previously configured interpreter" radio button, select Interpreter as Anaconda3\envs\tf2\python.exe, and finally click Create.

### 2.2.2 Designing the UI with Qt Designer
1. Launching Qt Designer
1) In PyCharm, select Tools -> External Tools -> Qt Designer (created earlier) to open the Qt Designer.

2) A window titled "Qt Designer" will launch, as shown below:

2. Creating a New Main Window
1) In the "New Form" window, select the "Main Window" option and click the Create button.
The three most commonly used windows in PyQt5 are described as follows:
- Main Window: A main window that provides a window with a menu bar, toolbar, and status bar
- Widget: A generic window without embedded widgets
- Dialog: A dialog window primarily used for short-term tasks or user interaction, without menu bars, toolbars, or status bars

2) After creation, a window design area named MainWindow will appear in the center of the Qt Designer interface. The Qt Designer interface is divided into the menu bar, toolbar, toolbox, window design area, object inspector, property editor, signal/slot editor, action editor, and resource browser, arranged as follows:

3. Designing the Main Window
1) After creating the main window, it contains only a menu bar and a status bar by default. Find the PushButton widget in the Widget Box toolbox on the left, select it, hold down the left mouse button, and drag it into the main window, as shown below:

2) Because the UI has been modified, an asterisk "*" appears after "MainWindow-untitled", indicating the project is unsaved. Select File -> Save from the menu.

3) After clicking Save, a dialog will pop up. The default save location is the project path. Change the filename to firstPyQt.ui (matching the project name).

4) After the UI file is saved, switch back to PyCharm. The firstPyQt.ui file will automatically appear in the project file list.

### 2.2.3 Converting .ui to .py
1) Select the firstPyQt.ui file, then select Tools -> External Tools -> pyUIC from the menu bar to perform the conversion.

2) After conversion, a firstPyQt.py file will appear in the project file list. Double-click it to view its contents.

### 2.2.4 Creating main.py
1) Through the steps above, firstPyQt.ui has been converted to firstPyQt.py. However, since firstPyQt.py does not have a program entry point, it cannot be run directly. Therefore, we need to modify main.py to serve as the program entry point, calling firstPyQt.py to run.

Add the following code to main.py. It uses `__main__` to set the program entry point and calls the `show()` function through the `MainWindow()` object to display the firstPyQt UI window.

```python
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
```

2) Then select File -> Save All from the menu bar to save the changes.

### 2.2.5 Running the PyQt5 Application on PC
1) Select Run -> Run 'main' from the menu bar to run the program, or click the green run icon on the top-right toolbar.

After the program runs, a window will appear with the same interface as designed.

### 2.2.6 Packaging the PyQt5 Application for PC
After the PyQt5 application project is complete, you can use the pyinstaller tool to package it into a .exe executable for PC. The steps are as follows:
1) First, for convenience, copy the firstPyQt project folder to a disk root directory, such as the D: drive root.

2) Open the Anaconda3 command line and switch to the tf2 virtual environment using the following command:
```
conda activate tf2
```

3) Open the cmd command line and navigate to the project directory, such as D:\firstPyQt shown below:
```
D:
cd firstPyQt
```

4) Enter the following command to package using pyinstaller:
```
pyinstaller -F main.py
```

5) A dist folder will appear in the firstPyQt project directory, containing main.exe as the packaged executable.

6) Run main.exe directly to launch the program.

### 2.2.7 Running the PyQt5 Application on the Gateway
1) Start the experiment platform. Refer to Appendix 1.2 to connect to the network and check the IP address, then remotely log in to the OrinNano edge computing gateway's Ubuntu console terminal via SSH.

2) Refer to Appendix 1.3-1.4 to copy the firstPyQt project folder to a directory on the gateway system.

3) Open the terminal software on the gateway using the mouse. If the icon is not in the left sidebar, click "All Programs" in the top-left corner, search for "Terminal", and drag the icon to the left sidebar.

4) Enter the following command on the keyboard to navigate to the copied project path, then run main.py:
```
cd test/firstPyQt                                                                 # Please use the actual copy path
python3 main.py
```

5) After the program runs, a Qt interface will also appear on the gateway screen, with the same UI as designed.

6) Note: If you run this program directly in the SSH tool, the program will display on the PC side.

## 2.3 Importing PyQt5 Experiment Example Projects
### 2.3.1 Running an Experiment Example Project
1) Extract the experiment example code provided on the CD to the default project save path (typically C:\Users\Username\PycharmProjects).

2) On the PyCharm welcome screen, click Open.

3) Browse and select the project path, then click OK.

4) After the project opens, PyCharm will display the prompt "No Python interpreter configured for the project". Click the "Configure Python interpreter" option next to it.

5) In the pop-up options, select Python 3.7 (tf2).

6) After the error is resolved, run the program directly. The imported example code should run normally.

### 2.3.2 Modifying the Experiment Example UI
Modifying an existing example project's UI can significantly reduce development time. The specific steps are as follows:
1) In PyCharm's Tools -> External Tools menu, select the previously created Qt Designer tool to open Qt Designer.

2) Qt Designer will display the new form dialog by default.

3) Since the example project's UI is already designed, do not create a new one. Instead, select Open.

4) Browse and select the .ui file in the project, then open it.

5) After opening, you can view the UI layout of the example project, as well as settings for windows and various components such as properties, actions, and slots. You can adjust parameters or add/remove components on the interface.

6) After modifying the UI, select File -> Save from the menu bar to overwrite the original .ui file.

7) Finally, in PyCharm, convert the .ui file to .py to apply the modified interface.
# Chapter 3 PyQt5 Basic Application Development

## 3.1 Window Properties

### 3.1.1 Objective

1) Learn how to set PyQt5 window properties.
2) Redesign the UI by configuring PyQt5 properties.

### 3.1.2 Background

The object name of a window serves as its unique identifier. In code, all settings and operations on the window are performed using this name. Window properties can be adjusted through the property editor in Qt Designer, such as setting the object name, title, size, and icon.

### Procedure

Note: This experiment is conducted based on the firstPyQt project created in Chapter 2.

#### 3.1.3.1 Setting Window Name

**Select the Window Object**

In the Qt Designer Object Inspector, select the main form MainWindow.

**Modify the Window Name**

In the Property Editor, change the `QObject -> objectName` property to `firstMain`, then save with the shortcut `Ctrl + S`.

**Convert .ui to .py**

Since the UI has been modified, return to PyCharm and use the pyUIC tool to convert the new `firstPyQt.ui` into `firstPyQt.py`. Open the `firstPyQt.py` file and verify that the window name has been automatically updated.

**Modify main.py**

Open the `main.py` file and modify the corresponding line of code as shown below:

```python
ui = fUi.Ui_firstMain()
```

**Run the Project**

Run the code directly. Since only the window object name was changed, the interface appears unchanged. The window size is 800 x 600 pixels.

#### 3.1.3.2 Setting Window Title Bar

In the Property Editor, locate the `windowTitle` option and change it to `myFirstPyQtAPP`. Save with the shortcut `Ctrl + S`.

Return to PyCharm and use the pyUIC tool to regenerate the `.py` file.

After re-running the program, the window title now displays `myFirstPyQtAPP`.

#### 3.1.3.3 Setting Window Size

In the Property Editor, locate the `geometry` option and change the width and height to 400 x 300. Save with the shortcut `Ctrl + S`.

Return to PyCharm and use the pyUIC tool to regenerate the `.py` file.

After re-running the program, the window is visibly smaller at 400 x 300 pixels.

#### 3.1.3.4 Setting Window Icon

Prepare an icon image and place it in the project directory.

In the Property Editor, locate the `windowIcon` option and click the button on the right.

From the dropdown list that appears, select "Choose File...".

In the "Select Pixmap" dialog that appears, browse to and select the `qt.png` file that was copied earlier, then click Open.

In Qt Designer, save with the shortcut `Ctrl + S`.

Return to PyCharm and use the pyUIC tool to regenerate the `.py` file.

### 3.1.4 Results

After re-running the program, the icon in the top-left corner of the window has changed.

Through the window property settings, the window name, title bar, window size, and window icon were all modified.

---

## 3.2 Signals and Slots

### 3.2.1 Objective

1) Learn how to use PyQt5 signals and slots.
2) Implement button-triggered actions on the UI using PyQt5 signals and slots.
3) Master the method of defining custom slot functions in PyQt5.

### 3.2.2 Background

Signals and slots are the core mechanism of Qt and the foundation for communication between objects in PyQt5 programming. In PyQt5, every QObject (including various windows and widgets) supports the signals and slots mechanism. Through the connection of signals and slots, communication between objects is achieved. When a signal is emitted, the connected slot function (method) executes automatically. In PyQt5, signals and slots are connected using the `signal.connect()` method.

### 3.2.3 Procedure

Note: This experiment is conducted based on the firstPyQt project created in Chapter 2.

#### 3.2.3.1 Editing Signals and Slots

In the Qt Designer Object Inspector, select `pushButton`.

In the Property Editor, locate the `text` option and change its content to "Close".

In the menu bar, select "Edit -> Edit Signals/Slots".

The toolbox and other areas will turn gray. Select the button in the UI window, then press and hold the left mouse button and drag to an empty area.

In the "Configure Connection" dialog that appears, check the checkbox in the bottom-left corner. Select `clicked()` from the left list and `close()` from the right list, then click OK.

After the signal and slot connection is established, preview the window. Save with the shortcut `Ctrl + S`.

Return to PyCharm and use the pyUIC tool to regenerate the `.py` file. The relevant code is automatically added to this file.

Re-run the program. After clicking the Close button, the program window closes automatically.

#### 3.2.3.2 Custom Slots

A custom slot is essentially a user-defined function that implements specific functionality. The procedure is as follows:

**Remove the Original Signal-Slot Connection**

In Qt Designer, select the Signal/Slot Editor, choose the previously created connection, then click the "-" button to delete it. Save with `Ctrl + S`. Return to PyCharm and use the pyUIC tool to regenerate the `.py` file.

**Override the UI Class**

In `main.py`, override the class that inherits the UI. Then, start the interface window from the entry point using the overridden `mainWindow()`. The code is as follows:

```python
class mainWindow(QMainWindow, fUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainWindow()
    ui.show()
    sys.exit(app.exec_())
```

**Define a Custom Slot Function**

Add the `ClickEvent()` slot function to the `mainWindow` class. The modified code is as follows:

```python
class mainWindow(QMainWindow, fUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
    def ClickEvent(self):
        self.statusbar.showMessage("Hello World!")
```

**Connect the Signal and Slot**

In the `mainWindow` class, connect the `clicked` signal to the `ClickEvent()` slot function. The modified code is as follows:

```python
class mainWindow(QMainWindow, fUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        # Connect the pushButton clicked signal to the ClickEvent slot
        self.pushButton.clicked.connect(self.ClickEvent)
    def ClickEvent(self):
        self.statusbar.showMessage("Hello World!")
```

### 3.2.4 Results

Run the code directly. After clicking the Close button in the popup window, the string "Hello World!" is displayed in the bottom-left corner of the window.

---

## 3.3 Multi-Window Design

### 3.3.1 Objective

Learn how to use multiple windows in PyQt5.

### 3.3.2 Background

A complete application typically consists of multiple windows, enabling interaction through popups or window transitions.

### 3.3.3 Procedure

Create a new project named `multiWindow` in PyCharm.

Open Qt Designer via External Tools.

In the default dialog, create a MainWindow. Then, in the menu bar, select File -> New (F)... and create a second MainWindow.

**Modify Window Properties**

- Set the `objectName` of the two windows to `multiWindow1` and `multiWindow2` respectively.
- Set the `windowTitle` of the two windows to `window1` and `window2` respectively.
- Set the width and height of both windows to 300 x 200.
- Add a `pushButton` widget to the `multiWindow1` window.

After configuring the properties, the two windows appear as shown. Select each window and save with `Ctrl + S`, naming them `multiWindow1.ui` and `multiWindow2.ui` respectively.

Return to PyCharm and use the pyUIC tool to convert both `.ui` files into `.py` files.

**Override mainWindow**

Modify the `main.py` code. Override the `mainWindow` class to open the `multiWindow1` window, and have the main function call it at startup.

```python
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
```

**Override window2**

Override the `window2` class to open the `multiWindow2` window.

```python
class window2(QMainWindow, mUi2.Ui_multiWindow2):
    def __init__(self):
        super(window2, self).__init__()
        self.setupUi(self)
```

**Connect the Slot Function**

Add a `showWindow2` slot function to the `mainWindow` class and connect the `pushButton` `clicked` signal to it.

```python
class mainWindow(QMainWindow, mUi1.Ui_multiWindow1):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        # Connect the pushButton clicked signal to the showWindow2 slot
        self.pushButton.clicked.connect(self.showWindow2)
    def showWindow2(self):
        self.window2 = window2()
        self.window2.show()
```

### 3.3.4 Results

After running the program, Window 1 opens. Clicking the PushButton opens Window 2.

---

## 3.4 Widget Design - Text

### 3.4.1 Objective

1) Understand the important properties and methods of PyQt text widgets: QLabel, QTextEdit, and QSpinBox.
2) Write code to master the setup methods for key properties of QLabel, QTextEdit, and QSpinBox.

### 3.4.2 Background

The QLabel widget, also known as a label control, is primarily used to display text that users cannot edit and to identify objects on a form. It corresponds to the `QLabel` class in PyQt5.

The QTextEdit widget is a multi-line text box control used to display multiple lines of text. When the text content exceeds the display range of the widget, a vertical scrollbar is shown.

The QSpinBox widget is an integer spin box that allows users to select an integer value by clicking the up/down buttons or pressing the up/down arrow keys to increase/decrease the displayed value. Users can also type a value directly.

### 3.4.3 Procedure

#### 3.4.3.1 QLabel

Create a new project named `textPyQt` in PyCharm (refer to Chapter 2), and copy the `qt.png` image file to the project root directory (the image can be found in the experiment source code for this chapter).

In Qt Designer, create a `MainWindow` with dimensions 400 x 300. Add two QLabel components from the toolbox, setting their `objectName` properties to `label1` and `label2`.

In Qt Designer, save as `textPyQt.ui` with the shortcut `Ctrl + S`. Return to PyCharm and use the pyUIC tool to generate the `textPyQt.py` file.

Modify the `main.py` code. Use the `setText` method to display text on `label1`, and set an image with coordinates and size on `label2`. The code is as follows:

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
import textPyQt as textUi

class mainWindow(QMainWindow, textUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.label1.setText("Hello!!!")
        self.label2.setGeometry(QtCore.QRect(160, 100, 60, 60))
        self.label2.setPixmap(QPixmap('qt.png'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainWindow()
    ui.show()
    sys.exit(app.exec_())
```

Run the program directly. The popup window interface appears as shown.

#### 3.4.3.2 QTextEdit

Note: This section builds upon the experimental code from the previous section.

In Qt Designer, add a QTextEdit widget to the window.

In Qt Designer, save `textPyQt.ui` with `Ctrl + S`. Return to PyCharm and use the pyUIC tool to regenerate the `textPyQt.py` file.

Modify the `main.py` code. Use the `setPlainText` method to add a long string to `textEdit`. The modified code is as follows:

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
import textPyQt as textUi

class mainWindow(QMainWindow, textUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.label1.setText("Hello!!!")
        self.label2.setGeometry(QtCore.QRect(160, 100, 60, 60))
        self.label2.setPixmap(QPixmap('qt.png'))
        self.textEdit.setPlainText("This is a sample multi-line text. You can scroll through all the content using the scrollbar.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainWindow()
    ui.show()
    sys.exit(app.exec_())
```

Run the program. Drag the scrollbar to browse through all the text.

#### 3.4.3.3 QSpinBox

Note: This section builds upon the experimental code from the previous section.

In Qt Designer, add a QSpinBox widget to the window.

In Qt Designer, save `textPyQt.ui` with `Ctrl + S`. Return to PyCharm and use the pyUIC tool to regenerate the `textPyQt.py` file.

Modify the `main.py` code. Use the `setRange` and `setSingleStep` methods to set the range and step size for the QSpinBox widget. The modified code is as follows:

```python
class mainWindow(QMainWindow, textUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.label1.setText("Hello!!!")
        self.label2.setGeometry(QtCore.QRect(160, 100, 60, 60))
        self.label2.setPixmap(QPixmap('qt.png'))
        self.textEdit.setPlainText("This is a sample multi-line text. You can scroll through all the content using the scrollbar.")
        self.spinBox.setRange(0, 66)        # Set range
        self.spinBox.setSingleStep(3)       # Set step size
```

Define a `getvalue` slot function in the `mainWindow` class:

```python
def getvalue(self):
    self.label1.setText(str(self.spinBox.value()))
```

Connect the `spinBox` `valueChanged` signal to the custom `getvalue()` slot function:

```python
class mainWindow(QMainWindow, textUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.label1.setText("Hello!!!")
        self.label2.setGeometry(QtCore.QRect(160, 100, 60, 60))
        self.label2.setPixmap(QPixmap('qt.png'))
        self.textEdit.setPlainText("This is a sample multi-line text. You can scroll through all the content using the scrollbar.")
        self.spinBox.setRange(0, 66)        # Set range
        self.spinBox.setSingleStep(3)       # Set step size
        self.spinBox.valueChanged.connect(self.getvalue)
```

### 3.4.4 Results

In the program window, clicking the arrows on the QSpinBox widget changes the displayed value, starting from 0 and incrementing by 3 each time. The QLabel1 widget synchronously displays the numeric change through the signal and slot mechanism.

Three different types of text widgets were created in the form, and the usage methods for each were learned.

---

## 3.5 Widget Design - Button

### 3.5.1 Objective

1) Understand the important properties and methods of PyQt button widgets: QPushButton and QCheckBox.
2) Write code to master the setup methods for key properties of QPushButton and QCheckBox.

### 3.5.2 Background

The QPushButton widget is a command button that allows users to perform an action by clicking. It can display either text or an image. When clicked, the button is pressed and then released.

The QCheckBox widget is a checkbox control, commonly used to provide users with yes/no or true/false options. It corresponds to the `QCheckBox` class.

### 3.5.3 Procedure

#### 3.5.3.1 QPushButton

Create a new project named `buttonPyQt` in PyCharm (refer to Chapter 2), and copy the `login.ico` image file to the project root directory (the image can be found in the experiment source code for this chapter).

In Qt Designer, create a `MainWindow` with dimensions 400 x 300. Add a QPushButton widget from the toolbox.

In Qt Designer, save as `buttonPyQt.ui` with `Ctrl + S`. Return to PyCharm and use the pyUIC tool to generate the `buttonPyQt.py` file.

Modify the `main.py` code. Use the `setText` method to change the button's text and the `setIcon` method to specify the button's image. The modified code is as follows:

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import buttonPyQt as butUi
from PyQt5.QtGui import QIcon, QPixmap

class mainWindow(QMainWindow, butUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.setText("Button")
        self.pushButton.setIcon(QIcon(QPixmap("login.ico")))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainWindow()
    ui.show()
    sys.exit(app.exec_())
```

Run the program. The QPushButton displays the specified image and text.

#### 3.5.3.2 QCheckBox

Continue working in the `buttonPyQt` project in Qt Designer. Add a QCheckBox widget.

In Qt Designer, save `buttonPyQt.ui` with `Ctrl + S`. Return to PyCharm and use the pyUIC tool to regenerate the `buttonPyQt.py` file.

Modify the `main.py` code. Add the following to set the text and image for the QCheckBox widget:

```python
self.checkBox.setText("Learn this skill")
self.checkBox.setIcon(QIcon(QPixmap("login.ico")))
```

Define a slot function `setBtnText` in the `mainWindow` class:

```python
def setBtnText(self):
    if self.checkBox.isChecked():
        self.pushButton.setText("Checked")
    else:
        self.pushButton.setText("Unchecked")
```

The most commonly used signal for the QCheckBox widget is `stateChanged`, which is emitted when the checkbox state changes. Add the code to connect the `checkBox` `stateChanged` signal to the `setBtnText` slot function:

```python
self.checkBox.setText("Learn this skill")
self.checkBox.setIcon(QIcon(QPixmap("login.ico")))
self.checkBox.stateChanged.connect(self.setBtnText)
```

The complete `main.py` code is as follows:

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import buttonPyQt as butUi
from PyQt5.QtGui import QIcon, QPixmap

class mainWindow(QMainWindow, butUi.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.setText("Button")
        self.pushButton.setIcon(QIcon(QPixmap("login.ico")))
        self.checkBox.setText("Learn this skill")
        self.checkBox.setIcon(QIcon(QPixmap("login.ico")))
        self.checkBox.stateChanged.connect(self.setBtnText)

    def setBtnText(self):
        if self.checkBox.isChecked():
            self.pushButton.setText("Checked")
        else:
            self.pushButton.setText("Unchecked")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainWindow()
    ui.show()
    sys.exit(app.exec_())
```

### 3.5.4 Results

Run the program.

When the checkBox is checked, the PushButton text changes to "Checked".

When the checkBox is unchecked, the PushButton text changes to "Unchecked".

---

## 3.6 Widget Design - Date/Time

### 3.6.1 Objective

1) Understand the important properties and methods of the PyQt date/time widget QDateTimeEdit.
2) Write code to master the setup methods for key properties of QDateTimeEdit.

### 3.6.2 Background

The QDateTimeEdit widget corresponds to the `QDateTimeEdit` class. This widget can display and edit both date and time simultaneously. Its most commonly used signal is `dateTimeChanged`, which is emitted when the date or time changes.

### 3.6.3 Procedure

Create a new project named `timePyQt` in PyCharm (refer to Chapter 2).

In Qt Designer, create a `MainWindow` with dimensions 400 x 300. Add a QDateTimeEdit widget and a QLabel widget from the toolbox.

In Qt Designer, save as `timePyQt.ui` with `Ctrl + S`. Return to PyCharm and use the pyUIC tool to generate the `timePyQt.py` file.

Modify `main.py`. In the `__init__(self)` method of the `mainWindow` class, define the `showChangeTime()` slot function:

```python
def showChangeTime(self):
    self.label.setText(self.dateTimeEdit.text())
```

Add the connection between the `dateTimeChanged` signal of the QDateTimeEdit and the `showChangeTime` slot function. Also synchronize with the system time and set the date/time display format:

```python
self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
self.dateTimeEdit.setDisplayFormat("yyyy/MM/dd hh:mm:ss")
self.dateTimeEdit.dateTimeChanged.connect(self.showChangeTime)
```

### 3.6.4 Results

Run the program. The QDateTimeEdit widget displays the current date and time.

Select the date or time within the QDateTimeEdit widget and click the up/down arrows to adjust it. The modified date and time are synchronously displayed on the QLabel widget through the signal and slot mechanism.

---

## 3.7 Widget Design - Progress Bar

### 3.7.1 Objective

1) Understand the important properties and methods of the PyQt progress bar widget QProgressBar.
2) Write code to master the setup methods for key properties of QProgressBar.

### 3.7.2 Background

The QProgressBar widget corresponds to the `QProgressBar` class. It is typically used during long-running tasks to inform users of the current progress. Its most commonly used signal is `valueChanged`, which is emitted when the progress bar value changes.

### 3.7.3 Procedure

Create a new project named `progressbarPyQt` in PyCharm (refer to Chapter 2).

In Qt Designer, create a `MainWindow` with dimensions 400 x 300. Add a QPushButton widget and a QProgressBar widget from the toolbox.

Save as `progressbarPyQt.ui` with the shortcut `Ctrl + S`. Return to PyCharm and use the pyUIC tool to generate the `progressbarPyQt.py` file.

In the `__init__(self)` method of the `mainWindow` class in `main.py`, set the default value of the progress bar to 0% and change the text of the PushButton:

```python
self.progressBar.setValue(0)   # Set the progress bar value
self.pushButton.setText("Start")
```

In the `__init__(self)` method of the `mainWindow` class in `main.py`, write the `running()` slot function:

```python
def running(self):
    global i
    self.progressBar.setMaximum(100)
    self.progressBar.setProperty("value", i)
    i += 10
    if i > 100:
        i = 0
```

Connect the PushButton `clicked` signal to the `running` slot function:

```python
self.progressBar.setValue(0)   # Set the initial value of the progress bar
self.pushButton.setText("Start")
self.pushButton.clicked.connect(self.running)
```

### 3.7.4 Results

Run the program.

Click the Start button on the interface to advance the progress bar. Each click increases the progress by 10%. When it reaches 100%, clicking the button again resets the progress bar to 0%.

---

## 3.8 Widget Design - Dialog

### 3.8.1 Objective

1) Understand the important properties and methods of the PyQt dialog widget QMessageBox.
2) Write code to master the setup methods for key properties of QMessageBox.

### 3.8.2 Background

The `QMessageBox` widget represents a dialog box. It includes five built-in dialog types: Information, Question, Warning, Error, and About. The syntax is as follows:

```
QMessageBox.information(QWidget=?, 'title', 'Content', buttons=?, defaultButton=? )
```

- `QWidget`: `self` or a window object, indicating the parent window of the dialog.
- `Title`: A string representing the dialog title.
- `Content`: A string representing the dialog message content.
- `Buttons`: The buttons to be added to the dialog.
- `defaultButton`: The button selected by default.

### 3.8.3 Procedure

Create a new project named `messageboxPyQt` in PyCharm (refer to Chapter 2).

In Qt Designer, create a `MainWindow` with dimensions 400 x 300. Add five QPushButton widgets from the toolbox. Select each button and modify their properties in the Property Editor:

- `QObject -> objectName`: `pushButton1`, `pushButton2`, `pushButton3`, `pushButton4`, `pushButton5`.
- `QAbstractButton -> text`: "Information", "Warning", "Question", "Error", "About".

Save as `messageboxPyQt.ui` with `Ctrl + S`. Return to PyCharm and use the pyUIC tool to generate the `messageboxPyQt.py` file.

In the `mainWindow` class in `main.py`, write the slot functions for the five dialogs in the `__init__(self)` method:

```python
def info(self):
    QMessageBox.information(None, 'Info', 'Information Dialog!', QMessageBox.Ok)
def warning(self):
    QMessageBox.warning(None, 'Warning', 'Warning Dialog!', QMessageBox.Ok)
def question(self):
    QMessageBox.question(None, 'Question', 'Question Dialog!', QMessageBox.Ok)
def error(self):
    QMessageBox.critical(None, 'Error', 'Error Dialog!', QMessageBox.Ok)
def about(self):
    QMessageBox.about(None, 'About', 'About Dialog!')
```

Connect the `clicked` signals of the five PushButtons to their respective slot functions:

```python
self.pushButton1.clicked.connect(self.info)
self.pushButton2.clicked.connect(self.warning)
self.pushButton3.clicked.connect(self.question)
self.pushButton4.clicked.connect(self.error)
self.pushButton5.clicked.connect(self.about)
```

### 3.8.4 Results

Click each of the five buttons on the interface in sequence to display the corresponding dialog effects.

---

## 3.9 Layout Management - Linear

### 3.9.1 Objective

1) Understand the important properties and methods of PyQt linear layouts.
2) Write code to implement linear layout configurations.

### 3.9.2 Background

A linear layout arranges components in either a vertical or horizontal direction. The base class of `Vertical Layout` is `QVBoxLayout`, while the base class of `Horizontal Layout` is `QHBoxLayout`.

### 3.9.3 Procedure

Note: Unlike the previous experiments, this section does not use Qt Designer for UI design. Instead, the UI is designed entirely through code.

#### 3.9.3.1 VerticalLayout (Vertical Layout)

Create a new project named `vlayoutPyQt` in PyCharm (refer to Chapter 2).

Override the `main.py` code. The custom `initUI` method is called during initialization to set up a vertical layout:

```python
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.initUI()  # Initialize the window

    def initUI(self):
        vlayout = QVBoxLayout()
        self.setLayout(vlayout)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)  # Create the application
    demo = Demo()                  # Create the window object
    demo.show()                    # Display the window
    sys.exit(app.exec_())
```

If the code is run at this point, the window appears empty.

Next, add three buttons to the `vlayout` vertical layout in `initUI`. Use the `addWidget()` method to add widgets and the `addSpacing()` method to set vertical spacing between widgets:

```python
def initUI(self):
    vlayout = QVBoxLayout()
    btn1 = QPushButton()
    btn1.setText('Button 1')
    btn2 = QPushButton()
    btn2.setText('Button 2')
    btn3 = QPushButton()
    btn3.setText('Button 3')
    vlayout.addWidget(btn1)
    vlayout.addSpacing(10)
    vlayout.addWidget(btn2)
    vlayout.addSpacing(30)
    vlayout.addWidget(btn3)
    self.setLayout(vlayout)
```

Run the code. The three buttons are arranged vertically in sequence.

#### 3.9.3.2 HorizontalLayout (Horizontal Layout)

Create a new project named `hlayoutPyQt` in PyCharm (refer to Chapter 2).

Override the `main.py` code. The custom `initUI` method is called during initialization to set up a horizontal layout:

```python
from PyQt5.QtWidgets import *

class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.initUI()  # Initialize the window

    def initUI(self):
        hlayout = QHBoxLayout()
        self.setLayout(hlayout)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)  # Create the application
    demo = Demo()                  # Create the window object
    demo.show()                    # Display the window
    sys.exit(app.exec_())
```

If the code is run at this point, the window appears empty.

Next, add three buttons to the `hlayout` horizontal layout in `initUI`. Use the `addWidget()` method to add widgets and the `addSpacing()` method to set horizontal spacing between widgets:

```python
def initUI(self):
    hlayout = QHBoxLayout()
    btn1 = QPushButton()
    btn1.setText('Button 1')
    btn2 = QPushButton()
    btn2.setText('Button 2')
    btn3 = QPushButton()
    btn3.setText('Button 3')
    hlayout.addWidget(btn1)
    hlayout.addSpacing(10)
    hlayout.addWidget(btn2)
    hlayout.addSpacing(30)
    hlayout.addWidget(btn3)
    self.setLayout(hlayout)
```

Run the code. The three buttons are arranged horizontally in sequence.

### 3.9.4 Results

Running the first program: three buttons are arranged vertically in sequence.

Running the second program: three buttons are arranged horizontally in sequence.

---

## 3.10 Layout Management - Grid

### 3.10.1 Objective

1) Understand the important properties and methods of the PyQt grid layout.
2) Write code to implement grid layout configurations.

### 3.10.2 Background

The grid layout, also known as GridLayout, arranges widgets placed within it into a multi-row, multi-column grid. The GridLayout divides the allocated space into rows and columns and inserts each widget into the appropriate cell.

The base class of `Grid Layout` is `QGridLayout`. Common methods are described below.

### 3.10.3 Procedure

Note: Unlike the previous experiments, this section does not use Qt Designer for UI design. Instead, the UI is designed entirely through code.

Create a new project named `gridPyQt` in PyCharm (refer to Chapter 2).

Override the `main.py` code. The custom `initUI` method is called during initialization to set up a grid layout:

```python
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.initUI()  # Initialize the window

    def initUI(self):
        grid = QGridLayout()  # Create a grid layout
        self.setLayout(grid)  # Set the grid layout

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)  # Create the application
    demo = Demo()                  # Create the window object
    demo.show()                    # Display the window
    sys.exit(app.exec_())
```

Next, implement a login window using the `grid` grid layout in `initUI`:

```python
def initUI(self):
    grid = QGridLayout()  # Create a grid layout

    # Create and set the label text
    label1 = QLabel()
    label1.setText("Username:")
    # Create a text input field
    text1 = QLineEdit()
    # Create and set the label text
    label2 = QLabel()
    label2.setText("Password:")
    # Create a text input field
    text2 = QLineEdit()
    # Create "Login" and "Cancel" buttons
    btn1 = QPushButton()
    btn1.setText("Login")
    btn2 = QPushButton()
    btn2.setText("Cancel")

    # Row 1, Column 1: Add label widget with left alignment
    grid.addWidget(label1, 0, 0, QtCore.Qt.AlignLeft)
    # Row 1, Column 2: Add text input widget with left alignment
    grid.addWidget(text1, 0, 1, QtCore.Qt.AlignLeft)
    # Row 2, Column 1: Add label widget with left alignment
    grid.addWidget(label2, 1, 0, QtCore.Qt.AlignLeft)
    # Row 2, Column 2: Add text input widget with left alignment
    grid.addWidget(text2, 1, 1, QtCore.Qt.AlignLeft)
    # Row 3, Column 1: Add button widget with center alignment
    grid.addWidget(btn1, 2, 0, QtCore.Qt.AlignCenter)
    # Row 3, Column 2: Add button widget with center alignment
    grid.addWidget(btn2, 2, 1, QtCore.Qt.AlignCenter)

    self.setLayout(grid)  # Set the grid layout
```

### 3.10.4 Results

Run the program. The widgets in the interface are positioned and aligned using the grid layout.
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
