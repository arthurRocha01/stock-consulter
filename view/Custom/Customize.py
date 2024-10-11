from PyQt6.QtWidgets import QHeaderView
from PyQt6.QtGui import QFont

class TableCustomize():
    def __init__(self, product_table):
        self.product_table = product_table
        self.headers = self.product_table.horizontalHeader()

    def _set_behavior(self):
        """ Seta o comportamento da tabela. """
        header_count = len(self.headers)
        for col in range(header_count):
            self.headers.setSectionResizeMode(col, QHeaderView.ResizeMode.Stretch)

    def set_maximun_column_size(self, settings):
        """ Seta o tamanho maxímo das colunas. """
        for index, size in enumerate(settings, start=1):
            self.headers.setSectionResizeMode(index, QHeaderView.ResizeMode.Interactive)
            self.headers.resizeSection(index, size)

    def _set_visual_settings(self):
        """ Seta configurações visuais do cabeçalho e tabela. """
        self.product_table.setStyleSheet('''
            QTaleWidget::item {
                    border-bottom: 1px solid #dcdcdc; /* Cor da borda inferior das linhas */
                    border-right: 1px solid #dcdcdc; /* Cor da borda direita das colunas */
                    padding: 5px; /* Espaçamento interno dos items */
                }
        ''')
        self.headers.setStyleSheet('''
            font-size: 20px;
            font-weight: bold;
        ''')

    def set_default_settings(self):
        self._set_behavior()
        self._set_visual_settings()