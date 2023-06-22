import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):  # function of model to predict price

    try:
        loc_index = __data_columns.index(location.lower()) # converts locations into lower case
    except:
        loc_index = -1  # if not found locations return -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath            # these are arguments to predict price
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)  # round price value upto 2 decimal numbers

def load_saved_artifacts():
    print("loading saved artifacts.......start")
    global __data_columns
    global __locations
                                                      # r for read in here
    with open("./artifacts/columns.json", "r") as f:  # read columns from json file and store it in 'f' object
        __data_columns = json.load(f)['data_columns']  # loading all columns in 'f' into __data_columns variable
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk, so skip these
                                          # and we want other columns which are location names

        global __model
        if __model is None:
            with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f: # read pickle file into 'f' object and 'rb' stands for read binary in here as it's a binary file
                __model = pickle.load(f)   # laod model in f obj into __model variable
        print("loading saved artifacts...done")

def get_location_names():
    return __locations  # all columns skipping first three, only contains locations

def get_data_columns():
    return __data_columns  # all columns in json file



if __name__ == '__main__':  # 3 types of functions/routines called
    load_saved_artifacts()
    print(get_location_names())

    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 2))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))  # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location