from PyQt6.QtWidgets import *
from PyQt6.QtGui import QDoubleValidator, QIntValidator, QRegularExpressionValidator
import string

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 750

class caesarCipherPopup(QWidget):
    def __init__(self, parent=None):
        self.parent = parent
        self.defaultAlphabet = string.ascii_lowercase

        QWidget.__init__(self)
        self.setWindowTitle("Caesar Cipher Settings")

        self.ccAlphabet = QLineEdit()
        self.ccAlphabet.insert(self.defaultAlphabet)

        self.ccShift = QLineEdit()
        self.ccShift.setValidator(QIntValidator())
        self.ccShift.setText("7")

        self.ccMaintainCase = QCheckBox()
        self.ccMaintainCase.setChecked(True)

        self.ccMaintainForeignChar = QCheckBox()
        self.ccMaintainForeignChar.setChecked(True)

        self.ccShiftNumbers = QCheckBox()
        self.ccShiftNumbers.setChecked(False)

        self.ccSaveButton = QPushButton("Save")
        self.ccSaveButton.clicked.connect(self.setCCSettings)

        self.layout = QFormLayout()
        self.layout.addRow("Alphabet:", self.ccAlphabet)
        self.layout.addRow("Shift:", self.ccShift)
        self.layout.addRow("Maintain Case:", self.ccMaintainCase)
        self.layout.addRow("Maintain Foreign Characters:", self.ccMaintainForeignChar)
        self.layout.addRow("Shift Numbers:", self.ccShiftNumbers)
        self.layout.addRow("", self.ccSaveButton)
        self.setLayout(self.layout)

        # Send default settings to the main window
        self.parent.setCCSettings(self.ccAlphabet.text(), self.ccShift.text(), self.ccMaintainCase.isChecked(), self.ccMaintainForeignChar.isChecked(), self.ccShiftNumbers.isChecked())

    # Set values here, and also set them in the main window
    def setCCSettings(self):
        self.parent.setCCSettings(self.ccAlphabet.text(), self.ccShift.text(), self.ccMaintainCase.isChecked(), self.ccMaintainForeignChar.isChecked(), self.ccShiftNumbers.isChecked())

class XORPopup(QWidget):
    def __init__(self, parent=None):
        self.parent = parent

        QWidget.__init__(self)
        self.setWindowTitle("XOR Settings")

        encodingTypes = ["Binary", "Decimal", "Hexidecimal", "Base64", "Text"]
        self.XORinputType = QComboBox()
        self.XORoutputType = QComboBox()
        self.XORkeyType = QComboBox()
        self.XORinputType.addItems(encodingTypes)
        self.XORoutputType.addItems(encodingTypes)
        self.XORkeyType.addItems(encodingTypes)

        self.XORKey = QLineEdit()

        self.SaveButton = QPushButton("Save")
        self.SaveButton.clicked.connect(self.setXORSettings)

        self.layout = QFormLayout()
        self.layout.addRow("Input Type:", self.XORinputType)
        self.layout.addRow("Output Type:", self.XORoutputType)
        self.layout.addRow("Key:", self.XORKey)
        self.layout.addRow("Key Type:", self.XORkeyType)
        self.layout.addRow("", self.SaveButton)
        self.setLayout(self.layout)

        # Send default settings to the main window
        self.parent.setXORSettings(self.XORinputType.currentText(), self.XORoutputType.currentText(), self.XORKey.text(), self.XORkeyType.currentText())

    # Set values here, and also set them in the main window
    def setXORSettings(self):
        self.parent.setXORSettings(self.XORinputType.currentText(), self.XORoutputType.currentText(), self.XORKey.text(), self.XORkeyType.currentText())



class cryptoolWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("cryptool")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createInputBox()
        self._createOptions()
        self._creatOutputBox()
        self.action = ''

    def _createInputBox(self):
        self.inputBox = QPlainTextEdit()
        self.inputBox.setMaximumSize(WINDOW_WIDTH, 200)
        self.inputBox.setPlaceholderText("Input")
        self.generalLayout.addWidget(self.inputBox)

    def _createOptions(self):
        self.optionsLayout = QGridLayout()
        convertButton = QRadioButton("Convert")
        convertButton.action = "Convert"
        convertButton.toggled.connect(self.setAction)
        self.optionsLayout.addWidget(convertButton, 0, 0)

        encryptButton = QRadioButton("Encrypt")
        encryptButton.action = "Encrypt"
        self.optionsLayout.addWidget(encryptButton, 0, 2)
        encryptButton.toggled.connect(self.setAction)

        crackButton = QRadioButton("Crack")
        crackButton.action = "Crack"
        self.optionsLayout.addWidget(crackButton, 0, 4)
        crackButton.toggled.connect(self.setAction)
        
        converting = ["Binary", "Decimal", "Hexidecimal", "Base64", "Text"]
        self.convertOptionsFrom = QComboBox()
        self.convertOptionsTo = QComboBox()
        self.convertOptionsFrom.addItems(converting)
        self.convertOptionsTo.addItems(converting)
        self.optionsLayout.addWidget(QLabel("From:"), 1, 0)
        self.optionsLayout.addWidget(self.convertOptionsFrom, 1, 1)
        self.optionsLayout.addWidget(QLabel("To:"), 2, 0)
        self.optionsLayout.addWidget(self.convertOptionsTo, 2, 1)

        encrypting = ["Caesar Cipher", "XOR", "RSA"]
        self.encryptOptions = QComboBox()
        self.encryptOptions.addItems(encrypting)
        self.optionsLayout.addWidget(QLabel("Type:"), 1, 2)
        self.optionsLayout.addWidget(self.encryptOptions, 1, 3)
        self.settingsButton = QPushButton("Settings")
        self.optionsLayout.addWidget(self.settingsButton, 2, 2)


        cracking = ["Weiners"]
        self.crackOptions = QComboBox()
        self.crackOptions.addItems(cracking)
        self.optionsLayout.addWidget(QLabel("Type:"), 1, 4)
        self.optionsLayout.addWidget(self.crackOptions, 1, 5)
        
        self.byByteCheck = QCheckBox("By Byte")
        self.optionsLayout.addWidget(self.byByteCheck, 3, 1)
        self.clearButton = QPushButton("Clear")
        self.optionsLayout.addWidget(self.clearButton, 3, 2)
        self.goButton = QPushButton("Go")
        self.optionsLayout.addWidget(self.goButton, 3, 3) 
        
        self.generalLayout.addLayout(self.optionsLayout)

    def _creatOutputBox(self):
        self.outputBox = QPlainTextEdit()
        self.outputBox.setReadOnly(True)
        self.outputBox.setMaximumSize(WINDOW_WIDTH, 200)
        self.outputBox.setPlaceholderText("Output")
        self.generalLayout.addWidget(self.outputBox)

    ########################################
    def clearDisplay(self):
        self.inputBox.clear()
        self.outputBox.clear()

    def displayOutput(self, text):
        self.outputBox.setPlainText(text)

    def setAction(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.action = radioButton.action

    def settingsPopup(self):
        #self.cc = caesarCipherPopup()
        #self.cc.setGeometry(100, 100, 400, 200) # how to place nicely in the middle?
        if self.encryptOptions.currentText() == "Caesar Cipher":
            self.cc = caesarCipherPopup(parent=self)
            self.cc.resize(400, 200)
            self.cc.show()
        elif self.encryptOptions.currentText() == "XOR":
            self.xor = XORPopup(parent=self)
            self.xor.resize(400, 200)
            self.xor.show()

    def setCCSettings(self, alphabet, shift, maintainCase, maintainForeignChar, shiftNumbers):
        self.ccAlphabet = alphabet
        self.ccShift = shift
        self.ccMaintainCase = maintainCase
        self.ccMaintainForeignChar = maintainForeignChar
        self.ccShiftNumbers = shiftNumbers

    def setXORSettings(self, inputType, outputType, key, keyType):
        self.XORinputType = inputType
        self.XORoutputType = outputType
        self.XORKey = key
        self.XORkeyType = keyType