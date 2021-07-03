import numpy as np
import pandas as pd


def diff_list(li1, li2):
    return (list(set(li1) - set(li2)))




def make_combinations(combination_list,number):
    
    from itertools import combinations
    
    return list(combinations(combination_list,number))



def make_products(list1,list2):
    
    from itertools import product
    
    return list(product(list1,list2))




def split_array(array, step, include=True):
    
    if include:
       
        k = 1
    
    else:
        
        k = 0

    array_splitted = []

    for i in range(len(array)):

        end_ix = i + step - k
       
        if end_ix > len(array) - 1:
            
            break
       
        arr_x = array[i:end_ix + k]
        
        array_splitted.append(arr_x)

    array_splitted = np.array(array_splitted)
    
    return array_splitted




