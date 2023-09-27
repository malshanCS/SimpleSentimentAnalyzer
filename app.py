import streamlit as st
import pandas as pd
import pickle


# load the model from disk
model = pickle.load(open('model2.pkl', 'rb'))

# create a title
st.title('good review / bad review')

# !streamlit run app.pyconda

review = st.text_input('Enter your movie review')
submit = st.button('Predict')

if submit:
    prediction = model.predict([review])
    # print(prediction)
    # st.write(prediction)

    if prediction[0] == 'positive':
        st.success('This review is positive')
    else:
        st.error('This review is negative')
