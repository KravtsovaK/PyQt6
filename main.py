import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from random import randint

class GuessNumberGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Угадай число")
        self.setGeometry(300, 300, 350, 200)

        self.label = QLabel(self)
        self.label.setText("Введите число от 1 до 100:")
        self.label.setGeometry(20, 20, 200, 30)

        self.input_field = QLineEdit(self)
        self.input_field.move(190, 20)

        self.button = QPushButton("Проверить", self)
        self.button.move(100, 70)
        self.button.clicked.connect(self.check_number)

        self.result_label = QLabel(self)
        self.result_label.move(80, 120)

        self.attempts_label = QLabel(self)
        self.attempts_label.move(20, 150)
        self.remaining_attempts = 5
        self.update_attempts_label()

        self.generated_number = randint(1,100)

    def check_number(self):
        number = int(self.input_field.text())
        self.input_field.clear()
        if number == self.generated_number:
            self.result_label.setText("Вы угадали число!<3")
            self.result_label.adjustSize()
            self.button.setEnabled(False)
        elif number < self.generated_number:
            self.result_label.setText("Загаданное число больше.")
            self.result_label.adjustSize()
            self.remaining_attempts -= 1
            self.update_attempts_label()
            if self.remaining_attempts == 0:
                self.result_label.setText(f"Вы проиграли. Загаданное число: {self.generated_number}")
                self.result_label.adjustSize()
                self.button.setEnabled(False)
        else:
            self.result_label.setText("Загаданное число меньше.")
            self.result_label.adjustSize()
            self.remaining_attempts -= 1
            self.update_attempts_label()
            if self.remaining_attempts == 0:
                self.result_label.setText(f"Вы проиграли. Загаданное число: {self.generated_number}")
                self.result_label.adjustSize()
                self.button.setEnabled(False)

    def update_attempts_label(self):
        self.attempts_label.setText(f"Осталось попыток: {self.remaining_attempts}")
        self.attempts_label.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = GuessNumberGame()
    game.show()
    sys.exit(app.exec())