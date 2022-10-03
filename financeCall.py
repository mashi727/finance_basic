'''
Imports are always put at the top of the file, just after any module
comments and docstrings, and before module globals and constants.

Imports should be grouped in the following order:

1. Standard library imports.
2. Related third party imports.
3. Local application/library specific imports.

You should put a blank line between each group of imports.
'''
import sys
import numpy as np
from datetime import datetime

from PySide6.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QWidget
from PySide6.QtGui import Qt
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox

import pyqtgraph as pg
from pyqtgraph.dockarea import Dock
from pyqtgraph import QtCore, QtGui

# 自作のライブラリ
from financeUi import Ui_MainWindow
from commands.make_tableview_mode import *
from api.fetch_ticker_symbol import *
from api.prepare_dataframe import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.init_ui()
        
        # 検索キー（searchSymbol）が変更されたら、自動的にtableViewに表示
        self.search_ticker_symbol.textEdited.connect(self.searchSymbol)
        self.tableView_ticker_symbols.doubleClicked.connect(lambda: self.plot_graph('fetch_4values'))

        self.plot()


    def init_ui(self):
        self.setGeometry(100, 100, 2400, 1400)


    def searchSymbol(self):
        ticker_search_keyword = self.search_ticker_symbol.text() # Search Keywordの取得
        self.tableView_ticker_symbols.setModel(make_masked_tableview_model(search_symbol(),ticker_search_keyword))
        self.tableView_ticker_symbols.horizontalHeader().setStretchLastSection(False)
        self.tableView_ticker_symbols.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode(3)) # 3 -> Resize to contents
        self.tableView_ticker_symbols.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode(1)) # 1 -> stretch

    def get_ticker_symbol(self):
        index = self.tableView_ticker_symbols.currentIndex()
        #company_name = self.tableView_ticker_symbols.model().index(index.row(), 1).data()
        company_data = []
        for i in range(2):
            company_data.append(self.tableView_ticker_symbols.model().index(index.row(), i).data())
        return company_data # ticker_symbol, 社名


    def plot_graph(self, discriminator):
        if discriminator=='fetch_4values':
            print('Im in fetch_4values!')
            company_data = self.get_ticker_symbol()
            # for actual data
            self.df_4values = fetch_4values(company_data, self.combobox_time_span.currentText()) # comboBox.current.Text()は、取得するspan
            # テスト用に、ローカルファイルから四本値を読み込み
            #self.df_4values.to_csv('data/aapl.csv')
            #self.df_4values = pd.read_csv('./data/aapl.csv', index_col='date', parse_dates=True)
            if not company_data:
                #pass
                QMessageBox.warning(None, "Notice!", "Ticker symbolを入力してください!", QMessageBox.Yes)
            else:
                # status barの表示
                status_bar = self.statusBar() # 下にあるステータスバー
                status_bar.showMessage('表示中の銘柄 : ' + str(company_data[1])) # 書きたいメッセージ
                df = make_dataframe(self.df_4values, int(self.SB_sma_short.text()), int(self.SB_sma_med.text()), int(self.SB_sma_long.text()))
                last_region = []
                self.plot_stock(df, last_region)
        else:
            print('Im in update sma_values!')
            df = make_dataframe(self.df_4values, int(self.SB_sma_short.text()), int(self.SB_sma_med.text()), int(self.SB_sma_long.text()))
            last_region = [self.minx, self.maxx]
            self.plot_stock(df, last_region)


    def plot_stock(self, df, last_region):
        print(df)
        pass


    def plot(self):
        # Dockの準備
        self.d1 = Dock('chart', size=(20, 15))
        self.d2 = Dock('region', size=(1, 2))

        self.graphicsView.addDock(self.d1)
        self.graphicsView.addDock(self.d2)
        glw = pg.GraphicsLayoutWidget()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    from pyqtgraph.dockarea.Dock import DockLabel
    def updateStyle(self):
        self.setStyleSheet("DockLabel { color: #FFF; background-color: #444; font-size:20pt}")
    setattr(DockLabel, 'updateStyle', updateStyle)

    style = """
        QWidget { color: #AAA; background-color: #333; border: 0px; padding:0px; }
        QWidget:item:selected { background-color: #666; }
        QMenuBar::item { background: transparent; }
        QMenuBar::item:selected { background: transparent; border: 1px solid#666; }
    """
    main()