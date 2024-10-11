from PyQt6.QtWidgets import (
    QLineEdit, QHBoxLayout, QPushButton,
    QTableWidget
)
from .Custom.Customize import TableCustomize
from model.ProductModel import ProductModel

class Searcher():
    def __init__(self, main_layout):
        self.main_layout = main_layout
        self.headers = ['Nome', 'Preço', 'Custo', 'Margem', 'Marca']
        self.count_headers = len(self.headers)

    def _init_handlers(self):
        """ Inicializa os manipuladores. """
        self.product_model = ProductModel(self.product_table)

    def _initialize_ui(self):
        """ Inicializa as a interfaces. """
        self._build_features()
        self._create_product_table()

    def _create_search_bar(self):
        """ Cria a barra de pesquisa. """
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Pesquise")
        self.search_bar.setFixedWidth(400)
        self.search_bar.textChanged.connect(lambda: self.product_model.event_handler('searcher', self.search_bar))
        self.function_layout.addWidget(self.search_bar)

    def _create_button_add(self):
        """ Cria o botão de adicionar um novo item. """
        self.button_add = QPushButton("Adcionar +")
        self.button_add.setFixedSize(100, 30)
        self.button_add.clicked.connect(lambda: self.product_model.event_handler('add'))
        self.function_layout.addWidget(self.button_add)

    def _build_features(self):
        """ Cria os funções da janela. """
        self.function_layout = QHBoxLayout()
        self.table_layout = QHBoxLayout()
        self.main_layout.addLayout(self.function_layout)
        self.main_layout.addLayout(self.table_layout)
        self._create_search_bar()
        self._create_button_add()

    def _customize_product_table(self):
        """ Customiza o estilo e comportamento da tabela. """
        customize = TableCustomize(self.product_table)
        customize.set_maximun_column_size([110, 110,  110, 200])
        customize.set_default_settings()

    def _create_product_table(self):
        """ Cria a tabela de produtos. """
        self.product_table = QTableWidget()
        self.product_table.setColumnCount(self.count_headers)
        self.product_table.setHorizontalHeaderLabels(self.headers)
        # self.product_table.itemChanged.connect()
        self._customize_product_table()
        self.table_layout.addWidget(self.product_table)

    def run(self):
        self._initialize_ui()
        self._init_handlers()