import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate sample medical healthcare data for 10 demo patients with at least 3 months of data
def generate_data():
    np.random.seed(0)
    categories = ['Temperature', 'Heart Rate', 'Blood Pressure', 'Respiratory Rate', 'Oxygen Saturation',
                  'Glucose Level', 'Cholesterol Level', 'BMI', 'Pain Level', 'Exercise Duration']
    patients = ['Patient ' + str(i) for i in range(1, 11)]
    data = {'Patient': np.repeat(patients, 90),  # At least 3 months of data for each patient (90 days)
            'Date': [(datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(90)] * 10,
            'Category': np.random.choice(categories, 900),
            'Value': np.random.normal(0, 1, 900)}  # Generating random normal values for demonstration
    return pd.DataFrame(data)

data = generate_data()

# Set page title
st.title('Medical Healthcare Data Visualization')

# Sidebar with options
patient = st.sidebar.selectbox('Select Patient', sorted(data['Patient'].unique()))
selected_category = st.sidebar.selectbox('Select Category', sorted(data['Category'].unique()))

# Filter data based on selected patient and category
filtered_data = data[(data['Patient'] == patient) & (data['Category'] == selected_category)]

# Display different charts based on selection
if st.sidebar.checkbox('Show Data Table'):
    st.subheader('Data Table')
    st.write(filtered_data)

chart_type = st.sidebar.selectbox('Select Chart Type', ['Line Chart', 'Histogram', 'Box Plot'])

if chart_type == 'Line Chart':
    st.subheader('Line Chart')
    st.line_chart(filtered_data.set_index('Date')['Value'])

elif chart_type == 'Histogram':
    st.subheader('Histogram')
    st.hist(filtered_data['Value'], bins=20)

elif chart_type == 'Box Plot':
    st.subheader('Box Plot')
    st.box_plot(filtered_data['Value'], vert=False)

# Additional charts or features can be added here

# Display sample data
st.subheader('Sample Data')
st.write(data.head(10))
