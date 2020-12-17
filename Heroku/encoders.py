from os.path import split
import pandas as pd
import numpy as np
from Heroku.data import df_optimized, get_data, clean_df
import pygeohash as gh
import Heroku

folder_source, _ = split(Heroku.__file__)

if __name__ == "__main__":
    params = dict(nrows=1000,
                  upload=False,
                  local=False,  # set to False to get data from GCP (Storage or BigQuery)
                  optimize=False)
    df = get_data(**params)
    df = clean_df(df)
  