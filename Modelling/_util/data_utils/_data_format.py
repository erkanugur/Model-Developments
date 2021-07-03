# DEPENDENCIES
import pandas as pd
import numpy as np

def data_format_daily(df_stocks,column_mapping):
    
    date = column_mapping['date']
    open = column_mapping['open']
    high = column_mapping['high']
    low = column_mapping['low']
    close = column_mapping['close']
    stock = column_mapping['stock']
    volume = column_mapping['volume']
    
    print('Old data format = ', df_stocks.dtypes)
    df_stocks[date] = pd.to_datetime(df_stocks[date], format='%Y%m%d')
    df_stocks[[open, high, low, close]] = df_stocks[[open, high, low, close]].applymap(
        lambda x: str(x).replace(',', '.'))
    df_stocks[[open, high, low, close]] = df_stocks[[open, high, low, close]].astype(np.float)
    df_stocks[[open, high, low, close]] = np.round(df_stocks[[open, high, low, close]], 2)
    print('New data format = ', df_stocks.dtypes)
    
    return df_stocks





def data_format_hourly(df_stocks,column_mapping):
    
    date = column_mapping['date']
    open = column_mapping['open']
    high = column_mapping['high']
    low = column_mapping['low']
    close = column_mapping['close']
    stock = column_mapping['stock']
    volume = column_mapping['volume']
    
    print('Old data format = ', df_stocks.dtypes)
    df_stocks[datetime] = df_stocks[date]
    df_stocks[[date, time]] = df_stocks[date].str.split(n=1, expand=True)
    df_stocks[date] = pd.to_datetime(df_stocks[date], format='%Y%m%d')
    df_stocks[datetime] = pd.to_datetime(df_stocks[datetime],format='%Y%m%d %H:%M')
    df_stocks[time] = pd.to_datetime(df_stocks[time], format='%H:%M').dt.time
    df_stocks[[open, high, low, close]] = df_stocks[[open, high, low, close]].applymap(
        lambda x: str(x).replace(',', '.'))
    df_stocks[[open, high, low, close]] = df_stocks[[open, high, low, close]].astype(np.float)
    df_stocks[[open, high, low, close]] = np.round(df_stocks[[open, high, low, close]], 2)
    df_stocks = df_stocks[[stock,datetime,date,time,open,high,low,close,volume]]
    print('New data format = ', df_stocks.dtypes)
    
    return df_stocks

  
    
  
    
  
    
  
    
  
    
       
