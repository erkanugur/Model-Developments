import pandas as pd

def create_metadata(df,target_column,features_drop,features_char,features_rej):
   
    features_num = [x for x in df.columns.tolist() if x not in features_rej+ features_char+features_drop +target_column]
    
    meta = pd.DataFrame()
    
    meta['variable'] = features_num + features_char + features_drop + features_rej + target_column
    
    meta = meta.set_index('variable')
    
    meta.loc[features_num,'type'] ='numeric'
    
    meta.loc[features_char,'type'] ='char'
    
    meta['status'] = 'keep'
    
    meta.loc[features_drop,'status'] ='drop_user'
    
    meta.loc[features_rej,'status'] ='rejected'
   
    meta.loc[target_column,'status'] ='target'
   
    return meta