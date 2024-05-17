# data_preprocessing.py
import pandas as pd

def preprocess_data(climatic_file, food_file):
    climatic_data = pd.read_csv(climatic_file)
    food_data = pd.read_csv(food_file)
    
    # Merge climatic and food data
    preprocessed_data = merge_data(climatic_data, food_data)
    
    # Encode categorical variables
    preprocessed_data = encode_categorical(preprocessed_data, ['location'])
    
    return preprocessed_data

def merge_data(climatic_data, food_data):
    # Merge climatic and food data
    merged_data = pd.merge(climatic_data, food_data, on=['year', 'location'])
    print(merged_data)
    return merged_data

def encode_categorical(data, columns):
    # One-hot encode categorical variables
    for column in columns:
        data = pd.get_dummies(data, columns=[column], drop_first=True)
    return data
