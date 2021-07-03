import numpy as np
import pandas as pd

def rsi(df,column_for_rsi,step):
    
    arr_for_rsi = df[column_for_rsi].values
    
    arr_change = np.insert(arr_for_rsi[1:] - arr_for_rsi[:-1], 0, np.nan)
    
    arr_gain = np.where(arr_change<0,0,arr_change)
    
    arr_loss = np.abs(np.where(arr_change>0,0,arr_change))
    
    arr_gain_avg = pd.Series(arr_gain).rolling(step).mean().values
    
    arr_loss_avg = pd.Series(arr_loss).rolling(step).mean().values
    
    arr_rs = arr_gain_avg/arr_loss_avg
    
    arr_rsi = np.where (arr_loss_avg == 0,100,100-(100/(1+arr_rs)))
    
    arr_rsi = np.round(arr_rsi,4)
    
    df['rsi_'+column_for_rsi+'_'+str(step)] = arr_rsi
    
    return df




def n_rsi(df,n_column_for_rsi,n_step):
     
    for i in n_column_for_rsi:
        
        for j in n_step:
            
            df = rsi(df,i,j)
            
    return df
