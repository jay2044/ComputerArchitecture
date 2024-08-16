import sys
from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QGridLayout, QLineEdit, QPushButton


class MultiplicationForm(QWidget):
    def __init__(self, array):
        super().__init__()
        self.layout = QGridLayout()

        self.expected_list = array

        self.edit_boxes = []
        number_of_columns = 3
        for index, word in enumerate(self.expected_list):
            if word == "final" or word == "product":
                continue
            row = index // number_of_columns
            col = index % number_of_columns
            edit_box = QLineEdit()
            self.edit_boxes.append(edit_box)
            self.layout.addWidget(edit_box, row, col)
            

        submit_button_row = (len(self.expected_list) + number_of_columns - 1) // number_of_columns
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.check_edit_boxes)
        self.layout.addWidget(self.submit_button, submit_button_row, 0, 1, number_of_columns)

        self.submissions = 0

        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label, submit_button_row + 1, 0, 1, number_of_columns)

        self.attempts_label = QLabel(f"Tries remaining {self.submissions}/3")
        self.layout.addWidget(self.attempts_label, submit_button_row + 1, 2, 1, number_of_columns)

        self.setLayout(self.layout)

    def check_edit_boxes(self):
        correct = all(
    edit_box.text() == word 
    for edit_box, word in zip(self.edit_boxes, self.expected_list) 
    if word not in {"final", "product"}
)   
        self.submissions += 1
        
        self.attempts_label.setText(f"Tries remaining {self.submissions}/3")

        if correct:
            self.result_label.setText("Correct")
        else:
            if self.submissions == 3:
                self.submit_button.setVisible(False)
                self.result_label.setText("Incorrect. No more tries remaining.")
            else:
                self.result_label.setText("Incorrect. Please try again.")
        
        
        
    def updateResults(self, results):
        self.expected_list = results
        
        for i in range(0, 6):
            for j in range(0, 3):
                if(self.layout.itemAtPosition(i, j) != None):
                    self.layout.itemAtPosition(i, j).widget().setText("")
    
    def updateSubmissions(self):
        self.submissions = 0
        self.submit_button.setVisible(True)
        self.result_label.setText("")
        self.attempts_label.setText(f"Tries remaining {self.submissions}/3")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = MultiplicationForm()
    form.show()

    app.exec()