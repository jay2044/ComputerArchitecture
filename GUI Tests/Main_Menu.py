import os
import sys
from PyQt6.QtWidgets import *
from BinMultGUI import *
from BinDivGUI import *
from MipsToMachGUI import *
from MachToMipsGUI import *

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, '../'))


class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

         # Create a QStackedWidget
        self.stacked_widget = QStackedWidget()

        # Create instances of the pages you want to navigate to
        self.main_menu_page = ButtonContainer(self.stacked_widget)
        self.binary_multiplication_page = BinaryMultiplication(self.stacked_widget)
        self.binary_division_page = BinaryDivision(self.stacked_widget)
        self.mips_to_machine_page = MipsToMachine(self.stacked_widget)
        self.machine_to_mips_page = MachineToMips(self.stacked_widget)


        # Add pages to the stacked widget
        self.stacked_widget.addWidget(self.main_menu_page)
        self.stacked_widget.addWidget(self.binary_multiplication_page)
        self.stacked_widget.addWidget(self.binary_division_page)
        self.stacked_widget.addWidget(self.mips_to_machine_page)
        self.stacked_widget.addWidget(self.machine_to_mips_page)



        layout.addWidget(self.stacked_widget)

        self.setLayout(layout)
        self.setWindowTitle("230 Gamified")

class ButtonContainer(QGroupBox):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        self.binary_mult_button = QPushButton("Binary Multiplication")
        self.binary_mult_button.clicked.connect(self.show_binary_mult_page)
        layout.addWidget(self.binary_mult_button)

        self.binary_div_button = QPushButton("Binary Division")
        layout.addWidget(self.binary_div_button)
        self.binary_div_button.clicked.connect(self.show_binary_div_page)

        self.mips_to_machine_button = QPushButton("Mips to Machine")
        layout.addWidget(self.mips_to_machine_button)
        self.mips_to_machine_button.clicked.connect(self.show_mips_to_machine_page)

        self.machine_to_mips_button = QPushButton("Machine To Mips")
        layout.addWidget(self.machine_to_mips_button)
        self.machine_to_mips_button.clicked.connect(self.show_machine_to_mips_page)
        
        self.setLayout(layout)

    def show_binary_mult_page(self):
        self.stacked_widget.setCurrentIndex(1)
    
    def show_binary_div_page(self):
        self.stacked_widget.setCurrentIndex(2)

    def show_machine_to_mips_page(self):
        self.stacked_widget.setCurrentIndex(3)

    def show_mips_to_machine_page(self):
        self.stacked_widget.setCurrentIndex(4)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainMenu()
    ex.show()
    sys.exit(app.exec())