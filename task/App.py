import json
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
  QWidget, QVBoxLayout, QLineEdit,
  QTableWidget, QTableWidgetItem, QHeaderView
)
from .Customize import StockFrameCustomizer


class StockConsulter(QWidget):
  def __init__(self):
    super().__init__()
    self.__create_window()
    self.__create_layout()
    self.__create_search_bar()
    self.__create_result_table()
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
    self.main_layout.addWidget(self.search_bar)


  def __customize_result_table(self):
    """ Customização do quadro de estoque. """
    customize = StockFrameCustomizer(self.table_result)

    customize.set_behavior()
    customize.set_maximum_column_size([110, 110, 200])
    customize.set_default_settings()

    # Definir fontes para cada coluna
    self.font_name = QFont('Arial', 13)
    self.font_price = QFont('Arial', 13, weight=QFont.Weight.Bold)
    self.font_margin = QFont('Arial', 13, italic=True)
    self.font_marca = QFont('Arial', 13)


  def __create_result_table(self):
    """ Cria o quadro de estoque. """
    self.table_result = QTableWidget()
    self.table_result.setColumnCount(4)
    self.table_result.setHorizontalHeaderLabels(['Name', 'Price', 'Margin', 'Marca'])
    # self.table_result.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
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
    self.table_result.setRowCount(len(products))
    for row, (name, details) in enumerate(products.items()):
      # Name
      name_item = QTableWidgetItem(name)
      name_item.setFlags(name_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
      name_item.setFont(self.font_name)
      self.table_result.setItem(row, 0, name_item)
      # Price
      price_item = QTableWidgetItem((str(details['price'])))
      price_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
      price_item.setFlags(price_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
      price_item.setFont(self.font_price)
      self.table_result.setItem(row, 1, price_item)
      # Margin
      margin_item = QTableWidgetItem( str(f'{details["margin"]}%') )
      margin_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
      margin_item.setFlags(margin_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
      margin_item.setFont(self.font_margin)
      self.table_result.setItem(row, 2, margin_item)
      # Fabricator
      marca_item = QTableWidgetItem(str(details['fabricator']))
      marca_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
      marca_item.setFlags(marca_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
      marca_item.setFont(self.font_marca)
      self.table_result.setItem(row, 3, marca_item)