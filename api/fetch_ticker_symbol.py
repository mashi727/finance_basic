# Ticker Symbol取得用
"""これは何？
ticker symbolをダウンロードして、csvに保存してdfを返す。
"""
import pandas_datareader.data as web
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
from PySide6 import QtWidgets

import os
import pandas as pd


def search_symbol():
    """_summary_
    Pandasデータフレームを使用して、NASDAQ銘柄情報を取得する関数です。
    結果は、data/ticker_symbol.csvに保存します。
    data/ticker_symbol.csvが存在すればそれを読み込み、dataフォルダがなければオンラインで読み込んでcsvを作成する。

    Returns:
        _type_: 返り値は、df_ticker_symbolでpandasのデータフレームです。
    """
    data_path = "data"#フォルダ名
    if not os.path.exists(data_path):#ディレクトリがなかったら
        os.mkdir(data_path)
    tickerSymbolFile = "./data/ticker_symbol.csv"
    try:
        df_ticker_symbol = pd.read_csv(tickerSymbolFile, index_col=0)
    except OSError as e:
        print(e)
        print('get Nasdaq Symbols...')
        df_ticker_symbol = get_nasdaq_symbols()
        df_ticker_symbol.to_csv('data/ticker_symbol.csv')
    else:
        pass
    return df_ticker_symbol


import requests
from pandas import json_normalize

def search_symbol_alphavantage(ticker_search_keyword):
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    API_KEY='0A5DAC7F3S5UWRJZ'
    SEARCH_KEY = ticker_search_keyword
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={SEARCH_KEY}&apikey=API_KEY'

    r = requests.get(url)
    data = r.json()
    df = json_normalize(data["bestMatches"])
    return df[['1. symbol', '2. name']]



