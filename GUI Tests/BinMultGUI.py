import os
import sys
from PyQt6.QtWidgets import *

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, '../'))

class BinaryMultiplication(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()
    
    def initUI(self):
        layout= QVBoxLayout()

        self.title_label = QLabel("Binary Multiplication")
        layout.addWidget(self.title_label)


        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.show_menu_page)
        layout.addWidget(self.back_button)

        self.setLayout(layout)
    
    def show_menu_page(self):
         self.stacked_widget.setCurrentIndex(0)