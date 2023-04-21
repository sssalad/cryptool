from PyQt6.QtWidgets import *

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 750

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

        cracking = ["Weiners"]
        self.crackOptions = QComboBox()
        self.crackOptions.addItems(cracking)
        self.optionsLayout.addWidget(QLabel("Type:"), 1, 4)
        self.optionsLayout.addWidget(self.crackOptions, 1, 5)
        
        self.clearButton = QPushButton("Clear")
        self.optionsLayout.addWidget(self.clearButton, 3, 2)
        self.goButton = QPushButton("Go")
        self.optionsLayout.addWidget(self.goButton, 3, 3)
        
        self.generalLayout.addLayout(self.optionsLayout)

    def _creatOutputBox(self):
        self.outputBox = QPlainTextEdit()
        self.outputBox.setReadOnly(True)
        self.outputBox.setMaximumSize(WINDOW_WIDTH, 200)
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