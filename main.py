import sys
from PyQt6.QtWidgets import QApplication
from task.App import StockConsulter

def main():
  app = QApplication(sys.argv)
  headers = ['Nome', 'Preço', 'Custo', 'Margem', 'Marca']
  stock_consulter = StockConsulter(headers)
  stock_consulter.show()
  sys.exit(app.exec())

if __name__ == '__main__':
  main()