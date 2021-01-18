
### GCP configuration - - - - - - - - - - - - - - - - - - -

# /!\ you should fill these according to your account

### GCP Project - - - - - - - - - - - - - - - - - - - - - -

PROJECT_ID = "speedy-area-297510"

### GCP Storage - - - - - - - - - - - - - - - - - - - - - -

BUCKET_NAME = 'riiid-project'

##### Data  - - - - - - - - - - - - - - - - - - - - - - - -

# train data file location
# /!\ here you need to decide if you are going to train using the provided and uploaded data/train_1k.csv sample file
# or if you want to use the full dataset (you need need to upload it first of course)
QSTATS_DATA_PATH = 'data/qstats_for_M1'
RANDOM_DATA_PATH = 'data/sequence_random.csv'
TEXTBOOK_DATA_PATH = 'data/sequence_sorted.csv'
QUESTIONS_DATA_PATH = 'data/toeic_question.csv'
FEATURES_DATA_PATH = 'data/xgboost_pipe_M1_features_list'

##### Model - - - - - - - - - - - - - - - - - - - - - - - -

# model folder name (will contain the folders for all trained model versions)
MODEL_NAME = 'models/xgboost_pipe_M1.pkl'

# model version folder name (where the trained model.joblib file will be stored)
MODEL_VERSION = 'Pipeline'