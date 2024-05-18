import os
import platform
import json
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from ui import encodeWidget, XORWidget, caesarCipherWidget, rsaWidget, WienerWidget

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 750

class cryptoolWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("cryptool")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        
        self.generalLayout = QGridLayout()
        
        # Create stuff
        self._createOptionsTree()

        # Connect slots
        self.optionsTree.itemActivated.connect(self.initializeItem)

        self.centralWidget = QWidget(self)
        self.centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(self.centralWidget)

    
    def _createOptionsTree(self):
        if (platform.system() == 'Windows'):
            UI_OPTIONS_TREE_JSON = (os.getcwd() + '\\ui\\ui.json')
        elif (platform.system() == 'Linux'):
            UI_OPTIONS_TREE_JSON = (os.getcwd() + '/ui/ui.json')

        inputFile = open(UI_OPTIONS_TREE_JSON)
        data = json.load(inputFile)
    
        self.optionsTree = QTreeWidget()
        self.optionsTree.setHeaderLabels(["Cryptool"])

        items = []
        for key, values in data.items():
            item = QTreeWidgetItem([key])
            for value in values:
                child = QTreeWidgetItem([value])
                item.addChild(child)
            items.append(item)

        self.optionsTree.insertTopLevelItems(0, items)
        self.generalLayout.addWidget(self.optionsTree, 0, 0, alignment=Qt.AlignmentFlag.AlignLeft)

    def initializeItem(self, item):
        try:
            parent = item.parent()
            parentName = parent.text(0)
        except:
            parentName = "NULL"
        itemName = item.text(0)
        # Clear the layout before we add something else
        if (self.generalLayout.itemAtPosition(0, 1) != None):
            self.generalLayout.itemAtPosition(0, 1).widget().deleteLater()

        if (itemName == 'Encode'):# or parentName == 'Encode'):
            encode = encodeWidget.encodeWidget()
            self.generalLayout.addWidget(encode, 0, 1, 4, 3)
        elif (itemName == 'Caesar Cipher'):
            caesars = caesarCipherWidget.caesarCipherWidget()
            self.generalLayout.addWidget(caesars, 0, 1, 4, 3)
        elif (itemName == 'XOR'):
            xor = XORWidget.XORWidget()
            self.generalLayout.addWidget(xor, 0, 1, 4, 3)
        elif (parentName == 'RSA' and itemName == 'Encrypt'):
            rsaEncrypt = rsaWidget.rsaWidget()
            self.generalLayout.addWidget(rsaEncrypt, 0, 1, 4, 3)
        elif (itemName == 'Wieners'):
            wiener = WienerWidget.WienerWidget()
            self.generalLayout.addWidget(wiener, 0, 1, 4, 3)
