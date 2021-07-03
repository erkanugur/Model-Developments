


def interstep_pct(df, column_pair, step):
    
    i = column_pair[0]
    
    j = column_pair[1]
    
    df[i[0]+'_'+j[0]+'_pct_'+str(step)] = df[i] / df[j].shift(step)
    
    return df

def n_interstep_pct(df,n_column_pair,n_step):
    
    for column_pair in n_column_pair:
        
        for step in n_step:
            
            df = interstep_pct(df,column_pair,step)
            
    return df




def step_pct(df,column_pair):
    
    i = column_pair[0]
    
    j = column_pair[1]
    
    df['step_pct_'+i+'_&_'+j] = df[i]/df[j]
    
    return df
  
    
    

def n_step_pct(df,n_column_pair):
    
    for column_pair in n_column_pair:
        
        df = step_pct(df,column_pair)
    
    return df