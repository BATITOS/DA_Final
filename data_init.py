import pandas as pd

def create_anime_df(file):
   df = pd.read_csv(file)
   
   return df

def find_data(file,id):
    user_data = pd.read_csv(file)
    y_train = None
    
    return user_data, y_train
    