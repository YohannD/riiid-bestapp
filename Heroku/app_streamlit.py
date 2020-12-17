import os
import pandas as pd
import streamlit as st
import time
import random
from Heroku.data import get_data

df = get_data()

random_beginner = df['Random']
random_intermediate = df['Random ']
random_average = df['Random  ']
random_fluent = df['Random   ']

sorted_beginner = df['Sorted']
sorted_intermediate = df['Sorted ']
sorted_average = df['Sorted  ']
sorted_fluent = df['Sorted   ']

kt_beginner = df['Knowledge Tracing']
kt_intermediate = df['Knowledge Tracing ']
kt_average = df['Knowledge Tracing  ']
kt_fluent = df['Knowledge Tracing   ']
#lool

def main():
    
    analysis = st.sidebar.radio("Chose type of user", \
        ["Je sors de ma grotte et je veux aller à Cardiff", \
        "J'ai poncé Shakespeare mais j'ai jamais quitté la Lozère", \
        "I can order 2 pints after 10PM", "LMA"])
    
    st.markdown("# Welcome to our Riiid project")
    st.markdown("** Our user's English proficiency level is estimated as follows: **")

        
    if analysis == "Je sors de ma grotte et je veux aller à Cardiff":

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
        
        st.header("TOEIC score predictions")

        cols_model = st.beta_columns(4)

        if cols_model[0].checkbox('Textbook sorted'):
            selected_models.append(sorted_beginner)
        if cols_model[1].checkbox('Textbook random'):
            selected_models.append(random_beginner)
        if cols_model[2].checkbox('Knowledge Tracing'):
            selected_models.append(kt_beginner)
        cols_model[3].checkbox('Reinforcement Learning XGK+ Ultra')

 
    if analysis == "J'ai poncé Shakespeare mais j'ai jamais quitté la Lozère":
        
        
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
        
        st.header("TOEIC score predictions")

        cols_model = st.beta_columns(4)

        if cols_model[0].checkbox('Textbook sorted'):
            selected_models.append(sorted_intermediate)
        if cols_model[1].checkbox('Textbook random'):
            selected_models.append(random_intermediate)
        if cols_model[2].checkbox('Knowledge Tracing'):
            selected_models.append(kt_intermediate)
        cols_model[3].checkbox('Reinforcement Learning XGK+ Ultra')


    if analysis == "I can order 2 pints after 10PM":
        
        
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
        
        st.header("TOEIC score predictions")

        cols_model = st.beta_columns(4)

        if cols_model[0].checkbox('Textbook sorted'):
            selected_models.append(sorted_average)
        if cols_model[1].checkbox('Textbook random'):
            selected_models.append(random_average)
        if cols_model[2].checkbox('Knowledge Tracing'):
            selected_models.append(kt_average)
        cols_model[3].checkbox('Reinforcement Learning XGK+ Ultra')


    if analysis == "LMA":
        
        
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
        
        st.header("TOEIC score predictions")

        cols_model = st.beta_columns(4)

        if cols_model[0].checkbox('Textbook sorted'):
            selected_models.append(sorted_fluent)
        if cols_model[1].checkbox('Textbook random'):
            selected_models.append(random_fluent)
        if cols_model[2].checkbox('Knowledge Tracing'):
            selected_models.append(kt_fluent)
        cols_model[3].checkbox('Reinforcement Learning XGK+ Ultra')

    if st.button('Start', False):

        st.line_chart(pd.concat(selected_models, axis=1, ignore_index=False, \
            names=['Textbook sorted', 'Textbook random', 'Knowledge Tracing']))

if __name__ == "__main__":
    main()