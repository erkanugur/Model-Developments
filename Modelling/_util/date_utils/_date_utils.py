import numpy as np
from datetime import  timedelta


def create_begin_date_list(end_date_list):
    
    begin_date_list = []
    
    for end_date in end_date_list:
    
        ref_date_begin = end_date - timedelta(days=4)
        
        begin_date_list.append(ref_date_begin)

    return begin_date_list



def create_end_date_list(date_list,ref_date_end,week_period):
    
    end_date_list = []
    
    min_date = np.min(np.array(date_list))
    
    if ref_date_end not in date_list:
    
        # datada bulunan günlerden ilk referans date mutlaka Cuma Günü olmalı
        while (ref_date_end.weekday() != 4) | (ref_date_end not in date_list):
        
            ref_date_end = ref_date_end - timedelta(days=1)

    for week in range(week_period):
            
        end_date_list.append(ref_date_end)
            
        ref_date_end = ref_date_end - timedelta(days=7)
         
        if ref_date_end-timedelta(days=4)<=min_date:
        
            break

    return end_date_list





def create_target_date_list(date_list,end_date_list,target_period):
    
    target_date_list = []
    
    targetless_end_date_list = []
    
    for end_date in end_date_list:
    
        try:
        
            ref_date_target = date_list[date_list.index(end_date) + (target_period)]
            
            target_date_list.append(ref_date_target)
        
        except:
        
            targetless_end_date_list.append(end_date)
    
    return target_date_list,targetless_end_date_list



def create_all_date_list (date_list,ref_date_end,week_period,target_period):
    
    end_date_list = create_end_date_list(date_list,ref_date_end,week_period)
    
    begin_date_list = create_begin_date_list(end_date_list)
    
    target_date_list,targetless_end_date_list = create_target_date_list(date_list,end_date_list,target_period)
    
    return begin_date_list,end_date_list,target_date_list,targetless_end_date_list
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    