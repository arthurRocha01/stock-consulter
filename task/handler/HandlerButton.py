from ..Register import Register
from .HandlerField import HandlerField
from..handler.DatabaseManager import DatabaseManager

class HandlerButton():
  def __init__(self, main_layout):
    self.handler_field = HandlerField(main_layout)
    self.handler_database = DatabaseManager()


  def button_add(self, signal):
    self.register_window = Register()
    self.register_window.show()


  def button_save(self, signal):
    values = self.handler_field.get_field_values(signal)
    print(values)
    self.handler_database.add_product(values)