# -*- coding: utf-8 -*-
"""
Created on Wed May 26 21:00:59 2021

@author: erkan
"""

import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score
from xgboost import XGBClassifier


def unigini_elimination(x_train,
           y_train,
           x_val,
           y_val,
           metadata,
           cut_off_below = 0.6,
           cut_off_change = 0.05):
    
    print('unigini elimination is started')
    
    features = metadata[(metadata['status']=='keep') ].index.tolist()
    unigini=pd.DataFrame()
    unigini.index.name = 'variable'
    
    for var in features:
       
        data_x = x_train[[var]].values
        data_y = y_train
        mdl=XGBClassifier(max_depth=3,n_estimators=1,use_label_encoder = False)
        mdl.fit(data_x,data_y)
        data_y_predicted=mdl.predict_proba(data_x)
        
        unigini.loc[var, 'train_roc']=roc_auc_score(y_train, pd.DataFrame(data_y_predicted)[1])
      
        data_x=x_val[[var]].values
        data_y=y_val
        mdll=XGBClassifier(max_depth=3,n_estimators=1,use_label_encoder = False)
        mdll.fit(data_x,data_y)
        data_y_predicted=mdll.predict_proba(data_x)
        unigini.loc[var, 'val_roc']=roc_auc_score(y_val, pd.DataFrame(data_y_predicted)[1])
        
        
    
    unigini['change']=np.abs(unigini['train_roc']-unigini['val_roc'])
    unigini['status'] = np.where(unigini['train_roc']<cut_off_below,'DROP_BELOW', 'KEEP' )
    unigini['status'] = np.where(unigini['change']>cut_off_change,'DROP_CHANGE',unigini['status'])
    
    
    
    for var in unigini.index.tolist():
        metadata.loc[var,'status'] = np.where(unigini.loc[var,'status']=='DROP_CHANGE' ,'DROP_UNIGINI_CHANGE',metadata.loc[var,'status'])
        metadata.loc[var,'status'] =  np.where(unigini.loc[var,'status']=='DROP_BELOW','DROP_UNIGINI_BELOW',metadata.loc[var,'status'] )
    
    unigini.reset_index(inplace=True)
    print('unigini elimination is completed')
    
    return unigini,metadata