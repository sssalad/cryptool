from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIntValidator
import string
from encryptors import caesarCipherMain

class caesarCipherWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        
        # Create stuff
        self._createInputBox()
        self._createOptions()
        self._createOutputBox()

        # Connect slots
        self.clearButton.clicked.connect(self.clearDisplay)
        self.goButton.clicked.connect(self.caesarCipher)

        self.setLayout(self.layout)

    def _createInputBox(self):
        self.inputBox = QPlainTextEdit()
        self.inputBox.setPlaceholderText("Input")
        self.layout.addWidget(self.inputBox, 0, 0, 1, 4)

    def _createOptions(self):
        self.layout.addWidget(QLabel("Alphabet:"), 1, 0)
        self.alphabet = QLineEdit()
        self.alphabet.insert(string.ascii_lowercase)
        self.layout.addWidget(self.alphabet, 1, 1)

        self.layout.addWidget(QLabel("Shift:"), 1, 2)
        self.shift = QLineEdit()
        self.shift.setValidator(QIntValidator())
        self.shift.insert("7")
        self.layout.addWidget(self.shift, 1, 3)

        self.maintainCase = QCheckBox(text="Maintain Case")
        self.layout.addWidget(self.maintainCase, 2, 0)
        self.maintainForeignChar = QCheckBox(text="Maintain Foreign Char")
        self.layout.addWidget(self.maintainForeignChar, 2, 1)
        self.shiftNumbers = QCheckBox(text="Shift Numbers")
        self.layout.addWidget(self.shiftNumbers, 2, 2)



        self.clearButton = QPushButton("Clear")
        self.layout.addWidget(self.clearButton, 3, 2)
        self.goButton = QPushButton("Go")
        self.layout.addWidget(self.goButton, 3, 3)
    
    def _createOutputBox(self):
        self.outputBox = QPlainTextEdit()
        self.outputBox.setReadOnly(True)
        self.outputBox.setPlaceholderText("Output")
        self.layout.addWidget(self.outputBox, 4, 0, 1, 4)

    ########################################
    def clearDisplay(self):
        self.inputBox.clear()
        self.outputBox.clear()

    def displayOutput(self, textList):
        toDisplay = ''
        for item in textList:
            toDisplay = toDisplay + str(item) + ''

        self.outputBox.setPlainText(toDisplay)

    def caesarCipher(self):
        inputString = self.inputBox.toPlainText()
        alphabet = self.alphabet.text()
        shift = self.shift.text()
        maintainCase = self.maintainCase.isChecked()
        maintainForeignChar = self.maintainForeignChar.isChecked()
        shiftNumbers = self.shiftNumbers.isChecked()

        result = caesarCipherMain(inputString, alphabet, shift, maintainCase, maintainForeignChar, shiftNumbers)
        self.displayOutput(result)