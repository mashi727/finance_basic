apikey_path = './.alpha_vantage_apikey'
with open(apikey_path) as f:
    API_KEY = f.readlines()[0]

def fetch_4values(company_data, fetch_span):
    # 四本値を取ってくる。
    from alpha_vantage.techindicators import TechIndicators
    symbol=company_data[0]
    from alpha_vantage.timeseries import TimeSeries
    ts = TimeSeries(key=API_KEY, output_format='pandas')
    if fetch_span == 'Daily':
        data, meta_data = ts.get_daily(symbol=symbol,outputsize='full')
        print(fetch_span)
    else:
        data, meta_data = ts.get_intraday(symbol=symbol,interval=fetch_span, outputsize='full')
        print(fetch_span)
    # 行名を変更する。
    df = data.rename(columns={'1. open': 'Open', '2. high': 'High', '3. low':'Low','4. close':'Close'})
    return df.sort_index(axis=0, level=None, ascending=True)

def fetch_4values_adjust(company_data, fetch_span):
    # 四本値を取ってくる。
    from alpha_vantage.techindicators import TechIndicators
    symbol=company_data[0]
    from alpha_vantage.timeseries import TimeSeries
    ts = TimeSeries(key=API_KEY, output_format='pandas')
    if fetch_span == 'Daily':
        data, meta_data = ts.get_daily_adjusted(symbol=symbol, outputsize='full')
        print(fetch_span)
    else:
        data, meta_data = ts.get_intraday_extended(symbol=symbol, adjusted='true' ,interval=fetch_span, outputsize='full')
        print(fetch_span)
    # 行名を変更する。
    df = data.rename(columns={'1. open': 'Open', '2. high': 'High', '3. low':'Low','4. close':'Close', '5. adjusted close':'Adj Close', '6. volume':'Volume'})
    
    return df.sort_index(axis=0, level=None, ascending=True)

def create_df():
    import pandas as pd
    import numpy as np
    # 適当な四本値をつくる
    n = 200000
    index = pd.date_range(start='20170101', periods=n, freq='T')
    s = pd.Series(np.random.randn(n).cumsum(), index=index)
    s += abs(s.min())*2
    df = s.resample('H').ohlc()
    df.columns = df.columns.map(str.capitalize)
    return df


def make_dataframe(df, sma_short, sma_med, sma_long):
    df['sma_short'] = df['Close'].rolling(sma_short).mean() # 10の窓をずらすので最初の9はNaNになるよ。10の移動平均
    df['sma_med'] = df['Close'].rolling(sma_med).mean() # 10の窓をずらすので最初の9はNaNになるよ。10の移動平均
    df['sma_long'] = df['Close'].rolling(sma_long).mean() # 10の窓をずらすので最初の9はNaNになるよ。10の移動平均
    
    #MACD
    df['macd'] = df['Close'].rolling(12).mean()-df['Close'].rolling(26).mean() # sma版
    df['macd_sig'] = df['macd'].rolling(9).mean()
    df['macd_hist'] = df['macd']-df['macd_sig']

    
    #df['6stages'] = 
    df.loc[(df['sma_short'] < df['sma_med'])   & (df['sma_med']   < df['sma_long'])  , 'stage'] = 1
    df.loc[(df['sma_med']   < df['sma_short']) & (df['sma_short'] < df['sma_long'])  , 'stage'] = 2
    df.loc[(df['sma_med']   < df['sma_long'])  & (df['sma_long']  < df['sma_short']) , 'stage'] = 3
    df.loc[(df['sma_long']  < df['sma_med'])   & (df['sma_med']   < df['sma_short']) , 'stage'] = 4
    df.loc[(df['sma_long']  < df['sma_short']) & (df['sma_short'] < df['sma_med'])   , 'stage'] = 5
    df.loc[(df['sma_short'] < df['sma_long'])  & (df['sma_long']  < df['sma_med'])   , 'stage'] = 6
    #print(df)
    return df


'''

def update_dataframe(short, long):
    # 四本値を取ってくる。
    from alpha_vantage.techindicators import TechIndicators
    symbol=company_data[0]
    from alpha_vantage.timeseries import TimeSeries
    ts = TimeSeries(key=API_KEY, output_format='pandas')
    if fetch_span == 'Daily':
        data, meta_data = ts.get_daily(symbol=symbol,outputsize='full')
        print(fetch_span)
    else:
        data, meta_data = ts.get_intraday(symbol=symbol,interval=fetch_span, outputsize='full')
        print(fetch_span)
    # 行名を変更する。
    df = data.rename(columns={'1. open': 'Open', '2. high': 'High', '3. low':'Low','4. close':'Close'})
    # dockarea描画用に適当にインジケータを用意
    df['sma_short'] = df['Close'].rolling(short).mean() # 10の窓をずらすので最初の9はNaNになるよ。10の移動平均
    df['sma_long'] = df['Close'].rolling(long).mean() # 10の窓をずらすので最初の9はNaNになるよ。10の移動平均
    print(df)
    return df
    
'''