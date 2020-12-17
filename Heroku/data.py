import pandas as pd
from google.cloud import storage
from Heroku.params import BUCKET_NAME, BUCKET_TRAIN_DATA_PATH
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier

def get_train_data(type='random',nrows=20000, local=False, **kwargs):
    """method to get the training data (or a portion of it) from google cloud bucket"""
    # Add Client() here
    client = storage.Client()

    if type=='random':
        if local:
            path = '/Users/Yohann/code/YohannD/riiid-project/notebooks/sequence_random.csv'
            df_train_random = pd.read_csv(path)
        else:
            path = 'gs://riiid-project/data/sequence_random.csv'
            df_train_random = pd.read_csv(path)
        return df_train_random

    if type=='sorted':
        if local:
            path = '/Users/Yohann/code/YohannD/riiid-project/notebooks/sequence_sorted.csv'  
            df_train_random = pd.read_csv(path)
        else:
            path = 'gs://riiid-project/data/sequence_sorted.csv'
            df_train_random = pd.read_csv(path)
        return df_train_random

def get_test_data(local=False):
    client = storage.Client()

    if local:
        path = '/Users/Yohann/code/YohannD/riiid-project/notebooks/toeic_question.csv'
        df_test = pd.read_csv(path)
    else:
        path = 'gs://riiid-project/data/toeic_question.csv'
        df_test = pd.read_csv(path)
    return df_test

def get_qstats(local=False):
    if local:
        path= '/Users/Yohann/code/YohannD/riiid-project/data/qstats_for_M1'
        qstats = pd.read_csv(path)
    else:
        path= 'gs://riiid-project/data/qstats_for_M1'
        qstats = pd.read_csv(path)
    return qstats

def clean_df(df, test=False):
    df = df.dropna(how='any', axis='rows')
    return df


def df_optimized(df, verbose=True, **kwargs):
    """
    Reduces size of dataframe by downcasting numeircal columns
    :param df: input dataframe
    :param verbose: print size reduction if set to True
    :param kwargs:
    :return:
    """
    in_size = df.memory_usage(index=True).sum()
    for type in ["float", "integer"]:
        l_cols = list(df.select_dtypes(include=type))
        for col in l_cols:
            df[col] = pd.to_numeric(df[col], downcast=type)
            if type == "float":
                df[col] = pd.to_numeric(df[col], downcast="integer")
    out_size = df.memory_usage(index=True).sum()
    ratio = (1 - round(out_size / in_size, 2)) * 100
    GB = out_size / 1000000000
    if verbose:
        print("optimized size by {} % | {} GB".format(ratio, GB))
    return df

def get_pipeline_features_list(local=False):
    if local:
        path= '/Users/Yohann/code/YohannD/riiid-project/models/xgboost_pipe_M1_features_list'
        pipeline_features_list = pd.DataFrame(path)
    else:
        path= 'gs://riiid-project/data/xgboost_pipe_M1_features_list'
        pipeline_features_list = pd.DataFrame(path)
    return pipeline_features_list



def infer_dtypes(path):
    """
    infer optimized dtypes for dataframe future dataframe csv loading
    :param path:
    :return: dict {"colname": dtype} to pass as argument to pd.read_csv
    """
    df = pd.read_csv(path, nrows=100)
    df_opt = df_optimized(df, verbose=False)
    dtypes = df_opt.dtypes
    colnames = dtypes.index
    types = [i.name for i in dtypes.values]
    column_types = dict(zip(colnames, types))
    return column_types



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
