import json
from ..custom.Utilities import Utilities


class DatabaseManager():
  def __init__(self):
    self.__load_data()
    self.utilities = Utilities()


  def __load_data(self):
    """ Carregar os dados do arquivo JSON. """
    with open('resources/database.json', 'r') as file:
      self.data = json.load(file)


  def __save_data(self):
    """ Salvar os dados do arquivo JSON. """
    with open('resources/database.json', 'w') as file:
      json.dump(self.data, file, indent=2)


  def get_product(self, product_name):
    """ Obter os detalhes de um produto. """
    return self.data.get(product_name, None)


  def update_product(self, product_name, column, new_value):
    """ Atualizar os detalhes de um produto. """
    column_map = {
      0: 'name',
      1: '',
      2: 'price',
      3: 'margin',
      4: 'marca'
    }
    field = column_map[column]
    if field not in ['name', 'marca']:
      new_value = self.utilities._clear_digits(new_value)
    self.data[product_name][field] = new_value

    self.__save_data()