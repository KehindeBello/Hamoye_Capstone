import streamlit as st
import pickle
import numpy as np
import sklearn

st.title('HDSC Capstone Project - Predicting Divorce')

with open('divorce_model_pkl' , 'rb') as f:
    model = pickle.load(f)

Idk_whats_going_on = st.slider("I dont know what's going on", 0, 4)
Anxieties = st.slider("Knowledge of partner's anxieties", 0, 4)
Accusations = st.slider("I have nothing to do with what i'm accused of", 0, 4)
Hopes_wishes = st.slider("Knowledge of partners hope and wishes", 0, 4)
Happy = st.slider("Same view about happiness", 0, 4)
Good_to_leave_home = st.slider("Sometimes I think it's good for me to leave home for a while", 0, 4)
Begin_correct = st.slider("We take our discussions from the beginning and correct it",0,4)
Aggro_argue = st.slider("Aggressiveness during argument", 0, 4)
Trust = st.slider("Similar values in trust", 0, 4)
Roles = st.slider("Similar role idea in marriage", 0, 4)

if st.button('Predict'):
    prediction = model.predict(np.array([[Idk_whats_going_on, Anxieties, Accusations, Hopes_wishes, Happy, Good_to_leave_home, Begin_correct, Aggro_argue, Trust, Roles]]))
    if prediction == 0:
        st.write('More likely to stay together')
    else:
        st.write('More likely to Divorce')
