import json
import pickle
import numpy as np


locations = None
data_columns = None
model = None
def get_estimate_price(locations,sqft,bhk,bath):
    try:
        loc_index = data_columns.index(locations.lower())
    except:
        loc_index = -1
    x= np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(model.predict([x])[0],2)


def get_location_names():
    return locations

def load_saved_artifacts():
    global data_columns
    global locations
    global model

    print("Loading saved.....start")
    
    # Load column data
    with open("./columns.json", 'r') as f:
        data_columns = json.load(f)['data_columns']
        locations = data_columns[3:]
    
    # Load the model
    global model
    with open("./banglore_home_prices_model.pickle", 'rb') as f:
        model = pickle.load(f)
    
    print("Loading saved .....done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimate_price('1st Phase JP Nagar',2000, 2, 2))