# -*- coding: utf-8 -*-
"""
Created on Sat May 22 18:06:12 2021

@author: erkan
"""

def cross_validation(estimator,metadata,x_train,y_train,scoring,cv):
    x_train_ = x_train[metadata[metadata['status']=='keep'].index.tolist()].copy()
    from sklearn.model_selection import cross_validate
    
    cross_val_scores = cross_validate(estimator = estimator,X = x_train, y = y_train,scoring = scoring, cv = cv,n_jobs = -1, return_train_score = True)
    
    cross_train_mean_score = cross_val_scores['train_score'].mean()
    cross_val_mean_score = cross_val_scores['test_score'].mean()
    cross_val_std_score = cross_val_scores['test_score'].std()
    
    return  cross_train_mean_score,cross_val_mean_score,cross_val_std_score
