import numpy as np
import pandas as pd


def cutoff_study(df_score, score_column, target_column):
    #DEPENDENCIES
    
    from sklearn.metrics import confusion_matrix
    
    a = []
   
    score_column = 'score'
    
    model_id = 'target1'
    
    for trsh in np.arange(0, 1, 0.01):
    
        df_score_ = df_score.copy()
        
        df_score_["y_pred"] = np.where(df_score_[score_column] >= trsh, 1, 0)
        
        
        cm = confusion_matrix(df_score_[target_column], df_score_['y_pred'])
        
        df_results = pd.DataFrame(
            columns=['Threshold', 'Accuracy', 'F1 score', 'Recall', 'Precision', 'Abs_Diff', 'TP', 'FP', 'TN', 'FN',
                     'TP+FP'])
        
        df_results.loc[model_id, 'Threshold'] = trsh
        
        df_results.loc[model_id, 'Accuracy'] = np.round((cm[0, 0] + cm[1, 1]) / cm.sum(), 3)
        
        df_results.loc[model_id, 'Precision'] = np.round(cm[1, 1] / (cm[0, 1] + cm[1, 1]), 3)
        
        df_results.loc[model_id, 'Recall'] = np.round(cm[1, 1] / (cm[1, 1] + cm[1, 0]), 3)
        
        df_results.loc[model_id, 'F1 score'] = np.round(
            2 * df_results.loc[model_id, 'Precision'] * df_results.loc[model_id, 'Recall'] / (
                        df_results.loc[model_id, 'Precision'] + df_results.loc[model_id, 'Recall']), 3)
        
        df_results.loc[model_id, 'Abs_Diff'] = np.abs(
            df_results.loc[model_id, 'Precision'] - df_results.loc[model_id, 'Recall'])
        
        df_results.loc[model_id, 'TP'] = cm[1, 1]
        
        df_results.loc[model_id, 'FP'] = cm[0, 1]
        
        df_results.loc[model_id, 'TN'] = cm[0, 0]
        
        df_results.loc[model_id, 'FN'] = cm[1, 0]
        
        df_results.loc[model_id, 'TP+FP'] = cm[1, 1] + cm[0, 1]
  
        a.append(df_results)
        

    df_cut_off = pd.concat(a)
    
    return df_cut_off