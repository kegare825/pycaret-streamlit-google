import pycaret
from pycaret.regression import *
import streamlit as st
import pandas as pd
import numpy as np


model = pd.read_pickle('model.pkl')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions


def run():
    import streamlit as st
    from PIL import Image
    import os
    cwd = os.getcwd()
    print(cwd)
    st.write(cwd)
    image = Image.open('./assets/logo2.png')
    image_jamb = Image.open('./assets/jambitches.jpg')

    st.image(image,use_column_width=False)

    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))

    st.sidebar.info('Prediccion en linea y por lotes de bienes raices')
    st.sidebar.success('https://www.pycaret.org')

    st.sidebar.image(image_jamb)

    st.title("JAMBOUSING")
    st.header("Real state prediction app")

    if add_selectbox == 'Online':

        age = st.number_input('Age', min_value=1, max_value=100, value=25)
        sex = st.selectbox('Sex', ['male', 'female'])
        bmi = st.number_input('BMI', min_value=10, max_value=50, value=10)
        children = st.selectbox('Children', [0,1,2,3,4,5,6,7,8,9,10])
        if st.checkbox('Smoker'):
            smoker = 'yes'
        else:
            smoker = 'no'
        region = st.selectbox('Region', ['southwest', 'northwest', 'northeast', 'southeast'])

        output=""

        input_dict = {'age' : age, 'sex' : sex, 'bmi' : bmi, 'children' : children, 'scd moker' : smoker, 'region' : region}
        input_df = pd.DataFrame([input_dict])

        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            output = '$' + str(output)

        st.success('The output is {}'.format(output))

    if add_selectbox == 'Batch':

        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            #predictions = predict_model(estimator=model,data=data)
            #st.write(predictions)

if __name__ == '__main__':
    run()
