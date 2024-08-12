from .DatabaseManager import DatabaseManager
from .Register import Register
from PyQt6.QtWidgets import QApplication


class HandlerButton:
    def __init__(self):
        self.database_manager = DatabaseManager()
        self.register_window = None


    def add_button_handler(self, signal):
        if self.register_window is None:
            self.register_window = Register()
            self.register_window.show()