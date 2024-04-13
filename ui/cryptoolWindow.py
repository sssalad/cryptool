import os
import json
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from ui.encodeWidget import encodeWidget

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
        inputFile = open(os.getcwd() + '\\ui\\ui.json') # use cwd at some point in the future 
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
        parent = item.parent()
        #parentName = parent.text(0)
        itemName = item.text(0)

        if (itemName == 'Encode'):# or parentName == 'Encode'):
            encode = encodeWidget()
            self.generalLayout.addWidget(encode, 0, 1, 4, 3)
