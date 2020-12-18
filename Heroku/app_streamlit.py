import os
import pandas as pd
import streamlit as st
import time
import random
from Heroku.data import get_data
from PIL import Image

df = get_data()
image = Image.open('data/under_construction.png')

random_beginner = df['Random']
random_intermediate = df['Random ']
random_average = df['Random  ']
random_fluent = df['Random   ']

sorted_beginner = df['Textbook']
sorted_intermediate = df['Textbook ']
sorted_average = df['Textbook  ']
sorted_fluent = df['Textbook   ']

sadist_beginner = df['Sadist Teacher']
sadist_intermediate = df['Sadist Teacher ']
sadist_average = df['Sadist Teacher  ']
sadist_fluent = df['Sadist Teacher   ']

kt_beginner = df['Knowledge Tracing']
kt_intermediate = df['Knowledge Tracing ']
kt_average = df['Knowledge Tracing  ']
kt_fluent = df['Knowledge Tracing   ']

@st.cache
def read_data(n_rows=10000):
    df_train_sorted = get_train_data(type='sorted' ,n_rows=n_rows, local=True)
    df_train_random = get_train_data(type='random', n_rows=n_rows, local=True)
    df_test = get_test_data(local=True)
    qstats = get_qstats(local=True)
    return df_train_sorted, df_train_random, df_test, qstats


def main():
    

    st.markdown("# Welcome to our Riiid project")
    st.markdown("** Educational technology **")
    option = st.sidebar.selectbox("Select a sudent", ["", "Beginner", "Bookworm", "Intermediate", "Fluent"])
        
    if option == "Beginner":

        st.sidebar.text_area("Profile", "Hello World")

        selected_models = []        

        cols_level = st.beta_columns(7)

        score_1 = 0
        score_2 = 0
        score_3 = 0
        score_4 = 0
        score_5 = 0
        score_6 = 0
        score_7 = 0

        cols_level[0].text_input('Photographs', score_1)
        cols_level[1].text_input('Q&A', score_2)
        cols_level[2].text_input('Short Convs', score_3)
        cols_level[3].text_input('Long Convs', score_4)
        cols_level[4].text_input('Sentences', score_5)
        cols_level[5].text_input('Single Texts', score_6)
        cols_level[6].text_input('Double Texts', score_7)
        
        st.header("Learning Mode 📚 👨‍🏫 📲 🔥")

        cols_model = st.beta_columns(5)

        if cols_model[0].checkbox('Textbook'):
            selected_models.append(sorted_beginner)
        if cols_model[1].checkbox('Random'):
            selected_models.append(random_beginner)
        if cols_model[2].checkbox('Sadist Teacher'):
            selected_models.append(sadist_beginner)    
        if cols_model[3].checkbox('Knowledge Tracing'):
            selected_models.append(kt_beginner)
        if cols_model[4].checkbox('Reinforcement Learning XGK+ Ultra'):
            st.image(image, caption='To be continued', use_column_width=False)
 
    if option == "Bookworm":

        st.sidebar.text_area("Profile", "I've read all of Shakespeare's works but never left Lozère")
        
        selected_models = []

        cols_level = st.beta_columns(7)

        score_1 = 2
        score_2 = 2
        score_3 = 2
        score_4 = 2
        score_5 = 9
        score_6 = 9
        score_7 = 9

        cols_level[0].text_input('Photographs', score_1)
        cols_level[1].text_input('Q&A', score_2)
        cols_level[2].text_input('Short Convs', score_3)
        cols_level[3].text_input('Long Convs', score_4)
        cols_level[4].text_input('Sentences', score_5)
        cols_level[5].text_input('Single Texts', score_6)
        cols_level[6].text_input('Double Texts', score_7)
        
        st.header("Learning Mode 📚 👨‍🏫 📲 🔥")

        cols_model = st.beta_columns(5)

        if cols_model[0].checkbox('Textbook'):
            selected_models.append(sorted_intermediate)
        if cols_model[1].checkbox('Random'):
            selected_models.append(random_intermediate)
        if cols_model[2].checkbox('Sadist Teacher'):
            selected_models.append(sadist_intermediate)
        if cols_model[3].checkbox('Knowledge Tracing'):
            selected_models.append(kt_intermediate)
        if cols_model[4].checkbox('Reinforcement Learning XGK+ Ultra'):
            st.image(image, caption='To be continued', use_column_width=False)

    if option == "Intermediate":
        
        st.sidebar.text_area("Profile", "I can order 2 pints after 10PM")
        
        selected_models = []

        cols_level = st.beta_columns(7)

        score_1 = 5
        score_2 = 5
        score_3 = 5
        score_4 = 5
        score_5 = 5
        score_6 = 5
        score_7 = 5

        cols_level[0].text_input('Photographs', score_1)
        cols_level[1].text_input('Q&A', score_2)
        cols_level[2].text_input('Short Convs', score_3)
        cols_level[3].text_input('Long Convs', score_4)
        cols_level[4].text_input('Sentences', score_5)
        cols_level[5].text_input('Single Texts', score_6)
        cols_level[6].text_input('Double Texts', score_7)
        
        st.header("Learning Mode 📚 👨‍🏫 📲 🔥")

        cols_model = st.beta_columns(5)

        if cols_model[0].checkbox('Textbook'):
            selected_models.append(sorted_average)
        if cols_model[1].checkbox('Random'):
            selected_models.append(random_average)
        if cols_model[2].checkbox('Sadist Teacher'):
            selected_models.append(sadist_average)
        if cols_model[3].checkbox('Knowledge Tracing'):
            selected_models.append(kt_average)
        if cols_model[4].checkbox('Reinforcement Learning XGK+ Ultra'):
            st.image(image, caption='To be continued', use_column_width=False)

    if option == "Fluent":
        
        st.sidebar.text_area("Profile", "The perfect guy 👱")
        
        selected_models = []

        cols_level = st.beta_columns(7)

        score_1 = 10
        score_2 = 10
        score_3 = 10
        score_4 = 10
        score_5 = 10
        score_6 = 10
        score_7 = 10

        cols_level[0].text_input('Photographs', score_1)
        cols_level[1].text_input('Q&A', score_2)
        cols_level[2].text_input('Short Convs', score_3)
        cols_level[3].text_input('Long Convs', score_4)
        cols_level[4].text_input('Sentences', score_5)
        cols_level[5].text_input('Single Texts', score_6)
        cols_level[6].text_input('Double Texts', score_7)

        st.header("Learning Mode 📚 👨‍🏫 📲 🔥")

        cols_model = st.beta_columns(5)

        if cols_model[0].checkbox('Textbook'):
            selected_models.append(sorted_fluent)
        if cols_model[1].checkbox('Random'):
            selected_models.append(random_fluent)
        if cols_model[2].checkbox('Sadist Teacher'):
            selected_models.append(random_fluent)
        if cols_model[3].checkbox('Knowledge Tracing'):
            selected_models.append(kt_fluent)
        if cols_model[4].checkbox('Reinforcement Learning XGK+ Ultra'):
            st.image(image, caption='To be continued', use_column_width=False)

    if st.button('Start', False):

        st.checkbox('Stop')

        'Starting a long computation...'

        latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(100):
            
            latest_iteration.text(f'Training for {i+1} days')
            bar.progress(i + 1)
            time.sleep(0.02)


        st.header("🎓 TOEIC probability of success")
        st.line_chart(pd.concat(selected_models, axis=1, ignore_index=False, \
            names=['Textbook sorted', 'Textbook random', 'Knowledge Tracing']))

if __name__ == "__main__":
    main()