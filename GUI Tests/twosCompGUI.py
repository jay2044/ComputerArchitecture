import os
import sys
from PyQt6.QtWidgets import *

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, '../'))
from binaryArith.binaryArith import *


class TwosCompApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.binary_label = QLabel("Binary Number:")
        self.binary_input = QLineEdit()
        layout.addWidget(self.binary_label)
        layout.addWidget(self.binary_input)

        self.size_label = QLabel("Size:")
        self.size_input = QLineEdit()
        layout.addWidget(self.size_label)
        layout.addWidget(self.size_input)

        self.result_label = QLabel("Two's Complement:")
        self.result_display = QLabel("")
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_display)

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button)

        self.setLayout(layout)
        self.setWindowTitle("Two's Complement Tester")

    def calculate(self):
        binary_str = self.binary_input.text()
        size_str = self.size_input.text()

        if not binary_str or not size_str:
            QMessageBox.warning(self, "Input Error", "Please enter both the binary number and the size.")
            return

        try:
            size = int(size_str)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Size must be an integer.")
            return

        if len(binary_str) != size:
            QMessageBox.warning(self, "Input Error", "The length of the binary number must match the size.")
            return

        result = twosComp(binary_str, size)
        self.result_display.setText(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TwosCompApp()
    ex.show()
    sys.exit(app.exec())
