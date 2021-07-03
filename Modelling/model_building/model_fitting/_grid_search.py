
import random
from datetime import datetime
import pandas as pd
import numpy as np
import re
import random
from dssuite.model_building.model_fitting._cross_validation import cross_validation
from xgboost import XGBClassifier

#%%



def create_starting_chromosome(base_dict):
   # Set up an initial array of all zeros
   chromosome = {}
   algorithm_list = list(base_dict.keys())
   algo_type = np.random.choice(algorithm_list)
   parameters = base_dict[algo_type].keys()
   for parameter in parameters:
       lower_band = base_dict[algo_type][parameter][0]
       upper_band = base_dict[algo_type][parameter][1]
       data_type = base_dict[algo_type][parameter][2]
       chromosome[parameter] = np.random.random_integers(lower_band,upper_band) if data_type == 'integer' else np.random.uniform(lower_band,upper_band)
       
   return chromosome

       

def create_starting_population(population_size,base_dict):
   population = []
   for i in range(population_size):
       chromosome = create_starting_chromosome(base_dict)
       population.append(chromosome)
   return population



def calculate_fitness_score(population,x_train,y_train,scoring,cv,cutoff,metadata):
    fitness_scores = []
    for chromosome in population:
        print(chromosome)
        estimator = XGBClassifier(**chromosome,use_label_encoder = False)
        train_mean,val_mean,val_std = cross_validation(estimator,metadata,x_train,y_train,scoring,cv)
   
        overfit_cutoff = abs(train_mean - val_mean)
 
        val_mean = 0 if val_mean <=0.60 else val_mean
        #val_std = 10 if val_std>0.05 else val_std
        fitness_value = val_mean / val_std
        if overfit_cutoff>cutoff:
        
            fitness_value = 0
        fitness_scores.append(fitness_value)

       
    return fitness_scores




def select_individual_by_tournament(population, fitness_scores):
   # Get population size
   population_size = len(fitness_scores)
   
   # Pick individuals for tournament
   fighter_1 = random.randint(0, population_size-1)
   fighter_2 = random.randint(0, population_size-1)
   
   # Get fitness score for each
   fighter_1_fitness = fitness_scores[fighter_1]
   fighter_2_fitness = fitness_scores[fighter_2]
   
   # Identify undividual with highest fitness
   # Fighter 1 will win if score are equal
   if fighter_1_fitness >= fighter_2_fitness:
       winner = fighter_1
   else:
       winner = fighter_2
   
   # Return the chromsome of the winner
   return population[winner]



def breed_by_crossover(parent_1, parent_2):
    from itertools import islice
    # Get length of chromosome
    chromosome_length = len(parent_1)
   
    # Pick crossover point, avoding ends of chromsome
    crossover_point = random.randint(1,3)
    parent_1 = dict(sorted(parent_1.items()))
    parent_2 = dict(sorted(parent_2.items()))
    
    inc = iter(parent_1.items())
    child_1 = dict(islice(inc,crossover_point))
    child_2 = dict(inc)
    
    
    inc = iter(parent_2.items())
    child_2_part_2 = dict(islice(inc,crossover_point))
    child_1_part_2 = dict(inc)


    # Create children. np.hstack joins two arrays
    child_1.update(child_1_part_2)

   
    child_2.update(child_2_part_2)
   
    # Return children
   
    return child_1, child_2



