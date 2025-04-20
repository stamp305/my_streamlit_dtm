import streamlit as st
import numpy as np
import pickle

with open('dtm_trained_model.pkl','rb') as f:
    dtm_model = pickle.load(f)
# Set the title
st.title("Iris Flower Feature Selector")
st.write("Enter the feature of the iris flower")

# Create sliders for each flower feature
sepal_length = st.slider("Sepal Length (cm)", min_value=4.0, max_value=8.0, value=5.1)
sepal_width = st.slider("Sepal Width (cm)", min_value=2.0, max_value=4.5, value=3.5)
petal_length = st.slider("Petal Length (cm)", min_value=1.0, max_value=7.0, value=1.4)
petal_width = st.slider("Petal Width (cm)", min_value=0.1, max_value=2.5, value=0.2)

# Show selected values
if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = dtm_model.predict(input_data)
    speicies = ['Setosa', 'Versicolor', 'Virginica']
    st.success(f"The Predicted Species is: **{speicies[prediction[0]]}**")
