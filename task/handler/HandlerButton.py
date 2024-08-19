from ..Register import Register

class HandlerButton():
  def __init__(self):
    pass


  def button_add(self, signal):
    self.register_window = Register()
    self.register_window.show()


  def button_save(self, signal):
    print(signal)