import time
import pandas as pd
import numpy as np
from Heroku.data import get_train_data, get_test_data, get_qstats, get_pipeline_features_list
import random
import pickle

pipeline = pickle.load(open('gs://riiid-project/models/xgboost_pipe_M1.pkl'))
df_train_sorted = get_train_data(type='sorted' , local=True)
df_train_random = get_train_data(type='random', local=True)
pipeline_features_list = get_pipeline_features_list(local=True)
df_test = get_test_data(local=True)
qstats = get_qstats(local=True)

def user_history_update(content_type_id,
                        content_id,
                        data_qstats,
                        user_history=None,
                        prior_question_had_explanation=False):
    '''Crée ou met à jour l'hisorique d'un utilisateur, stockée dans un df'''
    
    user_history_empty=pd.DataFrame({
                             #following columns are the impute of each loop
                             ### TO BE IMPUTED ###
                             'content_id':[-1],
                             'content_type_id':[-1],
                             'prior_question_had_explanation':False,
                             # following columns depend of previous history of the user : 
                             ### TO BE UPDATED WHATEVER THE CONTENT_TYPE ###
                             'user_activity_cumcount':[-1],
                             'at_least_one_lesson':[0],
                             ### TO BE UPDATED IF LAST WAS QUESTION , ELSE COPIED ###
                             'user_avg_score_cum':[0.499],
                             'user_correct_answers_cum':[0],
                             'user_avg_score_cum_part1':[0.499],
                             'user_avg_score_cum_part2':[0.499],
                             'user_avg_score_cum_part3':[0.499],
                             'user_avg_score_cum_part4':[0.499],
                             'user_avg_score_cum_part5':[0.499],
                             'user_avg_score_cum_part6':[0.499],
                             'user_avg_score_cum_part7':[0.499],
                             'user_correct_answers_cum_part1':[0],
                             'user_correct_answers_cum_part2':[0],
                             'user_correct_answers_cum_part3':[0],
                             'user_correct_answers_cum_part4':[0],
                             'user_correct_answers_cum_part5':[0],
                             'user_correct_answers_cum_part6':[0],
                             'user_correct_answers_cum_part7':[0],
                             # following columns are pure question stats : 
                             ### TO BE IMPORTED ###
                             'part':[-1],
                             'qstats_answered_correctly':[-1],
                             'qstats_prior_question_had_explanation':[-1],
                             'qstats_answered_correctly_knowing_having_had_explanation':[-1],
                             'qstats_answered_correctly_knowing_having_not_had_explanation':[-1],
                             # following columns depend of the current question AND the hisory of user
                             ### TO BE COMPUTED ###
                             'user_personalized_qstat_knowing_had_explanation_or_not':[-1],
                             'already_seen':[-1],
                             'user_avg_score_cum_on_this_part':[-1],
                             'user_correct_answers_cum_on_this_part':[-1],
                             # the following line is the prediction to be made
                             ### TO BE PREDICTED ###
                             'answered_correctly':[-1]
                          })
    
    if not type(user_history)==pd.DataFrame:
        user_history=user_history_empty
    
    last_line=user_history.iloc[-1]
    new_line =last_line.copy()
    
    last_content_type_id=user_history.iloc[-1]['content_type_id']
    
    ### TO BE IMPUTED ###
    new_line['content_id']=content_id
    new_line['content_type_id']=content_type_id
    new_line['prior_question_had_explanation']=prior_question_had_explanation
    ### TO BE UPDATED WHATEVER THE CONTENT_TYPE ###
    new_line['user_activity_cumcount'] = last_line['user_activity_cumcount'] + 1
    new_line['at_least_one_lesson'] = last_line['at_least_one_lesson']

    if last_content_type_id==0:
        part=last_line['part']
        ### TO BE UPDATED IF LAST WAS QUESTION , ELSE COPIED ###
        new_line['user_correct_answers_cum'] = last_line['user_correct_answers_cum']\
                                             + last_line['answered_correctly']
        new_user_questions_count             = last_line['user_correct_answers_cum']\
                                             / last_line['user_avg_score_cum']\
                                             + 1
        new_line['user_avg_score_cum']       = new_line['user_correct_answers_cum']\
                                             / new_user_questions_count

        new_line[f'user_correct_answers_cum_part{part}'] = last_line[f'user_correct_answers_cum_part{part}']\
                                                         + last_line['answered_correctly']
        vars()[f'new_user_questions_count_part{part}']   = last_line[f'user_correct_answers_cum_part{part}']\
                                                         / last_line[f'user_avg_score_cum_part{part}']\
                                                         + 1
        new_line[f'user_avg_score_cum_part{part}']       = new_line[f'user_correct_answers_cum_part{part}']\
                                                         / vars()[f'new_user_questions_count_part{part}']                
        
    if content_type_id==0:        
        currect_question_stats=qstats.loc[qstats.content_id==content_id].iloc[-1]
        ### TO BE IMPORTED ###
        new_line['part']\
              = currect_question_stats['part']
        new_line['qstats_answered_correctly']\
              = currect_question_stats['qstats_answered_correctly']
        new_line['qstats_prior_question_had_explanation']\
              = currect_question_stats['qstats_prior_question_had_explanation']
        new_line['qstats_answered_correctly_knowing_having_had_explanation']\
              = currect_question_stats['qstats_answered_correctly_knowing_having_had_explanation']
        new_line['qstats_answered_correctly_knowing_having_not_had_explanation']\
              = currect_question_stats['qstats_answered_correctly_knowing_having_not_had_explanation']
        ### TO BE COMPUTED ###
        new_line['user_personalized_qstat_knowing_had_explanation_or_not']\
              = new_line['qstats_answered_correctly_knowing_having_had_explanation']\
             if prior_question_had_explanation\
           else new_line['qstats_answered_correctly_knowing_having_not_had_explanation']
        new_line['already_seen']\
              = 1 if content_id in user_history.loc[user_history.content_type_id==0,'content_id']\
           else 0
        new_line['user_avg_score_cum_on_this_part']=new_line[f'user_avg_score_cum_part{new_line["part"]}']
        new_line['user_correct_answers_cum_on_this_part']=new_line[f'user_correct_answers_cum_part{new_line["part"]}']
                                              
    elif content_type_id==1:
        ### TO BE UPDATED WHATEVER THE CONTENT_TYPE ###
        new_line['at_least_one_lesson']=1
        ### TO BE IMPORTED ###
        new_line['part']= -1 # TODO : si on veut utiliser la partie de la lecture, il faut importer la base des lectures
        new_line['qstats_answered_correctly']= -1
        new_line['qstats_prior_question_had_explanation']= -1
        new_line['qstats_answered_correctly_knowing_having_had_explanation']= -1
        new_line['qstats_answered_correctly_knowing_having_not_had_explanation']= -1
        ### TO BE COMPUTED ###
        new_line['user_personalized_qstat_knowing_had_explanation_or_not']= -1
        new_line['already_seen']= -1
        new_line['user_avg_score_cum_on_this_part']= -1
        new_line['user_correct_answers_cum_on_this_part']= -1
        
    ### TO BE PREDICTED ###
        user_history.iloc[-1,-1]\
        = pipeline.predict_proba(user_history[pipeline_features_list.feature.to_list()].iloc[-2:-1])[0,1]

    new_line['answered_correctly']= -1
                                
    user_history=user_history.append(new_line,ignore_index=True)

    return user_history

def pred_answers(loop_length=100, question_selection_strategy='k_tracing'):
        user_history=None
        if question_selection_strategy=='k_tracing':
            for i in range(loop_length):
                next_question_id=random.choice(qstats.content_id.to_list())
        
                user_history=user_history_update(0,
                                         next_question_id,
                                         qstats,
                                         user_history,
                                         prior_question_had_explanation=random.uniform(0, 1)>0.1)
                ### PREDICTION ###
                user_history.iloc[-1,-1]\
                = pipeline.predict_proba(user_history[pipeline_features_list.feature.to_list()].iloc[-2:-1])[0,1]

        elif question_selection_strategy=='random':
            for i in range(loop_length):
                next_question_id = df_train_random.content_id.to_list()[i]
        
                user_history=user_history_update(0,
                                         next_question_id,
                                         qstats,
                                         user_history,
                                         prior_question_had_explanation=random.uniform(0, 1)>0.1)
                ### PREDICTION ###
                user_history.iloc[-1,-1]\
                = pipeline.predict_proba(user_history[pipeline_features_list.feature.to_list()].iloc[-2:-1])[0,1]


        elif question_selection_strategy=='sorted':
            for i in range(loop_length):
                next_question_id = df_train_sorted.content_id.to_list()[i]
        
                user_history=user_history_update(0,
                                         next_question_id,
                                         qstats,
                                         user_history,
                                         prior_question_had_explanation=random.uniform(0, 1)>0.1)
                #user_history.loc[len(user_history)-1, 'answered_correctly'] \
                #= pipeline.predict_proba(user_history[pipeline_features_list.feature.to_list()].iloc[-2:-1])[0,1]


                ### PREDICTION ###
                user_history.iloc[-1,-1]\
                = pipeline.predict_proba(user_history[pipeline_features_list.feature.to_list()].iloc[-2:-1])[0,1]

        return user_history







