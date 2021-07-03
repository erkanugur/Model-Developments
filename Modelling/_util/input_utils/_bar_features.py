def bar_features(df, column_dict,bar_type='raw'):
    # orijinal dataframe'i korumak için deep copy alınır.
    df_copy = df.copy()
    # open,high,low,close değerlerinin tutulduğu kolon isimleri sözlükten okunur.
    open = column_dict['open']
    high = column_dict['high']
    low = column_dict['low']
    close = column_dict['close']
    # oluşturulacak değişkenleri normalize etmek için ortalama fiyat hesaplanır.
    norm = (df_copy[high] + df_copy[low] + df_copy[open] + df_copy[close]) / 4
    if bar_type == 'raw':
        upper_shadow_column = 'upper_shadow'
        lower_shadow_column = 'lower_shadow'
        abs_body_column = 'abs_body'
        body_column = 'body'
        daily_range_column = 'daily_range'

    elif bar_type == 'heikin':
        upper_shadow_column = 'h_upper_shadow'
        lower_shadow_column = 'h_lower_shadow'
        abs_body_column = 'h_abs_body'
        body_column = 'h_body'
        daily_range_column = 'h_daily_range'
    # üst diken, alt diken, mutlak gövde ,gövde ve günlük aralık değerleri hesaplanır.
    df_copy[upper_shadow_column] = df_copy[high] - df_copy[[open, close]].max(axis=1)
    df_copy[lower_shadow_column] = df_copy[[open, close]].min(axis=1) - df_copy[low]
    df_copy[abs_body_column] = df_copy[[open, close]].max(axis=1) - df_copy[[open, close]].min(axis=1)
    df_copy[body_column] = df_copy[close] - df_copy[open]
    df_copy[daily_range_column] = df_copy[high] - df_copy[low]
    # hesaplanan değişkenler normalize edilir.
    df_copy[upper_shadow_column] = (df_copy[upper_shadow_column] / norm)/0.05
    df_copy[lower_shadow_column] = (df_copy[lower_shadow_column] / norm)/0.05
    df_copy[body_column]  = (df_copy[body_column]  / norm)/0.05
    df_copy[abs_body_column] = ( df_copy[abs_body_column]  / norm)/0.05
    df_copy[daily_range_column]  = (df_copy[daily_range_column]  / norm)/0.05
    # kopyalanan dataframe return olarak dönülür.
    return df_copy