import pandas as pd
from dssuite._util.input_utils._input_utils import diff_list
def create_input(df_stocks,create_input_dictionary):
    input_produced = []
    stock_list = list(df_stocks['stock'].unique())
    i = 0
    for key in create_input_dictionary.keys():
        print(key)
        current_columns = df_stocks.columns.tolist()
        df_subsets = []
        j = 0
        function = create_input_dictionary[key]['function']
        parameters = create_input_dictionary[key]['parameters']
        for stock in stock_list:
            df = df_stocks.loc[df_stocks['stock']==stock].copy()
            df.reset_index(drop=True,inplace=True)
            
            if len(parameters)==1:
                df = function(df, parameters[0])
            elif len(parameters)==2:
                df = function(df, parameters[0],parameters[1])
            elif len(parameters)==3:
                df = function(df, parameters[0],parameters[1],parameters[2])
            elif len(parameters)==4:
                df = function(df, parameters[0],parameters[1],parameters[2],parameters[3])
            elif len(parameters)==5:
                df = function(df, parameters[0],parameters[1],parameters[2],parameters[3],parameters[4])
            elif len(parameters)==6:
                df = function(df, parameters[0],parameters[1],parameters[2],parameters[3],parameters[4],parameters[5])
            else:
                pass
            
            
            df_subsets.append(df)
            j+=1
            
        
        #INPUT ÜRETME KISMI BİTTİ.
        join_keys = ['date','stock']
        if i == 0:  
        
            df_inputs_all = pd.concat(df_subsets)
            df_inputs_all.dropna(inplace=True)
            new_columns = df_inputs_all.columns.tolist()
            input_produced += diff_list(new_columns,current_columns)
            df_inputs_all = df_inputs_all[join_keys+input_produced]
            
        else:
            df_inputs = pd.concat(df_subsets)
            df_inputs.dropna(inplace=True)
            new_columns = df_inputs.columns.tolist()
            df_inputs_all = pd.merge(df_inputs_all,df_inputs,how='inner',on = join_keys)
            input_produced += diff_list(new_columns,current_columns)
            df_inputs_all = df_inputs_all[join_keys+input_produced]
        
        i+=1
        
    return df_inputs_all,input_produced
