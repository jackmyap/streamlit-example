import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Load your trained model (this assumes you have a trained model saved as a pickle file)
# model = pd.read_pickle("/path/to/your/model.pkl")

# Define the structure of the user input
def user_input_features():
    age = st.sidebar.number_input("Age", 18, 80, 30)
    sex = st.sidebar.selectbox('Sex', ('male', 'female'))
    cp = st.sidebar.selectbox('Chest Pain Type', ('typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'))
    trestbps = st.sidebar.slider('Resting Blood Pressure', 90, 200, 120)
    chol = st.sidebar.slider('Serum Cholestoral in mg/dl', 100, 600, 300)
    fbs = st.sidebar.radio('Fasting Blood Sugar > 120 mg/dl', ('True', 'False'))
    restecg = st.sidebar.selectbox('Resting Electrocardiographic Results', ('normal', 'ST-T wave abnormality', 'left ventricular hypertrophy'))
    thalach = st.sidebar.slider('Maximum Heart Rate Achieved', 70, 200, 150)
    exang = st.sidebar.radio('Exercise Induced Angina', ('Yes', 'No'))
    
    # Convert categorical inputs to numeric values for the model
    # This would involve transforming the user input to match the format that the model expects
    # For example, if your model uses one-hot encoding for categorical data, you'd convert the input here

    data = {'age': age,
            'sex': sex,
            'cp': cp,
            'trestbps': trestbps,
            'chol': chol,
            'fbs': fbs,
            'restecg': restecg,
            'thalach': thalach,
            'exang': exang
            }
    features = pd.DataFrame(data, index=[0])
    return features

# Set up the main app
st.write("""
# Heart Disease Prediction App
This app predicts the **Probability of Heart Disease** based on your input parameters.
""")

st.sidebar.header('User Input Parameters')

df = user_input_features()

# When 'Predict' is clicked, make the prediction and display it
if st.button('Predict'):
    prediction = model.predict(df)
    st.write('Based on the input, the model predicts...')
    st.write(prediction)

# You can also display the user input for verification
st.subheader('User Input Parameters')
st.write(df)
