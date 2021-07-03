import numpy as np


def color_tod(df, column_pair,bar_type='raw'):
    # orijinal dataframe'i korumak için deep copy alınır.
    df_copy = df.copy()
    # column_pair olarak liste halinde verilen kolonlar ayrıştırılır.
    column_f = column_pair[0]
    column_s = column_pair[1]
    # oluşturulacak olan değişken adı için tag hazırlanır.
    if bar_type=='raw':
        tag = column_f[0] + '_' + column_s[0]
    elif bar_type =='heikin':
        tag = 'heikin_'+column_f.split('_')[1][0].lower() + '_' + column_s.split('_')[1][0].lower()
    # ilgili değişken oluşturulur.
    df_copy[tag + '_color_tod'] = np.where(df_copy[column_f] < df_copy[column_s], 1, 0)
    # kopyalanan dataframe return olarak dönülür.
    return df_copy


def color_yes(df, column_pair,bar_type='raw'):
    # orijinal dataframe'i korumak için deep copy alınır.
    df_copy = df.copy()
    # column_pair olarak liste halinde verilen kolonlar ayrıştırılır.
    column_f = column_pair[0]
    column_s = column_pair[1]
    # oluşturulacak olan değişken adı için tag hazırlanır.
    if bar_type=='raw':
        tag = column_f[0] + '_' + column_s[0]
    elif bar_type =='heikin':
        tag = 'heikin_'+column_f.split('_')[1][0].lower() + '_' + column_s.split('_')[1][0].lower()
    else:
        pass
    # ilgili değişken oluşturulur.
    df_copy[tag + '_color_yes'] = np.where(df_copy[column_f].shift() < df_copy[column_s], 1, 0)
    # kopyalanan dataframe return olarak dönülür.
    return df_copy

def n_color_yes(df, n_column_pair,bar_type='raw'):
    df_bar_color = df.copy()
    for column_pair in n_column_pair:
        df_bar_color = color_yes(df_bar_color,column_pair,bar_type)
    return df_bar_color