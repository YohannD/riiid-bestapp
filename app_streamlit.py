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
import matplotlib.pyplot as plt
from Heroku.utils import user_history_update, pred_answers
import pickle
import random
from Heroku.data import *
import matplotlib.pyplot as plt
from scipy import misc

pipeline_features_list=pd.read_csv('/Users/Yohann/code/YohannD/riiid-project/models/xgboost_pipe_M1_features_list')
txt_sorted_model = pred_answers(loop_length=100, question_selection_strategy='sorted')
txt_random_model = pred_answers(loop_length=100, question_selection_strategy='random')
k_tracing_model = pred_answers(loop_length=100, question_selection_strategy='k_tracing')
y_sorted = pd.Series(txt_sorted_model['user_avg_score_cum'])
y_random = pd.Series(txt_random_model['user_avg_score_cum'])
y_k_tracing = pd.Series(k_tracing_model['user_avg_score_cum'])


@st.cache
def read_data(n_rows=10000):
    df_train_sorted = get_train_data(type='sorted' ,n_rows=n_rows, local=True)
    df_train_random = get_train_data(type='random', n_rows=n_rows, local=True)
    df_test = get_test_data(local=True)
    qstats = get_qstats(local=True)
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




        # inputs from user
        #reading_proficiency = st.text_input("Listening proficiency level:", "50%")
        #listening_proficiency = st.text_input("Reading proficiency level:", "50%")
        

        


        if st.button('Start', False):

            #x_sorted = txt_sorted_model['user_activity_cumcount']
            #x_random = txt_random_model['user_activity_cumcount']
            #x_k_tracing = k_tracing_model['user_activity_cumcount']
            #training_days = 100

            st.line_chart(pd.concat(selected_models, axis=1, ignore_index=True, names=['Textbook sorted', 'Textbook random', 'Knowledge Tracing']))
            #st.line_chart(y_random)
            #st.line_chart(y_k_tracing)


        

        ### Initialize the user to None or starting level ###
        

        # def radar_chart(days=days):

        #    for i in range(loop_length):
            ### CHOIX DE LA QUESTION ###
        #        if question_selection_strategy=='random':
        #            next_question_id=random.choice(qstats.content_id.to_list())
        
        
        #        user_history=user_history_update(0,
        #                                 next_question_id,
        #                                 qstats,
        #                                 user_history,
        #                                 prior_question_had_explanation=random.uniform(0, 1)>0.1)
                ### PREDICTION ###
        #        user_history.iloc[-1,-1]\
        #        = pipeline.predict_proba(user_history[pipeline_features_list.feature.to_list()].iloc[-2:-1])[0,1]
        #        part = range(7)
            
        #    df_part = user_history[['part', 'user_avg_score_cum_part1','user_avg_score_cum_part2','user_avg_score_cum_part3',
        #        'user_avg_score_cum_part4', 'user_avg_score_cum_part5', 'user_avg_score_cum_part6', 'user_avg_score_cum_part7']]
        #    fig = px.line_polar(data_frame=df_part.iloc[[-1]], r=part, theta=df_part.drop(columns='part').columns, line_close=True)
        #    placeholder.write(fig)

            #latest_session = st.empty()
        #    df_part = user_history[['part', 'user_avg_score_cum_part1','user_avg_score_cum_part2','user_avg_score_cum_part3',
        #        'user_avg_score_cum_part4', 'user_avg_score_cum_part5', 'user_avg_score_cum_part6', 'user_avg_score_cum_part7']]
        #    st.write(df_part)
        #    fig = px.line_polar(data_frame=df_part.iloc[[i]], r=df_part.part.unique()[1:], theta=df_part.drop(columns='part').columns, line_close=True)
        #        placeholder.write(fig)

        
        

                #bar.progress(1)

        #bars = alt.Chart(data).mark_bar().encode(
        #x=X('1:Q',axis=Axis(title='Your average score')),
        #y=Y('0:Q',axis=Axis(title='Model'))
        #).properties(
        #width=650, 
        #height=400
        #)

        #bar_plot = st.altair_chart(bars)
#

        # def plot_bar_animated_altair(df):
           #bars = alt.Chart(df, title="Score after some questions").encode(
            #x=X('user_activity_cumcount:Q',axis=Axis(title='Number of questions')), 
            #y=Y('user_avg_score_cum:Q',axis=Axis(title='Model'), sort='-x')
            #).properties(
                 #width=650, 
                 #height=400
           #)

        #st.dataframe(data)

                #bars = plot_bar_animated_altair(data)
                #time.sleep(0.01)

                #bar_plot.altair_chart(bars)

                #plot_url = py.plot(fig)


                #st.write(TEACHER_HTML, unsafe_allow_html=True)



            
                #time.sleep(0.1)

#                
#                #res = pipeline.predict(data[COLS])
                #st.write('💸 TOEIC Score:', res)
                #st.map(data=data)


        # print(colored(proc.sf_query, "blue"))
        # proc.test_execute()
if __name__ == "__main__":
    df_train_sorted, df_train_random, df_test, qstats = read_data()
    pipeline = pickle.load(open('/Users/Yohann/code/YohannD/riiid-project/models/xgboost_pipe_M1.pkl', 'rb'))
    main()
            #main()
##