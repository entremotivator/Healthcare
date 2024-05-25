import streamlit as st
import pandas as pd
import numpy as np

# Generate sample medical healthcare data
def generate_data():
    np.random.seed(0)
    categories = ['A', 'B', 'C', 'D', 'E']
    years = np.arange(2010, 2020)
    data = {'Category': np.random.choice(categories, 100),
            'Year': np.random.choice(years, 100),
            'Value': np.random.randint(1, 100, 100),
            'Age': np.random.randint(20, 80, 100),
            'Gender': np.random.choice(['Male', 'Female'], 100)}
    return pd.DataFrame(data)

data = generate_data()

# Set page title
st.title('Medical Healthcare Data Visualization')

# Sidebar with options
chart_type = st.sidebar.selectbox('Select Chart Type', ['Bar Chart', 'Line Chart', 'Scatter Plot', 'Pie Chart'])

# Display different charts based on selection
if chart_type == 'Bar Chart':
    st.subheader('Bar Chart')
    bar_data = data.groupby('Category')['Value'].mean().reset_index()
    st.bar_chart(bar_data.set_index('Category'))

elif chart_type == 'Line Chart':
    st.subheader('Line Chart')
    line_data = data.groupby('Year')['Value'].sum().reset_index()
    st.line_chart(line_data.set_index('Year'))

elif chart_type == 'Scatter Plot':
    st.subheader('Scatter Plot')
    scatter_data = data.sample(100)
    st.scatter_chart(scatter_data, x='Value', y='Age', color='Gender')

elif chart_type == 'Pie Chart':
    st.subheader('Pie Chart')
    pie_data = data['Gender'].value_counts().reset_index()
    st.pie_chart(pie_data.set_index('index'))

# Additional charts can be added here

# Display sample data
st.subheader('Sample Data')
st.write(data.head(10))

