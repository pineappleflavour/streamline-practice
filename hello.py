#pip3 install streamlit

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Simple Data Dashboard')

# Load data
data = st.file_uploader("Choose a CSV file", type = 'csv')
if data is not None:
    st.write('File Uploaded Successfully!')

    df = pd.read_csv(data)

    # Show the data
    st.subheader('Data Preview')
    st.write(df.head())
    
    # Show the data summary
    st.subheader('Data Summary')
    st.write(df.describe())

    # Filter tool for the data
    st.subheader('Filter Data')
    columns = df.columns.tolist()
    selected_columns = st.selectbox('Select Column to filter by', columns)
    unique_values = df[selected_columns].unique()
    selected_values = st.selectbox('Select Value', unique_values)

    filtered_df = df[df[selected_columns] == selected_values]
    st.write(filtered_df)

    # Plot the data
    st.subheader('Data Visualization')
    x_axis = st.selectbox('Select X-axis', columns)
    y_axis = st.selectbox('Select Y-axis', columns)

    if st.button('Generate Plot'):
        st.write('Generating Plot')
        st.line_chart(filtered_df.set_index(x_axis)[y_axis])
        
else:
    st.write('No File Uploaded')

# Run the app
# streamlit run hello.py