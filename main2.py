import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

import random

class DiceRollWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dice Roll")
        self.layout = QVBoxLayout()

        self.count_dice_label = QLabel("Введите количество костей:")
        self.count_dice_input = QLineEdit()
        self.layout.addWidget(self.count_dice_label)
        self.layout.addWidget(self.count_dice_input)

        self.count_attempts_label = QLabel("Введите количество бросков:")
        self.count_attempts_input = QLineEdit()
        self.layout.addWidget(self.count_attempts_label)
        self.layout.addWidget(self.count_attempts_input)

        self.roll_button = QPushButton("Бросить кости")
        self.layout.addWidget(self.roll_button)

        self.result_label = QLabel("Результаты:")
        self.layout.addWidget(self.result_label)

        self.roll_button.clicked.connect(self.roll_dice)

        self.setLayout(self.layout)

    def roll_dice(self):
        count_dice = int(self.count_dice_input.text())
        count_attempts = int(self.count_attempts_input.text())

        results = self._roll_dice(count_attempts, count_dice)
        probabilities = self._calculate_probabilities(results)
        sorted_probabilities = dict(sorted(probabilities.items()))

        result_text = ""
        for result, probability in sorted_probabilities.items():
            result_text += f'количество очков: {result} | вероятность: {probability}%\n'

        self.result_label.setText(result_text)

    def _roll_dice(self, count_attempts, count_dice):
        result = []
        for a in range(count_attempts):
            dice_sum = 0
            for a in range(count_dice):
                dice_sum += random.randint(1,6)
            result.append(dice_sum)
        return result

    def _calculate_probabilities(self, results):
        total = len(results)
        probabilities = {}
        for result in results:
            if result in probabilities:
                probabilities[result] += 1
            else:
                probabilities[result] = 1
        for key in probabilities:
            probabilities[key] = (probabilities[key] / total) * 100
        return probabilities

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = DiceRollWidget()
    widget.show()
    sys.exit(app.exec())