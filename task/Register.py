from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
  QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
  QLabel, QPushButton
)


class Register(QWidget):
  def __init__(self):
    super().__init__()
    self.__create_window()
    self.__create_layout()
    self.__create_fields()
    self.__create_button_save()


  def __create_window(self):
    self.setWindowTitle('Register App')
    self.resize(450, 400)
    self.setMinimumSize(450, 400)


  def __create_layout(self):
    self.main_layout = QVBoxLayout()
    self.setLayout(self.main_layout)


  def __set_Font(self, obj, size):
    font = QFont('Arial', size, weight=QFont.Weight.Bold)
    obj.setFont(font)


  def __create_field(self, field):
    layout = QHBoxLayout()
    label = QLabel(field, self)
    self.__set_Font(label, 20)
    input = QLineEdit(self)
    input.setFixedWidth(200)
    layout.addWidget(label)
    layout.addWidget(input)
    self.main_layout.addLayout(layout)


  def __create_fields(self):
    fields = ['Nome', 'Fabricador', 'Preço', 'Margem',
    'CST', 'NCM', 'Aliquot']
    for field in fields:
      self.__create_field(field)


  def __create_button_save(self):
    layout = QHBoxLayout()
    self.button_save = QPushButton('Salvar')
    self.button_save.setFixedWidth(100)
    layout.addStretch()
    layout.addWidget(self.button_save, alignment=Qt.AlignmentFlag.AlignRight)
    self.main_layout.addLayout(layout)