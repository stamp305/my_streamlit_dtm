import streamlit as st

# Set the title
st.title("Iris Flower Feature Selector")

# Create sliders for each flower feature
sepal_length = st.slider("Sepal Length (cm)", min_value=4.0, max_value=8.0, value=5.1)
sepal_width = st.slider("Sepal Width (cm)", min_value=2.0, max_value=4.5, value=3.5)
petal_length = st.slider("Petal Length (cm)", min_value=1.0, max_value=7.0, value=1.4)
petal_width = st.slider("Petal Width (cm)", min_value=0.1, max_value=2.5, value=0.2)

# Show selected values
st.write("### Selected Feature Values:")
st.write(f"Sepal Length: {sepal_length} cm")
st.write(f"Sepal Width: {sepal_width} cm")
st.write(f"Petal Length: {petal_length} cm")
st.write(f"Petal Width: {petal_width} cm")
