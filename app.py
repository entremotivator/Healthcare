import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Load sample medical healthcare data
@st.cache
def load_data():
    return pd.read_csv('medical_data.csv')  # You can replace 'medical_data.csv' with your own dataset

data = load_data()

# Set page title
st.title('Medical Healthcare Data Visualization')

# Sidebar with options
chart_type = st.sidebar.selectbox('Select Chart Type', ['Bar Chart', 'Line Chart', 'Scatter Plot', 'Pie Chart'])

# Display different charts based on selection
if chart_type == 'Bar Chart':
    st.subheader('Bar Chart')
    bar_data = data.groupby('Category')['Value'].mean().reset_index()
    fig = px.bar(bar_data, x='Category', y='Value', title='Average Value by Category')
    st.plotly_chart(fig)

elif chart_type == 'Line Chart':
    st.subheader('Line Chart')
    line_data = data.groupby('Year')['Value'].sum().reset_index()
    fig = px.line(line_data, x='Year', y='Value', title='Total Value by Year')
    st.plotly_chart(fig)

elif chart_type == 'Scatter Plot':
    st.subheader('Scatter Plot')
    scatter_data = data.sample(100)
    fig = px.scatter(scatter_data, x='Value', y='Age', color='Gender', title='Scatter Plot of Value vs Age')
    st.plotly_chart(fig)

elif chart_type == 'Pie Chart':
    st.subheader('Pie Chart')
    pie_data = data['Gender'].value_counts().reset_index()
    pie_data.columns = ['Gender', 'Count']
    fig = px.pie(pie_data, values='Count', names='Gender', title='Distribution of Gender')
    st.plotly_chart(fig)

# Additional charts can be added here

# Display sample data
st.subheader('Sample Data')
st.write(data.head(10))
