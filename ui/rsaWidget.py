from PyQt6.QtWidgets import *
from rsa.rsaHelpers import *

class rsaWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        
        # Create stuff
        self._createInputBoxes()
        self._createOptions()
        self._createOutputBox()

        # Connect slots
        self.clearButton.clicked.connect(self.clearDisplay)
        self.goButton.clicked.connect(self.rsaGo)
        self.inputKeyBox.textChanged.connect(self.getRSANumbers)

        self.setLayout(self.layout)

    def _createInputBoxes(self):
        self.inputMessageBox = QPlainTextEdit()
        self.inputMessageBox.setPlaceholderText("Text to encrypt/decrypt")
        self.layout.addWidget(self.inputMessageBox, 0, 0, 1, 2)

        self.inputKeyBox = QPlainTextEdit()
        self.inputKeyBox.setPlaceholderText("Public or private key")
        self.layout.addWidget(self.inputKeyBox, 0, 2, 1, 2)

    def _createOptions(self):
        self.layout.addWidget(QLabel("N:"), 2, 0)
        self.modulus = QLineEdit()
        self.layout.addWidget(self.modulus, 2, 1)

        self.layout.addWidget(QLabel("e:"), 2, 2)
        self.e = QLineEdit()
        self.layout.addWidget(self.e, 2, 3)

        self.layout.addWidget(QLabel("d:"), 2, 4)
        self.d = QLineEdit()
        self.layout.addWidget(self.d, 2, 5)

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
        self.inputMessageBox.clear()
        self.inputKeyBox.clear()
        self.outputBox.clear()

    def displayOutput(self, toDisplay):
        self.outputBox.setPlainText(toDisplay)

    def getRSANumbers(self):
        if self.inputKeyBox.toPlainText() != '':
            self.modulus.setText('')
            self.e.setText('')
            self.d.setText('')

            inputKey = self.inputKeyBox.toPlainText()
            rsaNumbers = getNumbersFromPEMRSAKey(inputKey)
            if rsaNumbers == 'error':
                self.modulus.setText('?')
                self.e.setText('?')
                self.d.setText('?')
            else:
                for num in rsaNumbers:
                    if num == 'n':
                        self.modulus.setText(str(rsaNumbers[num]))
                    elif num == 'e':
                        self.e.setText(str(rsaNumbers[num]))
                    elif num == 'd':
                        self.d.setText(str(rsaNumbers[num]))

    def rsaGo(self):
        message = self.inputMessageBox.toPlainText()
        key = self.inputKeyBox.toPlainText()
        result = rsaDencrypt(key, message)
        self.displayOutput(result)