
from dssuite._util.input_utils._input_utils import split_array
import pandas as pd
import numpy as np


def std(df, column, step):
    
    array_splitted = split_array(df[column].values, step)
    
    if len(array_splitted) == 0:
        
        df.loc[step:, 'std_' + str(step) + '_' + column] = np.nan
    
    else:
        
        df.loc[step:, 'std_' + str(step) + '_' + column] = np.std(array_splitted, axis=1)
    
    return df




def n_std(df,n_column,n_step):
    
    for i in n_column:
        
        for j in n_step:
            
            df = std(df,i,j)
    
    return df




def mindex(df, column, step):
    
    array_splitted = split_array(df[column].values, step)
    
    if len(array_splitted) == 0:
        
        df.loc[step-1:, 'min_index_' + str(step) + '_' + column] = np.nan
   
    else:
        
        df.loc[step-1:, 'min_index_' + str(step) + '_' + column] = (np.argmin(array_splitted,
                                                                            axis=1) + 1) / step  # + np.arange(0,len(np.argmin(array_splitted,axis=1)))
    return df


def minimum(df, column, step):
    
    array_splitted = split_array(df[column].values, step)
    
    if len(array_splitted) == 0:
      
        df.loc[step-1:, 'min_' + str(step) + '_' + column] = np.nan
    
    else:
      
        df.loc[step-1:, 'min_' + str(step) + '_' + column] = np.min(array_splitted, axis=1)
    
    
    df['min_' + str(step) + '_' + column] =  df[column] / df['min_' + str(step) + '_' + column]
    
    return df


def n_minimum(df, n_column, n_step):
    
    for i in n_column:
        
        for j in n_step:
           
            df = minimum(df, i, j)
    
    return df


def n_mindex(df, n_column, n_step):
    
    for i in n_column:
        
        for j in n_step:
           
            df = mindex(df, i, j)
    
    return df


def maxindex(df, column, step):
    
    array_splitted = split_array(df[column].values, step)

    if len(array_splitted) == 0:
        
        df.loc[step-1:, 'maxindex_' + str(step) + '_' + column] = np.nan
    
    else:

        df.loc[step-1:, 'maxindex_' + str(step) + '_' + column] = (np.argmax(array_splitted,
                                                                           axis=1) + 1) / step  # + np.arange(0,len(np.argmax(array_splitted,axis=1)))
    return df

def maximum(df, column, step):
   
    array_splitted = split_array(df[column].values, step)
    
    if len(array_splitted) == 0:
     
        df.loc[step:, 'max_' + str(step) + '_' + column] = np.nan

    else:
        
        df.loc[step:, 'max_' + str(step) + '_' + column] = np.max(array_splitted, axis=1)
    
    
    df['max_' + str(step) + '_' + column] =  df[column] / df['max_' + str(step) + '_' + column]
    
    return df


def n_maxindex(df, n_column, n_step):
    
    for i in n_column:
        
        for j in n_step:
            
            df = maxindex(df, i, j)
            
    return df


def n_maximum(df, n_column, n_step):
    
    for i in n_column:
        
        for j in n_step:
            
            df = maxindex(df, i, j)
    
    return df


def ema(df,column_for_ma,step):
    
    arr_ema = df[column_for_ma].ewm(span=step,min_periods=step,adjust=False,ignore_na=False).mean().values
    
    arr_ema=np.round(arr_ema,4)
    
    df['ema_'+column_for_ma+'_'+str(step)] = arr_ema
    
    df['ema_'+column_for_ma+'_'+str(step)] = df[column_for_ma] / df['ema_'+column_for_ma+'_'+str(step)]
    
    return df


def n_ema(df,n_column_for_ma,n_step,write_df=True):
    
    for i in n_column_for_ma:
        
        for j in n_step:
            
            df = ema(df,i,j)
            
    return df


        
 
def ma(df,column,step):
    
    array_splitted = split_array(df[column].values,step,include=True)
    
    if len(array_splitted)==0:
    
        df.loc[step-1:,column+'_pct']=np.nan
    
    else:
    
        df.loc[step-1:,column+'_pct']=np.sum(array_splitted,axis=1)/array_splitted.shape[1]
    
    return df
    

def n_ma(df,n_column,n_step):
    
    for column in n_column:
    
        for step in n_step:
        
            df = ma(df,column,step)
    
    return df



def avg_per_step(df,column,step,cutoff):
    
    array_splitted = split_array(df[column].values,step)
    
    for i in range(len(array_splitted)):
        
        sum_divide_len = np.sum(array_splitted[i,array_splitted[i,:]>cutoff])/step
        
        df.loc[df.index.values[step+i],'avg_per_step_'+str(step)+'_'+column+'_'+str(cutoff)] = sum_divide_len
    
    return df


def n_avg_per_step(df,n_column,n_step,n_cutoff):
    
    for column in n_column:
    
        for step in n_step:
        
            for cutoff in n_cutoff:
                
                df = avg_per_step(df,column,step,cutoff)
    
    return df

    


def avg_per_cutoff_step(df,column,step,cutoff):
    
    array_splitted = split_array(df[column].values,step)
    
    for i in range(len(array_splitted)):
    
        if len(array_splitted[i,array_splitted[i,:]>cutoff])!=0:
        
            sum_divide_len = np.sum(array_splitted[i,array_splitted[i,:]>cutoff])/len(array_splitted[i,array_splitted[i,:]>cutoff])
        
        else:
        
            sum_divide_len=0
            
        df.loc[df.index.values[step+i],'avg_per_cutoff_step_'+str(step)+'_'+column+'_'+str(cutoff)] = sum_divide_len

    return df

def n_avg_per_cutoff_step(df,n_column,n_step,n_cutoff):
    
    for column in n_column:
    
        for step in n_step:
        
            for cutoff in n_cutoff:
            
                df = avg_per_cutoff_step(df,column,step,cutoff)
    
    return df
                












