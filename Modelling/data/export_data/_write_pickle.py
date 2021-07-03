

def write_pickle(object,file_name):
    import pickle
    with open(file_name+'.pickle', 'wb') as handle:
        pickle.dump(object, handle, protocol=pickle.HIGHEST_PROTOCOL)
