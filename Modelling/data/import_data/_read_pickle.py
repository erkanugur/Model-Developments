

def read_pickle(file_name):
    import pickle
    with open(file_name+'.pickle', 'rb') as handle:
        return pickle.load(handle)
