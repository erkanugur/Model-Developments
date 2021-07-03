
import pandas as pd
#heikin ashi hesaplama mantığında open değerinin hesaplanması iteratif bir şekilde olması gerektiği için ve satır bazında group by fonksiyonu kullanılmadığından hisseleri for döngüsünde döndürerek hesaplandı.
def HA(df,column_dict):
    # orijinal dataframe'i korumak için deep copy alınır.
    df_copy = df.copy()
    # open,high,low,close değerlerinin tutulduğu kolon isimleri sözlükten okunur.
    open = column_dict['open']
    high = column_dict['high']
    low = column_dict['low']
    close = column_dict['close']
    stock = column_dict['stock']
    stock_list = df[stock].unique().tolist()
    df_subset_list = []
    for stock in stock_list:
        df_subset = df[df['stock']==stock]
        df_subset_copy = df_copy[df_copy['stock']==stock]
        df_subset_copy[close] = (df_subset[open] + df_subset[high] + df_subset[low] + df_subset[close]) / 4
        df_subset.reset_index(inplace=True,drop=True)
        df_subset_copy.reset_index(inplace=True,drop=True)
        for i in range(0, len(df_subset)):
            if i == 0:
                df_subset_copy.at[i, open] = (df_subset.at[i, open] + df_subset.at[i, close]) / 2
            else:
                df_subset_copy.at[i, open] = (df_subset_copy.at[i-1, open] + df_subset_copy.at[i-1, close]) / 2


        # heiken high hesaplanır. heiken open, heiken close ve high değerlerinden maksimum olanıdır.
        df_subset_copy[high] = df_subset_copy.loc[:, [open, close]].join(df_subset[high]).max(axis=1)
        # heiken high hesaplanır. heiken open, heiken close ve low değerlerinden minimum olanıdır.
        df_subset_copy[low] = df_subset_copy.loc[:, [open, close]].join(df_subset[low]).min(axis=1)
        # heiken değişkenlerinin ismi rename edilir.
        df_subset_copy.rename(columns={open: 'h_' + open, high: 'h_' + high, low: 'h_' + low, close: 'h_' + close}, inplace=True)
        df_subset_list.append(df_subset_copy)

    df_copy = pd.concat(df_subset_list)

    return df_copy
    
    
    
    
    
    
    
    
   