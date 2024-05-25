from PyQt6.QtWidgets import *
from encryptors.encryptors import XORMain

class XORWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        
        # Create stuff
        self._createInputBox()
        self._createOptions()
        self._createOutputBox()

        # Connect slots
        self.clearButton.clicked.connect(self.clearDisplay)
        self.goButton.clicked.connect(self.xor)

        self.setLayout(self.layout)

    def _createInputBox(self):
        self.inputBox = QPlainTextEdit()
        self.inputBox.setPlaceholderText("Input")
        self.layout.addWidget(self.inputBox, 0, 0, 1, 4)

    def _createOptions(self):
        types = ["Binary", "Decimal", "Hexidecimal", "Base64", "Text"]
        self.inputType = QComboBox()
        self.outputType = QComboBox()
        self.inputType.addItems(types)
        self.outputType.addItems(types)
        self.layout.addWidget(QLabel("From:"), 1, 0)
        self.layout.addWidget(self.inputType, 1, 1)
        self.layout.addWidget(QLabel("To:"), 1, 2)
        self.layout.addWidget(self.outputType, 1, 3)

        self.layout.addWidget(QLabel("Key Type:"), 2, 0)
        self.keyType = QComboBox()
        self.keyType.addItems(types)
        self.layout.addWidget(self.keyType, 2, 1)

        self.layout.addWidget(QLabel("Key:"), 2, 2)
        self.key = QLineEdit()
        self.layout.addWidget(self.key, 2, 3)

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

    def xor(self):
        inputString = self.inputBox.toPlainText()
        inputType = self.inputType.currentText()
        outputType = self.outputType.currentText()
        key = self.key.text()
        keyType = self.keyType.currentText()

        result = XORMain(inputString, inputType, outputType, key, keyType)
        self.displayOutput(result)