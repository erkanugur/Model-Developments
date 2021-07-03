import numpy as np
import pandas as pd


def model_fitting(x_train, y_train, x_val, y_val,metadata,
                  model_name='XGBClassifier',param = None):
    
    
    x_train = x_train[metadata[metadata['status']=='keep'].index.tolist()]
    x_val =  x_val[metadata[metadata['status']=='keep'].index.tolist()]
    
    
    if model_name == 'XGBClassifier':
        # XGBoost
        from xgboost import XGBClassifier

        if param == None:
            param = { 'base_score':0.5,
                           'learning_rate':0.04,
                           'max_depth':2,
                           'n_estimators':15,
                           'objective':'binary:logistic',
                           'subsample':0.8
                         }

        fit_params = {
                        "early_stopping_rounds":10, 
                        "eval_metric" : "auc", 
                        "eval_set" : [(x_train, y_train), (x_val, y_val)]
                     }
        
        
        
        model = XGBClassifier(**param,use_label_encoder = False)
        
     
        model.fit(x_train, y_train,**fit_params)

    return model





