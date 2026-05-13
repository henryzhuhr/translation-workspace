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
