import json
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
  QMainWindow, QWidget, QVBoxLayout, QHeaderView,
  QTableWidget, QTableWidgetItem, QLineEdit
)


class StockConsulter(QMainWindow):
  def __init__(self, headers):
    super().__init__()
    self.__run_initialization(headers)


  def __set_default_settings(self):
    self.setWindowTitle('Stock-Consulter')
    self.resize(800, 600)
    self.setMinimumSize(600, 400)
    self.showMaximized()


  def __create_window(self):
    """ Cria a estrutura da janela. """
    self.__set_default_settings()
    self.central_widget = QWidget()
    self.main_layout = QVBoxLayout()
    self.setCentralWidget(self.central_widget)
    self.central_widget.setStyleSheet('''
            background-color: #2d2d2d;
        ''')
    self.central_widget.setLayout(self.main_layout)


  def __create_search_bar(self):
    """ Cria a barra de pesquisa. """
    self.search_bar = QLineEdit()
    self.search_bar.setPlaceholderText('Search')
    self.search_bar.setFixedWidth(400)
    self.search_bar.textChanged.connect(self.__perform_search)
    self.search_bar.setStyleSheet('''
            QLineEdit {
                background-color: #444444;
                color: #ffffff;
                border: 2px solid #888888;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
            }
            QLineEdit:focus {
                border: 2px solid #aaaaaa;
                background-color: #555555;
            }
        ''')
    font = QFont('Arial', 11)
    self.search_bar.setFont(font)
    self.main_layout.addWidget(self.search_bar)


  def __customize_result_table(self):
    """ Configura a visualização da tabela de resultados. """
    behavior_map = {    # Mapeamento de tamanho mínimo dos headers.
      0: '',
      1: 200,
      2: 100,
      3: 150
    }
    header = self.result_table.horizontalHeader()
    for col, value in behavior_map.items():
      if col == 0:    # Header do nome de produto (ocupa todo o espaço que sobrar dos outros).
        header.setSectionResizeMode(col, QHeaderView.ResizeMode.Stretch)
      else:
        header.setSectionResizeMode(col, QHeaderView.ResizeMode.Interactive)
        header.resizeSection(col, value)
      self.result_table.setRowHeight(col, 50)
    self.result_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)    # Desabilitar edição dos items.
    self.result_table.setStyleSheet('''
            QTableWidget {
                background-color: #2d2d2d;
                color: #ffffff;
                gridline-color: #444444;
                font-size: 14px;
                alternate-background-color: #3d3d3d;
            }
            QTableWidget::item {
                padding: 10px;
                border-bottom: 1px solid #444444;
            }
            QTableWidget::item:selected {
                background-color: #555555;
            }
            QHeaderView::section {
                background-color: #444444;
                color: #ffffff;
                font-weight: bold;
                padding: 5px;
                border: 1px solid #555555;
            }
            QTableWidget::item:hover {
                background-color: #555555;
            }
        ''')
    self.result_table.horizontalHeader().setStyleSheet('''
      font-size: 20px;
      font-weight: bold;
    ''')


  def __create_result_table(self, headers):
    """ Cria a tabela de resultados. """
    num_headers = len(headers)
    self.result_table = QTableWidget()
    self.result_table.setColumnCount(num_headers)
    self.result_table.setHorizontalHeaderLabels(headers)
    self.main_layout.addWidget(self.result_table)
    self.__customize_result_table()


  def __adjust_row_heights(self):
    """ Ajusta a altura das linhas da tabela de resultados. """
    for row in range(self.result_table.rowCount()):
      self.result_table.setRowHeight(row, 35)


  def __render_items(self):
    """ Renderiza os items na tabela de resultados. """
    with open('resources/database.json', 'r', encoding='utf-8') as file:
      self.data = json.load(file)
    sorted_products = {   # Organiza os items em ordem alfabética.
      item: details for item, details in sorted(
        self.data.items(), key=lambda item: item[0]
      )
    }
    self.__update_table(sorted_products)
    self.__adjust_row_heights()


  def __set_font(self, column_name):
    """ Define a fonte do item na coluna especificada. """
    font_map = {    # Mapeamento dos tamanhos da fonte.
      'product': 16,
      'fabricator': 16,
      'price': 16,
      'margin': 16,
    }
    font = QFont('Arial', font_map[column_name])
    font.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, 0.7)
    return font


  def __update_table(self, items):
    """ Atualiza a visualização da tabela de resultados. """
    cols_map = {    # Mapeamento dos nomes dos headers.
      0: 'product',
      1: 'fabricator',
      2: 'price',
      3: 'margin'
    }
    self.result_table.setRowCount(len(items))
    for row, (name, details) in enumerate(items.items()):
      for col in range(4):
        header = cols_map[col]
        if header == 'product':
          item = QTableWidgetItem(name)
        else:
          item = QTableWidgetItem(str(details[header]))
          item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
        font = self.__set_font(header)
        item.setFont(font)
        self.result_table.setItem(row, col, item)


  def __perform_search(self):
    """ Realiza a pesquisa na tabela de resultados. """
    search_text = self.search_bar.text().lower()
    filtered_items = {
      item: details for item, details in self.data.items()
      if search_text in item.lower()
    }
    self.__update_table(filtered_items)


  def __run_initialization(self, headers):
    """ Inicializa a janela e cria os componentes. """
    self.__create_window()
    self.__create_search_bar()
    self.__create_result_table(headers)
    self.__render_items()