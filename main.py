import sys
import theme
import CreatWidget
import customTimePicker
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QHBoxLayout, QVBoxLayout, QDateEdit, 
    QFrame, QDialog, QFileDialog,
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1920, 1080)
        self.setWindowTitle("Тест")
        self.showMaximized()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        self.current_theme = "dark"  # стартовая тема
        self.apply_theme(self.current_theme)



    def toggle_theme(self):
        if self.current_theme == "dark":
            self.current_theme = "light"
        else:
            self.current_theme = "dark"
        self.apply_theme(self.current_theme)

    def apply_theme(self, theme_name):
        if theme_name == "dark":
            self.setStyleSheet(theme.DARK_THEME)
        else:
            self.setStyleSheet(theme.LIGHT_THEME)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
