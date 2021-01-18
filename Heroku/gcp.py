import json
import os
import joblib
from google.cloud import storage
from google.oauth2 import service_account
from termcolor import colored
import pickle
from Heroku.params import *


def get_credentials():
    credentials_raw = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    if '.json' in credentials_raw:
        credentials_raw = open(credentials_raw).read()
    creds_json = json.loads(credentials_raw)
    creds_gcp = service_account.Credentials.from_service_account_info(creds_json)
    return creds_gcp


def storage_upload(model_version=MODEL_VERSION, bucket=BUCKET_NAME, rm=False):
    client = storage.Client().bucket(bucket)

    storage_location = 'models/{}/versions/{}/{}'.format(
        MODEL_NAME,
        model_version,
        'model.joblib')
    blob = client.blob(storage_location)
    blob.upload_from_filename('model.joblib')
    print(colored("=> model.joblib uploaded to bucket {} inside {}".format(BUCKET_NAME, storage_location),
                  "green"))
    if rm:
        os.remove('model.joblib')


def download_model(model_version=MODEL_VERSION, bucket=BUCKET_NAME, rm=True):
    creds = get_credentials()
    client = storage.Client(credentials=creds, project=PROJECT_ID).bucket(bucket)

    storage_location = '{}'.format(
        MODEL_NAME)
    blob = client.blob(storage_location)
    blob.download_to_filename('model.pkl')
    print(f"=> pipeline downloaded from storage")
    model = pickle.load(open('model.pkl', 'rb'))
    if rm:
        os.remove('model.pkl')
    return model