import streamlit as st
import pandas as pd
import numpy as np

# Generate sample medical healthcare data
def generate_data():
    np.random.seed(0)
    categories = ['Temperature', 'Heart Rate', 'Blood Pressure', 'Respiratory Rate', 'Oxygen Saturation',
                  'Glucose Level', 'Cholesterol Level', 'BMI', 'Pain Level', 'Exercise Duration']
    patients = np.arange(1, 101)
    data = {'Patient': np.random.choice(patients, 1000),
            'Category': np.random.choice(categories, 1000),
            'Value': np.random.normal(0, 1, 1000)}  # Generating random normal values for demonstration
    return pd.DataFrame(data)

data = generate_data()

# Set page title
st.title('Medical Healthcare Data Visualization')

# Sidebar with options
chart_type = st.sidebar.selectbox('Select Chart Type', ['Line Chart', 'Histogram', 'Box Plot'])

# Display different charts based on selection
if chart_type == 'Line Chart':
    st.subheader('Line Chart')
    selected_category = st.selectbox('Select Category', sorted(data['Category'].unique()))
    line_data = data[data['Category'] == selected_category]
    st.line_chart(line_data.groupby('Patient')['Value'].mean())

elif chart_type == 'Histogram':
    st.subheader('Histogram')
    selected_category = st.selectbox('Select Category', sorted(data['Category'].unique()))
    hist_data = data[data['Category'] == selected_category]['Value']
    st.hist(hist_data, bins=20)

elif chart_type == 'Box Plot':
    st.subheader('Box Plot')
    selected_category = st.selectbox('Select Category', sorted(data['Category'].unique()))
    box_data = data[data['Category'] == selected_category]
    st.box_plot(box_data['Value'], vert=False)

# Additional charts can be added here

# Display sample data
st.subheader('Sample Data')
st.write(data.head(10))

