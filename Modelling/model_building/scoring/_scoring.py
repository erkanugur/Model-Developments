
import numpy as np


def scoring(model,metadata, score_data,scoring_type = 'all'):
   
    score_data = score_data[metadata[metadata['status']=='keep'].index.tolist()]
    
    if scoring_type =='all':
 
        return model.predict_proba(score_data)[:, 1],model.predict(score_data).astype(np.int32)
    
    
     
    elif scoring_type =='label':
        
        return model.predict(score_data).astype(np.int32)
    
    
    elif scoring_type =='prob':
        
        return model.predict_proba(score_data)[:, 1]
    
    else:
        
        pass
 