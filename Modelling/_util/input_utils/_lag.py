
from dssuite._util.input_utils._input_utils import split_array


def full_lag(df, column, step):
    
    array_splitted = split_array(df[column].values, step, False)
    
    for i in range(step):
        
        df.loc[step:, column + '_lag_' + str(i + 1)] = array_splitted[:, step - i - 1]
    
    return df 


def n_full_lag(df, n_column, step):
    
    for column in n_column:
       
        df = full_lag(df, column, step)
        
    return df


def single_lag(df, column, step):
    
    array_splitted = split_array(df[column].values, step,False)
    
    df.loc[step:, column + '_lag_' + str(step)] = array_splitted[:, step - (step-1) - 1]
    
    return df


def n_single_lag(df, n_column, step):
    
    for column in n_column:
        
        df = single_lag(df, column, step)

    return df