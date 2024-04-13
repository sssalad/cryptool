from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from encodeMain import encodeMain

class encodeWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        
        # Create stuff
        self._createInputBox()
        self._createOptions()
        self._createOutputBox()

        # Connect slots
        self.clearButton.clicked.connect(self.clearDisplay)
        self.goButton.clicked.connect(self.encode)

        self.setLayout(self.layout)

    def _createInputBox(self):
        self.inputBox = QPlainTextEdit()
        self.inputBox.setPlaceholderText("Input")
        self.layout.addWidget(self.inputBox, 0, 0, 1, 4)

    def _createOptions(self):
        converting = ["Binary", "Decimal", "Hexidecimal", "Base64", "Text"]
        self.convertOptionsFrom = QComboBox()
        self.convertOptionsTo = QComboBox()
        self.convertOptionsFrom.addItems(converting)
        self.convertOptionsTo.addItems(converting)
        self.layout.addWidget(QLabel("From:"), 1, 0)
        self.layout.addWidget(self.convertOptionsFrom, 1, 1)
        self.layout.addWidget(QLabel("To:"), 1, 2)
        self.layout.addWidget(self.convertOptionsTo, 1, 3)

        self.byByteCheck = QCheckBox("By Byte")
        self.layout.addWidget(self.byByteCheck, 2, 1)
        self.clearButton = QPushButton("Clear")
        self.layout.addWidget(self.clearButton, 2, 2)
        self.goButton = QPushButton("Go")
        self.layout.addWidget(self.goButton, 2, 3) 
    
    def _createOutputBox(self):
        self.outputBox = QPlainTextEdit()
        self.outputBox.setReadOnly(True)
        self.outputBox.setPlaceholderText("Output")
        self.layout.addWidget(self.outputBox, 3, 0, 1, 4)

    ########################################
    def clearDisplay(self):
        self.inputBox.clear()
        self.outputBox.clear()

    def displayOutput(self, textList):
        toDisplay = ''
        for item in textList:
            toDisplay = toDisplay + str(item) + ''

        self.outputBox.setPlainText(toDisplay)

    def encode(self):
        inputString = self.inputBox.toPlainText()
        convertFrom = self.convertOptionsFrom.currentText()
        convertTo = self.convertOptionsTo.currentText()
        byBytes = self.byByteCheck.isChecked()

        result = encodeMain(inputString, convertFrom, convertTo, byBytes)
        self.displayOutput(result)
