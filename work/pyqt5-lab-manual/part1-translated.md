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
