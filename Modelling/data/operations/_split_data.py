



def split_data(df,target_column,stratify_columns,oot_column = None,oot_cutoff_date = None,train_ratio = 0.7,random_state=23):
    
    from sklearn.model_selection import train_test_split
    
    df_train,df_test = train_test_split(df,
                                                  test_size=1-train_ratio,
                                                  random_state=random_state,
                                                  stratify = df[stratify_columns])

    df.loc[df_train.index.tolist(),'train_test_label'] = 'train'
    
    df.loc[df_test.index.tolist(),'train_test_label'] = 'val'
   
    if oot_cutoff_date != None and oot_column != None:
        oot_indexes = df[df[oot_column] >= oot_cutoff_date].index.tolist()
        df.loc[oot_indexes,'train_test_label'] = 'oot'
    
    print(df.groupby('train_test_label')[target_column].count())
    
    return df