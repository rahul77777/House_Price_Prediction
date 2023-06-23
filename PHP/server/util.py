import pickle
import json
import numpy as np

__localities = None
__data_columns = None
__model = None

def get_estimated_price(locality,area_in_sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(locality.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = area_in_sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __localities

    with open("./artifacts/pune_locality.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __localities = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('./artifacts/pune_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_locality_names():
    return __localities

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_locality_names())
    print(get_estimated_price('Fatima Nagar',1000, 3, 3))
    print(get_estimated_price('Fatima Nagar', 1000, 2, 2))
    #print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    #print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location