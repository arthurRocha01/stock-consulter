from PyQt6.QtWidgets import (
  QWidget, QVBoxLayout
)
from .Searcher import Searcher

class App(QWidget):
  def __init__(self):
    super().__init__()
    self._create_window()
    self._create_layout()
    self._run()

  def _create_window(self):
    """ Cria a janela principal."""
    self.setWindowTitle("Stock-Consulter")
    self.resize(400, 300)

  def _create_layout(self):
    """ Cria o layout principal."""
    self.main_layout = QVBoxLayout()
    self.setLayout(self.main_layout)

  def _run(self):
    self.searcher = Searcher(self.main_layout)
    self.searcher.run()