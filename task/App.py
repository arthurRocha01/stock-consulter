import json
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
  QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
  QTableWidget, QTableWidgetItem, QPushButton
)
from .Customize import StockFrameCustomizer
from .SignalManager import SignalManager
from .Utilities import Utilities


class StockConsulter(QWidget):
  def __init__(self, headers):
    super().__init__()
    self.__initialize_handlers()
    self.__initialize_ui(headers)


  def __initialize_handlers(self):
    """ Inicializa os handlers. """
    self.handler_signal = SignalManager()
    self.utilities = Utilities()


  def __initialize_ui(self, headers):
    """ Cria a interface gráfica. """
    self.__create_window()
    self.__create_layout()
    self.__build_features()
    self.__create_result_table(headers)
    self.__initialize_result_table()


  def __create_window(self):
    """ Cria a janela principal. """
    self.setWindowTitle('Search App')
    self.resize(800, 600)
    self.setMinimumSize(600, 400)


  def __create_layout(self):
    """ Cria o layout principal. """
    self.main_layout = QVBoxLayout()
    self.setLayout(self.main_layout)


  def __create_search_bar(self):
    """ Cria a barra de pesquisa. """
    self.search_bar = QLineEdit()
    self.search_bar.setPlaceholderText('Pesquise aqui...')
    self.search_bar.setFixedWidth(400)
    self.search_bar.textChanged.connect(self.perform_search)
    self.features_layout.addWidget(self.search_bar)


  def __create_button_add(self):
    self.button_add = QPushButton('Adcionar +')
    self.button_add.setFixedSize(100, 30)
    self.button_add.clicked.connect(lambda: self.__button_clicked_handler(True))
    self.features_layout.addWidget(self.button_add, )


  def __build_features(self):
    self.features_layout = QHBoxLayout()
    self.main_layout.addLayout(self.features_layout)
    self.__create_search_bar()
    self.__create_button_add()


  def __create_font_settings(self):
    """ Configura as fontes dos textos. """
    self.font_name = QFont('Arial', 13)
    self.font_price = QFont('Arial', 13, weight=QFont.Weight.Bold)
    self.font_cost_price = QFont('Arial', 13, italic=True)
    self.font_margin = QFont('Arial', 13, italic=True)
    self.font_marca = QFont('Arial', 13)


  def __customize_result_table(self):
    """ Customização do quadro de estoque. """
    customize = StockFrameCustomizer(self.table_result)
    customize.set_behavior()
    customize.set_maximum_column_size([110, 110,  110, 200])
    customize.set_default_settings()
    self.__create_font_settings()


  def __create_result_table(self, headers):
    """ Cria o quadro de estoque. """
    self.table_result = QTableWidget()
    self.table_result.setColumnCount(len(headers))
    self.table_result.setHorizontalHeaderLabels(headers)
    self.table_result.itemChanged.connect(self.__handle_cell_changed)
    self.main_layout.addWidget(self.table_result)
    self.__customize_result_table()


  def __load_data(self):
    """ Carregar os dados do arquivo JSON. """
    with open('resources/database.json', 'r') as file:
      self.data = json.load(file)


  def __initialize_result_table(self):
    """ Inicializar o quadro de estoque com os dados carregados. """
    self.__load_data()
    sorted_products = {k: v for k, v in sorted(self.data.items(), key=lambda item: item[0])}
    self.update_table(sorted_products)


  def __handle_cell_changed(self, item):
    """ Tratamento para quando uma célula é alterada. """
    self.handler_signal.cell_signal_handler(self.table_result, item)


  def __button_clicked_handler(self, signal):
    self.handler_signal.button_clicked_handler(signal)


  def perform_search(self):
    """ Realizar a pesquisa e atualizar o quadro de estoque. """
    search_text = self.search_bar.text().lower()
    filtered_products = {
      name: details for name, details in self.data.items()
      if search_text in name.lower()
    }
    self.update_table(filtered_products)


  def update_table(self, products):
    """ Atualizar o quadro de estoque com os dados filtrados. """
    self.table_result.blockSignals(True)
    self.table_result.setRowCount(len(products))
    for row, (name, details) in enumerate(products.items()):
      self.__populate_row(row, name, details)
    self.table_result.blockSignals(False)


  def __populate_row(self, row, name, details):
    """ Preencher uma linha do quadro de estoque. """
    name = name
    price = self.utilities.calculate_price(
      details['price'], details['margin']
    )
    cost = details['price']
    margin = self.utilities.customize_margin(details['margin'])
    fabricator = details['fabricator']
    # Nome
    self.__add_table_item(row, 0, name, self.font_name)
    # Preço
    self.__add_table_item(row, 1, price, self.font_price)
    # Custo
    self.__add_table_item(row, 2, cost, self.font_cost_price)
    # Margem
    self.__add_table_item(row, 3, margin, self.font_margin, True)
    # Marca
    self.__add_table_item(row, 4, fabricator, self.font_marca)


  def __add_table_item(self, row, column, value, font_key, editable=False):
    """ Adicionar um item à célula do quadro de estoque. """
    item = QTableWidgetItem(value)
    if column != 0:
      item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
    if not editable:
      item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
    item.setFont(font_key)
    self.table_result.setItem(row, column, item)