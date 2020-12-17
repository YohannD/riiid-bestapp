from datetime import datetime
import joblib
import pandas as pd
import pytz
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import make_pipeline
import seaborn as sns
import streamlit as st
import time
import random
from Heroku.utils import user_history_update, pred_answers
import pickle
import random
from Heroku.data import *
from scipy import misc


txt_sorted_model = pred_answers(loop_length=100, question_selection_strategy='sorted')
txt_random_model = pred_answers(loop_length=100, question_selection_strategy='random')
k_tracing_model = pred_answers(loop_length=100, question_selection_strategy='k_tracing')
y_sorted = pd.Series(txt_sorted_model['user_avg_score_cum'])
y_random = pd.Series(txt_random_model['user_avg_score_cum'])
y_k_tracing = pd.Series(k_tracing_model['user_avg_score_cum'])


@st.cache
def read_data(n_rows=10000):
    df_train_sorted = get_train_data(type='sorted' ,n_rows=n_rows, local=False)
    df_train_random = get_train_data(type='random', n_rows=n_rows, local=False)
    df_test = get_test_data(local=False)
    qstats = get_qstats(local=False)
    return df_train_sorted, df_train_random, df_test, qstats


def main():
    
    analysis = st.sidebar.radio("Chose type of user", ["Je sors de ma grotte et je veux aller à Cardiff", "J'ai poncé Shakespeare mais j'ai jamais quitté la Lozère", "I can order 2 pints after 10PM", "LMA"])
    #if analysis == "Dataviz":
    #    st.header("Riiid Project Basic Data Visualisation")
    #    st.markdown("**Have fun immplementing your own Riiid project Dataviz**")

    #    data     = read_data(n_rows=1000)
    #    df = data.copy()
    #    st.write(df.head(10))

        
    #    filtered_df = df[df['passenger_count'] == passengers]
    #    st.write(filtered_df.head(10))

    #    st.bar_chart(df['passenger_count'].value_counts())


    #    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
    #    df['date'] = df['pickup_datetime'].dt.date
    #    df_2014 = df[df['pickup_datetime'] == 2014]
    #    grouped = df_2014.date.value_counts().sort_index() 
    #    st.line_chart(grouped)

        #st.write(trips)

    if analysis == "Je sors de ma grotte et je veux aller à Cardiff":
        
        st.markdown("# ML Project")
        st.markdown("** Welcome to our Riiid project **")

        loop_length=10000
        question_selection_strategy='random'
        days=100
        user_history=None
        selected_models = []

        cols_level = st.beta_columns(7)

        score_1 = 0.5
        score_2 = 0.5
        score_3 = 0.5
        score_4 = 0.5
        score_5 = 0.5
        score_6 = 0.5
        score_7 = 0.5

        cols_level[0].text_input('Photographs', score_1)
        cols_level[1].text_input('Q&A', score_2)
        cols_level[2].text_input('Short Convs', score_3)
        cols_level[3].text_input('Talk', score_4)
        cols_level[4].text_input('Sentences', score_5)
        cols_level[5].text_input('Single Texts', score_6)
        cols_level[6].text_input('Double Texts', score_7)

        placeholder = st.empty()
        start_button = st.empty()
        chart_button = st.empty()
        bar = st.progress(0)
        
        st.header("TOEIC score predictions")

        cols_model = st.beta_columns(4)

        if cols_model[0].checkbox('Textbook sorted'):
            selected_models.append(y_sorted)
        if cols_model[1].checkbox('Textbook random'):
            selected_models.append(y_random)
        if cols_model[2].checkbox('Knowledge Tracing'):
            selected_models.append(y_k_tracing)
        cols_model[3].checkbox('Reinforcement Learning XGK+ Ultra')        


        if st.button('Start', False):

            #x_sorted = txt_sorted_model['user_activity_cumcount']
            #x_random = txt_random_model['user_activity_cumcount']
            #x_k_tracing = k_tracing_model['user_activity_cumcount']
            #training_days = 100

            st.line_chart(pd.concat(selected_models, axis=1, ignore_index=True, names=['Textbook sorted', 'Textbook random', 'Knowledge Tracing']))
            #st.line_chart(y_random)
            #st.line_chart(y_k_tracing)

        # print(colored(proc.sf_query, "blue"))
        # proc.test_execute()
if __name__ == "__main__":
    #df_train_sorted, df_train_random, df_test, qstats = read_data()
    main()
            #main()
##