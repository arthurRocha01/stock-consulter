from PyQt6.QtWidgets import QHeaderView
from PyQt6.QtGui import QFont

class StockFrameCustomizer():
  def __init__(self, result_table):
    self.result_table = result_table
    self.header = result_table.horizontalHeader()


  def set_behavior(self):
    for col in range(len(self.header)):
      self.header.setSectionResizeMode(col, QHeaderView.ResizeMode.Stretch)


  def set_maximum_column_size(self, settings):
    for index, size in enumerate(settings, start=1):
      self.header.setSectionResizeMode(index, QHeaderView.ResizeMode.Interactive)
      self.header.resizeSection(index, size)


  def set_default_settings(self):
    self.result_table.setStyleSheet('''
            QTableWidget::item {
                border-bottom: 1px solid #dcdcdc; /* Cor da borda inferior das linhas */
                border-right: 1px solid #dcdcdc; /* Cor da borda direita das colunas */
                padding: 5px; /* Espaçamento interno dos itens */
            }
        ''')
    self.header.setStyleSheet('font-size: 20px; font-weight: bold;')
    #self.result_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)


class RegisterCustomize():
    def set_size_element(self, element, width, height):
      element.setFixedWidth(width)
      element.setFixedHeight(height)
