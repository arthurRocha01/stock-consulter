from .DatabaseManager import DatabaseManager
from ..custom.Utilities import Utilities
from .HandlerButton import HandlerButton


class SignalManager():
  def __init__(self):
    self.database_manager = DatabaseManager()
    self.utilities = Utilities()
    self.button_handler = HandlerButton()


  def __handle_name(self, item, name, column, new_value):
    """ Lida com o sinal da coluna Nome """
    self.database_manager.update_product(name, column, new_value)


  def __handle_price(self, item, name, column, new_value):
    """ Lida com o sinal da coluna Preço """
    self.database_manager.update_product(name, column, new_value)


  def __handle_cost_price(self, item, name, column, new_value):
    """ Lida com o sinal da coluna Custo """
    self.database_manager.update_product(name, column, new_value)


  def __handle_margin(self, item, name, column, new_value):
    """ Lida com o sinal da coluna Margin """
    self.database_manager.update_product(name, column, new_value)
    self.utilities.customize_margin(item, 2)


  def __handle_marca(self, item, name, column, new_value):
    """ Lida com o sinal da coluna Marca """
    self.database_manager.update_product(name, column, new_value)


  def __add_button_handler(self, signal):
    self.button_handler.button_add(signal)


  def __save_button_handler(self, signal):
    self.button_handler.button_save(signal)


  def __get_colunm_type(self, column):
    """ Obter o tipo de dado da coluna. """
    map_columns = {
      0: 'name',
      1: 'price',
      2: 'cost_price',
      3: 'margin',
      4: 'marca'
    }
    return map_columns.get(column, None)


  def __update_price(self, row, table_result):
    """ Atualizar o preço de venda a partir do custo e da nova margem. """
    price = table_result.item(row, 1)
    cost = table_result.item(row, 2).text()
    margin = table_result.item(row, 3).text()
    margin = self.utilities.clear_special_characters(margin)
    new_price = self.utilities.calculate_price(
      cost, margin
    )
    price.setText(new_price)


  def __response_signal(self, item, table_result, signal, row, column, name, new_value):
    """ Responder ao sinal recebido. """
    if signal == 'name':
      self.__handle_name(item, name, column, new_value)
    elif signal == 'price':
      self.__handle_price(item, name, column, new_value)
    elif signal == 'cost_price':
      self.__handle_cost_price(item, name, column, new_value)
    elif signal == 'margin':
      self.__handle_margin(item, name, column, new_value)
      self.__update_price(row, table_result)
    elif signal == 'marca':
      self.__handle_marca(item, name, column, new_value)


  def cell_signal_handler(self, table_result, item):
    """ Tratar o sinal recebido. """
    row = item.row()
    column = item.column()
    name = table_result.item(row, 0).text()
    new_value = item.text()
    signal = self.__get_colunm_type(column)
    self.__response_signal(item, table_result, signal, row, column, name, new_value)


  def button_clicked_handler(self, signal):
    if signal == 'add':
      self.__add_button_handler(signal)
    if signal == 'save':
      self.__save_button_handler(signal)