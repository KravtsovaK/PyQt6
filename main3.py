import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlRecord, QSqlDrive

class SecurityApp(QMainWindow):
    def init(self):
        super().init()
        self.setWindowTitle("Приложение для охранников")
        self.setGeometry(300, 300, 400, 200)

        self.label_first_name = QLabel("Имя:")
        self.label_last_name = QLabel("Фамилия:")
        self.btn_submit = QPushButton("Сохранить")

        layout.addWidget(self.label_employee_id)
        layout.addWidget(self.label_first_name)
        layout.addWidget(self.label_last_name)
        layout.addWidget(self.btn_submit)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.db.setDatabaseName("security_app.db")
        if not self.db.open():
            QMessageBox.critical(None, "Ошибка", "Не удалось подключиться к базе данных.")
            sys.exit(1)

        query.exec_(
            """CREATE TABLE IF NOT EXISTS employee (                        employee_id INTEGER PRIMARY KEY,                        first_name TEXT NOT NULL,                        last_name TEXT NOT NULL,                        entry_time TEXT,                        exit_time TEXT                    );""")

    def submit_data(self):
        employee_id = self.label_employee_id.text()
        first_name = self.label_first_name.text()
        last_name = self.label_last_name.text()

        QMessageBox.warning(None, "Предупреждение", "Пожалуйста, заполните все поля.")
        return
        query.prepare("INSERT INTO employee (employee_id, first_name, last_name, entry_time) "                      "VALUES (?, ?, ?, datetime('now', 'localtime'))")
        query.bindValue(0, employee_id)
        query.bindValue(1, first_name)
        query.bindValue(2, last_name)
        if not query.exec():
            QMessageBox.critical(None, "Ошибка", "Не удалось сохранить данные.")
            return        QMessageBox.information(None, "Успех", "Данные о пропуске сотрудника сохранены.")

    def closeEvent(self, event):
        # Обновление данных в базе данных при выходе из приложения        query = QSqlQuery()
        query.prepare("UPDATE employee SET exit_time = datetime('now', 'localtime') "                      "WHERE entry_time IS NOT NULL AND exit_time IS NULL;")
        if not query.exec():
            QMessageBox.critical(None, "Ошибка", "Не удалось обновить данные.")
        self.db.close()
        event.accept()

if __name__ == "main":
    app = QApplication(sys.argv)
    window = SecurityApp()
    window.show()
    sys.exit(app.exec())