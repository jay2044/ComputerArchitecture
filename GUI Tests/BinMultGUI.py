import os
import sys
import numpy as np
from PyQt6.QtWidgets import *

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, '../'))
from MultiplicationTest import *
from binaryArith.binaryArith import *

class BinaryMultiplication(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        
        layout= QVBoxLayout()

        # Create a horizontal layout for the back button
        top_layout = QHBoxLayout()
        
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.show_menu_page)
        top_layout.addWidget(self.back_button)
        
        # Align the button to the left
        top_layout.addStretch(1)
        
        # Add the top layout to the main layout
        layout.addLayout(top_layout)

        self.title_label = QLabel("Binary Multiplication")
        layout.addWidget(self.title_label)

        self.multd = generateRandomBinary(4)
        self.multr = generateRandomBinary(4)

        self.instructions_label = QLabel(f"Multiply these two numbers together: {self.multd} and {self.multr}")
        layout.addWidget(self.instructions_label)

        gridLayout = QGridLayout()

        self.multiplicand_label = QLabel("Multiplicand")
        gridLayout.addWidget(self.multiplicand_label, 0, 0)

        self.multiplier_label = QLabel("Multiplier")
        gridLayout.addWidget(self.multiplier_label, 0, 1)
        
        self.result_label = QLabel("Result")
        gridLayout.addWidget(self.result_label, 0, 2)
        
        result = np.array(multAlg(self.multd, self.multr, False))
        result = result.flatten()
        
        layout.addLayout(gridLayout)

        self.answerGrid = MultiplicationForm(result)

        layout.addWidget(self.answerGrid)

        # self.back_button = QPushButton("Back")
        # self.back_button.clicked.connect(self.show_menu_page)
        # layout.addWidget(self.back_button)

        self.setLayout(layout)
            
    def update(self):
        #change the numbers everytime the page is reloaded
        self.multd = generateRandomBinary(4)
        self.multr = generateRandomBinary(4)

        #updating the value of the text
        self.layout().itemAt(2).widget().setText(f"Multiply these two numbers together: {self.multd} and {self.multr}")

        #rerun the algorithm
        result = np.array(multAlg(self.multd, self.multr, False))
        result = result.flatten()

        #pass those values to the answerGrid
        self.layout().itemAt(4).widget().updateResults(result)
        self.layout().itemAt(4).widget().updateSubmissions()

 
    def show_menu_page(self):
         self.stacked_widget.setCurrentIndex(0)

        