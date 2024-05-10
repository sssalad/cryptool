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

    def displayOutput(self, textList):
        toDisplay = ''
        for item in textList:
            toDisplay = toDisplay + str(item) + ''

        self.outputBox.setPlainText(toDisplay)

    def rsaGo(self):
        inputKey = self.inputKeyBox.toPlainText()
        #keyModulus = getNFromASN1(inputKey)
        #self.modulus.setText(str(keyModulus))
        rsaNumbers = getNumbersFromPEMRSAKey(inputKey)
        for num in rsaNumbers:
            print(str(num) + ": " + str(rsaNumbers[num]))