import re

class Utilities():
  def clear_special_characters(self, string):
    return re.sub(r'[^\w\s.]', '', string)


  def _clear_digits(self, digits):
    return re.sub(r'\D+', '', digits)


  def _format_decimal(self, number):
    return float(number.replace(',', '.'))


  def calculate_price(self, price, margin):
    try:
      price = self._format_decimal(price)
      margin = self._format_decimal(margin)
      if price:
        sale_price = price * (1 + margin / 100)
      return str(round(sale_price, 2))
    except Exception:
      return str(0.00)


  def customize_margin(self, value, method=1):
    if method == 1:
      if not value.endswith('%'):
        return f'{value} %'
    else:
      new_value = value.text()
      if not new_value.endswith('%'):
        value.setText(f'{new_value} %')