from PySide6 import QtCore
from PySide6.QtCore import *

import pandas as pd

class TableModel(QtCore.QAbstractTableModel):
    """_summary_
    データフレームの値をテーブルに読み込むためのクラスで、QAbstractItemModelを継承したQAbstractTableModelを使用しして作成します。
    モデルクラスには、以下の設定が必要です。
        __init__(self, *)
        data(self, index, role)
        rowCount(self, parent=QModelIndex())
        columnCount(self, parent=QModelIndex())
        headerData(self, section, orientation, role)
    使い方:
        self.tableView.setModel(some_dataframe)
        self.tableView.horizontalHeader().setStretchLastSection(False)
        self.tableView.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode(3)) # 3 -> Resize to contents
        dataframeを設定して、dfの列ごとに表示の有無などを設定します。
    """
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])
        return ""  # There is no vertical header

def make_masked_tableview_model(df_ticker_symbol, ticker_search_keyword):
    """_summary_

    Args:
        df_ticker_symbol (_type_): 検索する対象です。
        ticker_search_keyword (_type_): 検索するキーワードを指定します。

    Returns:
        _type_: TableModelクラスの引数となるtableview_model_dataを返します。
    """
    df_print = df_ticker_symbol.loc[:,['NASDAQ Symbol','Security Name']]
    data =  df_print[df_print['Security Name'].str.contains(ticker_search_keyword)]
    tableview_model_data = TableModel(data)
    '''
    attributes = dir(tableview_model_data)
    n_max = len(attributes)
    for (n, attribute) in enumerate(attributes, start=1):
        pass
        print(f'{n}/{n_max} {attribute}')
    '''
    return tableview_model_data


def make_tableview_model(data):
    tableview_model_data = TableModel(data)    
    '''
    attributes = dir(tableview_model_data)
    n_max = len(attributes)
    for (n, attribute) in enumerate(attributes, start=1):
        pass
        print(f'{n}/{n_max} {attribute}')
    '''

    return tableview_model_data
