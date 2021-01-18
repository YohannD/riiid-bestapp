import pandas as pd
from Heroku.gcp import get_credentials
from google.cloud import storage
from Heroku.params import *
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier
from Heroku.gcp import *
import pickle

creds = get_credentials()

def get_data(local=False):
    client = storage.Client()
    if local:
        pipeline = pickle.load(open('heroku/Heroku/data/xgboost_pipe_M1.pkl', 'rb'))
        pipeline_features_list = pd.read_csv('heroku/Heroku/data/xgboost_pipe_M1_features_list')
        qstats = pd.read_csv('heroku/Heroku/data/qstats_for_M1')
        df_random = pd.read_csv('heroku/Heroku/data/sequence_random.csv')
        df_textbook = pd.read_csv('heroku/Heroku/data/sequence_sorted.csv')
        questions = pd.read_csv('heroku/Heroku/data/toeic_question.csv')
    else:
        pipeline = download_model()
        pipeline_features_list = pd.read_csv("gs://{}/{}".format(BUCKET_NAME, FEATURES_DATA_PATH))
        qstats = pd.read_csv("gs://{}/{}".format(BUCKET_NAME, QSTATS_DATA_PATH))
        questions = pd.read_csv("gs://{}/{}".format(BUCKET_NAME, QUESTIONS_DATA_PATH))
        df_random = pd.read_csv("gs://{}/{}".format(BUCKET_NAME, RANDOM_DATA_PATH))
        df_textbook = pd.read_csv("gs://{}/{}".format(BUCKET_NAME, TEXTBOOK_DATA_PATH))
    return pipeline, pipeline_features_list, qstats, df_random, df_textbook, questions

def clean_df(df, test=False):
    df = df.dropna(how='any', axis='rows')
    return df

if __name__ == "__main__":
    params = dict(nrows=10000000,
                  upload=False,
                  local=True,  # set to False to get data from GCP (Storage or BigQuery)
                  optimize=True)
    df = get_data(**params)
    params["optimize"] = False
    df_2 = get_data(**params)
    m1 = df.memory_usage().sum()/1000000
    m2 = df_2.memory_usage().sum()/1000000
    print(m1, m2, m1 / m2)
    mm = pd.merge(df, df_2, on="key")