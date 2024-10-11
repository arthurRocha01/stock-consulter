from .SignallManager import SignalManager
import json

class ProductModel():
    def __init__(self, product_table):
        self.signal_manager = SignalManager()
        self._initialize_product_table()
        self.product_table = product_table

    def _load_data(self):
        """ Carrega os arquivos do bancod de dados json. """
        with open('resource/database.json', 'r') as data:
            self.data = json.load(data)

    def event_handler(self, event, data=None):
        self.signal_manager.handler_signal(event, data)

    def _initialize_product_table(self):
        """ Inicializa a tabela de produtos com os dados. """
        self._load_data()
        sorted_products = dict( sorted(self.data.items()) )
        # print(sorted_products)

    def _update_table(self, products):
        """ Atualiza a tabela de produtos com os dados filtrados. """
        self.product_table.blockSignal(True)
        self.product_table.setRowCount( len(products) )