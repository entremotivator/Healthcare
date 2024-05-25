import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    plt.bar(bar_data['Category'], bar_data['Value'])
    plt.xlabel('Category')
    plt.ylabel('Average Value')
    plt.title('Average Value by Category')
    st.pyplot()

elif chart_type == 'Line Chart':
    st.subheader('Line Chart')
    line_data = data.groupby('Year')['Value'].sum().reset_index()
    plt.plot(line_data['Year'], line_data['Value'])
    plt.xlabel('Year')
    plt.ylabel('Total Value')
    plt.title('Total Value by Year')
    st.pyplot()

elif chart_type == 'Scatter Plot':
    st.subheader('Scatter Plot')
    scatter_data = data.sample(100)
    plt.scatter(scatter_data['Value'], scatter_data['Age'], c=scatter_data['Gender'] == 'Female')
    plt.xlabel('Value')
    plt.ylabel('Age')
    plt.title('Scatter Plot of Value vs Age')
    plt.legend(['Male', 'Female'])
    st.pyplot()

elif chart_type == 'Pie Chart':
    st.subheader('Pie Chart')
    pie_data = data['Gender'].value_counts().reset_index()
    plt.pie(pie_data['Gender'], labels=pie_data['index'], autopct='%1.1f%%')
    plt.title('Distribution of Gender')
    st.pyplot()

# Additional charts can be added here

# Display sample data
st.subheader('Sample Data')
st.write(data.head(10))
