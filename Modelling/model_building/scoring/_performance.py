import pandas as pd
from dssuite.model_building.scoring._scoring import scoring

def cm_stats(target, prediction, row_name=0):
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import precision_score
    from sklearn.metrics import recall_score
    from sklearn.metrics import f1_score

    df_metric = pd.DataFrame()
    
    df_metric.loc[row_name, 'accuracy_score'] = accuracy_score(target, prediction)
    
    df_metric.loc[row_name, 'precision_score'] = precision_score(target, prediction)
    
    df_metric.loc[row_name, 'recall_score'] = recall_score(target, prediction)
    
    df_metric.loc[row_name, 'f1_score'] = f1_score(target, prediction)
    
    return df_metric


def cm(target, prediction, row_name=0):
    
    from sklearn.metrics import confusion_matrix
    
    df_conf_matrix = pd.DataFrame(confusion_matrix(target, prediction))
    
    df_conf_matrix['index'] = row_name
    
    df_conf_matrix['index'] = df_conf_matrix['index'] + ['_F', '_T']
    
    df_conf_matrix = df_conf_matrix.set_index('index')

    return df_conf_matrix



def model_perf(model,
               metadata,
               x_train,
               y_train,
               x_val,
               y_val,
               x_oot=None,
               y_oot=None,
               print_flag=True):
    
    
    #DEPENDENCIES
    
    from sklearn.metrics import roc_auc_score
    
    
    x_train = x_train[metadata[metadata['status']=='keep'].index.tolist()]
    
    
    #VARIABLE IMPORTANCE
    variableimportance = pd.DataFrame(model.feature_importances_, columns=['Importance'],
                                      index=x_train.columns).sort_values(by=['Importance'], ascending=False)





    #PREDICTIONS
    y_train_sc,y_train_pred = scoring(model,metadata, x_train,scoring_type = 'all')
    y_val_sc,y_val_pred = scoring(model,metadata, x_val,scoring_type = 'all')



    if any(x_oot != None):
        y_oot_sc,y_oot_pred = scoring(model,metadata, x_oot,scoring_type = 'all')
         
   
    
    #ROC
    df_roc = pd.DataFrame()
    
    df_roc.loc['train', 'ROC'] = roc_auc_score(y_train, y_train_sc)
    
    df_roc.loc['val', 'ROC'] = roc_auc_score(y_val, y_val_sc)
    
    if any(y_oot != None):
        df_roc.loc['oot', 'ROC'] = roc_auc_score(y_oot, y_oot_sc)

    
    
    #CONFUSION MATRIX
    cm_list = []
    cm_list.append(cm_stats(y_train, y_train_pred, row_name='train'))
    cm_list.append(cm_stats(y_val, y_val_pred, row_name='test'))
    if any(y_oot != None):
        cm_list.append(cm_stats(y_oot, y_oot_pred, row_name='oot'))
    df_cm_stats = pd.concat(cm_list)

    cm_list = []
    cm_list.append(cm(y_train, y_train_pred, row_name='train'))
    cm_list.append(cm(y_val, y_val_pred, row_name='test'))
    if any(y_oot != None):
        cm_list.append(cm(y_oot, y_oot_pred, row_name='oot'))
    df_cm_all = pd.concat(cm_list)

    if print_flag:
        print(variableimportance[:20])
        print(df_roc)
        print(df_cm_stats)
        print(df_cm_all)

    return variableimportance, df_cm_all, df_roc, df_cm_stats







def lift_table(scoredata,score_column, target_column):

    lift_table = pd.DataFrame()
    
    scoredata['Quantile'] = pd.qcut(scoredata[score_column].rank(method='first'), 10, labels=False)
    
    lift_table['Mean'] = scoredata.groupby(by=['Quantile'])[score_column].mean()
    
    lift_table['T_0'] = scoredata[scoredata[target_column] == 0].groupby(by=['Quantile']).size()
    
    lift_table['T_1'] = scoredata[scoredata[target_column] == 1].groupby(by=['Quantile']).size()
    
    lift_table['N'] = scoredata.groupby(by=['Quantile']).size()
    
    lift_table['Mean_Odds'] = scoredata.loc[scoredata[target_column] == 1,score_column].count() / scoredata[score_column].count()
    
    lift_table['Odds'] = lift_table['T_1'] / lift_table['N']
    
    lift_table['Lift_Odds'] = lift_table['Odds'] / lift_table['Mean_Odds']

    print(lift_table)
    
    return lift_table
