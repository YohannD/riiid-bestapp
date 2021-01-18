import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import make_pipeline
import seaborn as sns
import streamlit as st
import time
import random
import matplotlib.pyplot as plt
from Heroku.utils import *
from Heroku.data import *


#@st.cach


def main():
    
    st.markdown("# Welcome to our Riiid project")
    st.markdown("## What is your English proficiency level?")
    st.markdown("### Scale")
    st.markdown("0: Beginner | 1: Intermediate | 2: Upper Intermediate | 3: Advanced")
    
    option = st.sidebar.selectbox("Select a student", ["My student", "Beginner", "Bookworm", "Intermediate", "Fluent"])
    pipeline, features_list, qstats, df_random, df_textbook, questions = get_data()

    if option == "My student":
        selected_models = []
        initial_experience = []

        st.markdown('<b class="material-icons">Listening Skills</b>', unsafe_allow_html=True)
        cols_level = st.beta_columns(4)
        score_1 = cols_level[0].number_input('Photographs', 0, 3, 0)
        score_2 = cols_level[1].number_input('Q&A', 0, 3, 0)
        score_3 = cols_level[2].number_input('Short Convs', 0, 3, 0)
        score_4 = cols_level[3].number_input('Long Convs', 0, 3, 0)
        st.markdown('<b class="material-icons">Reading Skills</b>', unsafe_allow_html=True)
        cols_level_2 = st.beta_columns(3)
        score_5 = cols_level_2[0].number_input('Sentences', 0, 3, 0)
        score_6 = cols_level_2[1].number_input('Single Texts', 0, 3, 0)
        score_7 = cols_level_2[2].number_input('Double Texts', 0, 3, 0)

        initial_experience.append(score_1)
        initial_experience.append(score_2)
        initial_experience.append(score_3)
        initial_experience.append(score_4)
        initial_experience.append(score_5)
        initial_experience.append(score_6)
        initial_experience.append(score_7)

        st.header("Learning Mode")

        cols_model = st.beta_columns(5)

        if cols_model[0].checkbox('Textbook 📚'):
            sorted_beginner = plot_learning_curve(pipeline, features_list, qstats, initial_experience=initial_experience,
                training_question_selection_strategy='textbook', number_students=2)
            selected_models.append(sorted_beginner)
        if cols_model[1].checkbox('Random 🔁'):
            random_beginner = plot_learning_curve(pipeline, features_list, qstats, initial_experience=initial_experience,
                training_question_selection_strategy='random')
            selected_models.append(random_beginner)
        if cols_model[2].checkbox('Sadist Teacher 👨‍🏫'):
            sadist_beginner = plot_learning_curve(pipeline, features_list, qstats, initial_experience=initial_experience,
                training_question_selection_strategy='sadist_coach')
            selected_models.append(sadist_beginner)    
        if cols_model[3].checkbox('Knowledge Tracing 📲'):
            kt_beginner = plot_learning_curve(pipeline, features_list, qstats, initial_experience=initial_experience,
                training_question_selection_strategy='knowledge_tracing')
            selected_models.append(kt_beginner)
        if cols_model[4].checkbox('Reinforcement Learning + Ultra 🔥'):
            st.image(image, caption='To be continued', use_column_width=False)


    if option == "Beginner":

        st.sidebar.text_area("Profile", "Hello World 🌍")

        selected_models = []        

        initial_experience = [0, 0, 0, 0, 0, 0, 0]
        cols_level = st.beta_columns(7)
        cols_level[0].text_input('Photographs', initial_experience[0])
        cols_level[1].text_input('Q&A', initial_experience[1])
        cols_level[2].text_input('Short Convs', initial_experience[2])
        cols_level[3].text_input('Long Convs', initial_experience[3])
        cols_level[4].text_input('Sentences', initial_experience[4])
        cols_level[5].text_input('Single Texts', initial_experience[5])
        cols_level[6].text_input('Double Texts', initial_experience[6])

        st.header("Learning Mode")

        cols_model = st.beta_columns(5)

        if cols_model[0].checkbox('Textbook 📚'):
            sorted_beginner = plot_learning_curve(pipeline, features_list, qstats, initial_experience=initial_experience,
                training_question_selection_strategy='textbook', number_students=2)
            selected_models.append(sorted_beginner)
        if cols_model[1].checkbox('Random 🔁'):
            random_beginner = plot_learning_curve(pipeline, features_list, qstats, initial_experience=initial_experience,
                training_question_selection_strategy='random')
            selected_models.append(random_beginner)
        if cols_model[2].checkbox('Sadist Teacher 👨‍🏫'):
            sadist_beginner = plot_learning_curve(pipeline, features_list, qstats, initial_experience=initial_experience,
                training_question_selection_strategy='sadist_coach')
            selected_models.append(sadist_beginner)    
        if cols_model[3].checkbox('Knowledge Tracing 📲'):
            kt_beginner = plot_learning_curve(pipeline, features_list, qstats, initial_experience=initial_experience,
                training_question_selection_strategy='knowledge_tracing')
            selected_models.append(kt_beginner)
        if cols_model[4].checkbox('Reinforcement Learning + Ultra 🔥'):
            st.image(image, caption='To be continued', use_column_width=False)

    if option == "Bookworm":

        st.sidebar.text_area("Profile", "I've read all of Shakespeare's works but never left Lozère 🐛📚")
        
        selected_models = []

        cols_level = st.beta_columns(7)

        initial_experience = [0, 0, 0, 0, 3, 3, 3]

        cols_level[0].text_input('Photographs', initial_experience[0])
        cols_level[1].text_input('Q&A', initial_experience[1])
        cols_level[2].text_input('Short Convs', initial_experience[2])
        cols_level[3].text_input('Long Convs', initial_experience[3])
        cols_level[4].text_input('Sentences', initial_experience[4])
        cols_level[5].text_input('Single Texts', initial_experience[5])
        cols_level[6].text_input('Double Texts', initial_experience[6])
        
        st.header("Learning Mode")

        cols_model = st.beta_columns(5)

        if cols_model[0].checkbox('Textbook 📚'):
            sorted_intermediate = plot_learning_curve(pipeline, features_list, qstats, initial_experience=initial_experience,
                training_question_selection_strategy='textbook', number_students=2)
            selected_models.append(sorted_intermediate)
        if cols_model[1].checkbox('Random 🔁'):
            random_intermediate = plot_learning_curve(pipeline, features_list, qstats, initial_experience=initial_experience,
                training_question_selection_strategy='random', number_students=2)
            selected_models.append(random_intermediate)
        if cols_model[2].checkbox('Sadist Teacher 👨‍🏫'):
            sadist_intermediate = plot_learning_curve(pipeline, features_list, qstats, initial_experience=initial_experience,
                training_question_selection_strategy='sadist_coach', number_students=2)
            selected_models.append(sadist_intermediate)
        if cols_model[3].checkbox('Knowledge Tracing 📲'):
            kt_intermediate = plot_learning_curve(pipeline, features_list, qstats, initial_experience=initial_experience,
                training_question_selection_strategy='knowledge_tracing', number_students=2)
            selected_models.append(kt_intermediate)
        if cols_model[4].checkbox('Reinforcement Learning + Ultra 🔥'):
            st.image(image, caption='To be continued', use_column_width=False)

    if option == "Intermediate":
        
        st.sidebar.text_area("Profile", "I can order 2 pints after 10PM 🍻")
        
        selected_models = []

        cols_level = st.beta_columns(7)

        initial_experience = [2, 2, 2, 2, 2, 2, 2]


        cols_level[0].text_input('Photographs', initial_experience[0])
        cols_level[1].text_input('Q&A', initial_experience[1])
        cols_level[2].text_input('Short Convs', initial_experience[2])
        cols_level[3].text_input('Long Convs', initial_experience[3])
        cols_level[4].text_input('Sentences', initial_experience[4])
        cols_level[5].text_input('Single Texts', initial_experience[5])
        cols_level[6].text_input('Double Texts', initial_experience[6])
        
        st.header("Learning Mode")

        cols_model = st.beta_columns(5)

        if cols_model[0].checkbox('Textbook 📚'):
            sorted_average = plot_learning_curve(pipeline, features_list, qstats, initial_experience=initial_experience,
                training_question_selection_strategy='textbook', number_students=2)
            selected_models.append(sorted_average)
        if cols_model[1].checkbox('Random 🔁'):
            random_average = plot_learning_curve(pipeline, features_list, qstats, initial_experience=initial_experience,
                training_question_selection_strategy='random', number_students=2)
            selected_models.append(random_average)
        if cols_model[2].checkbox('Sadist Teacher 👨‍🏫'):
            sadist_average = plot_learning_curve(pipeline, features_list, qstats, initial_experience=initial_experience,
                training_question_selection_strategy='sadist_coach', number_students=2)
            selected_models.append(sadist_average)
        if cols_model[3].checkbox('Knowledge Tracing 📲'):
            kt_average = plot_learning_curve(pipeline, features_list, qstats, initial_experience=initial_experience,
                training_question_selection_strategy='knowledge_tracing', number_students=2)
            selected_models.append(kt_average)
        if cols_model[4].checkbox('Reinforcement Learning + Ultra 🔥'):
            st.image(image, caption='To be continued', use_column_width=False)

    if option == "Fluent":
        
        st.sidebar.text_area("Profile", "The perfect guy 👱")
        
        selected_models = []

        cols_level = st.beta_columns(7)

        initial_experience = [3, 3, 3, 3, 3, 3, 3]


        cols_level[0].text_input('Photographs', initial_experience[0])
        cols_level[1].text_input('Q&A', initial_experience[1])
        cols_level[2].text_input('Short Convs', initial_experience[2])
        cols_level[3].text_input('Long Convs', initial_experience[3])
        cols_level[4].text_input('Sentences', initial_experience[4])
        cols_level[5].text_input('Single Texts', initial_experience[5])
        cols_level[6].text_input('Double Texts', initial_experience[6])

        st.header("Learning Mode")

        cols_model = st.beta_columns(5)

        if cols_model[0].checkbox('Textbook 📚'):
            sorted_fluent = plot_learning_curve(pipeline, features_list, qstats, initial_experience=initial_experience,
                training_question_selection_strategy='textbook', number_students=2)
            selected_models.append(sorted_fluent)
        if cols_model[1].checkbox('Random 🔁'):
            random_fluent = plot_learning_curve(pipeline, features_list, qstats, initial_experience=initial_experience,
                training_question_selection_strategy='random', number_students=2)
            selected_models.append(random_fluent)
        if cols_model[2].checkbox('Sadist Teacher 👨‍🏫'):
            sadist_fluent = plot_learning_curve(pipeline, features_list, qstats, initial_experience=initial_experience,
                training_question_selection_strategy='sadist_coach', number_students=2)
            selected_models.append(sadist_fluent)
        if cols_model[3].checkbox('Knowledge Tracing 📲'):
            kt_fluent = plot_learning_curve(pipeline, features_list, qstats, initial_experience=initial_experience,
                training_question_selection_strategy='knowledge_tracing', number_students=2)
            selected_models.append(kt_fluent)
        if cols_model[4].checkbox('Reinforcement Learning + Ultra 🔥'):
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

        results_df = pd.Series(range(0, 105 , 5), name='caramel')
        selected_models.append(results_df)
        concat = pd.concat(selected_models, axis=1).set_index('caramel')
        st.line_chart(concat)

if __name__ == "__main__":
    main()