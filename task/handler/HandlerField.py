class HandlerField():
  def __init__(self, main_layout):
    self.main_layout = main_layout


  def get_field_values(self, signal):
    values = {}
    field_names = ['Name', 'Fabricator', 'Price', 'Margin',
    'CST', 'NCM', 'Aliquot']
    for i, field_name in enumerate(field_names):
      layout = self.main_layout.itemAt(i).layout()
      widget = layout.itemAt(1).widget()
      value = widget.text()
      values[field_name] = value
    return values