from PyQt6.QtWidgets import *
from rsa.rsaHelpers import *

class WienerWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        
        self._createInputBoxes()
        self._createOutputBox()

        # Connect slots
        self.clearButton.clicked.connect(self.clearDisplay)
        self.goButton.clicked.connect(self.wienerAttackGo)

        self.setLayout(self.layout)

    def _createInputBoxes(self):
        self.layout.addWidget(QLabel("n:"), 0, 0)
        self.modulus = QLineEdit()
        self.layout.addWidget(self.modulus, 0, 1)

        self.layout.addWidget(QLabel("e:"), 1, 0)
        self.e = QLineEdit()
        self.layout.addWidget(self.e, 1, 1)

        self.layout.addWidget(QLabel("[Optional] c:"), 2, 0)
        self.cipherText = QLineEdit()
        self.layout.addWidget(self.cipherText, 2, 1)

        self.clearButton = QPushButton("Clear")
        self.layout.addWidget(self.clearButton, 3, 0)
        self.goButton = QPushButton("Go")
        self.layout.addWidget(self.goButton, 3, 1)

    
    def _createOutputBox(self):
        self.layout.addWidget(QLabel("d:"), 4, 0)
        self.d = QLineEdit()
        self.layout.addWidget(self.d, 4, 1)

        self.layout.addWidget(QLabel("[Optional] m:"), 2, 0)
        self.plainText = QLineEdit()
        self.layout.addWidget(self.plainText, 2, 1)

    ########################################
    def clearDisplay(self):
        self.modulus.clear()
        self.e.clear()
        self.cipherText.clear()

    def displayOutput(self, d, m=None):
        self.d.setText(d)
        if m:
            self.plainText.setText(m)

    def wienerAttackGo(self):
        n = self.modulus.text()
        e = self.e.text()
        d = WienerAttack(int(n), int(e))
        self.displayOutput(str(d))