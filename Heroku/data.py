import pandas as pd

path = 'Heroku/data/data.csv'

def get_data():
    df = pd.read_csv(path)
    df = df.set_index('days')
    return df