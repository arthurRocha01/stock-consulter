import sys
from PyQt6.QtWidgets import QApplication
from task.App import StockConsulter

def main():
  app = QApplication(sys.argv)
  headers = ['Produto', 'Preço', 'Margem', 'Marca']
  stock_consulter = StockConsulter()
  stock_consulter.show()
  sys.exit(app.exec())

if __name__ == '__main__':
  main()