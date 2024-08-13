from .DatabaseManager import DatabaseManager
from .Register import Register
from PyQt6.QtWidgets import QApplication


class HandlerButton:
    def __init__(self):
        self.database_manager = DatabaseManager()


    def add_button_handler(self, signal):
        self.register_window = Register()
        self.register_window.show()