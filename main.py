import sys
from PyQt6.QtWidgets import QApplication
from view.App import App
import os

def main():
  app = QApplication(sys.argv)
  stock_consulter = App()
  stock_consulter.show()
  sys.exit(app.exec())

if __name__ == "__main__":
  main()