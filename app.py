import streamlit as st
import pandas as pd
from datetime import datetime

# Title and introduction
st.title('Home Healthcare Services')
st.write('Welcome to our Home Healthcare Services app. We provide high-quality healthcare services in the comfort of your home.')

# Sidebar for navigation
st.sidebar.title('Navigation')
pages = ['Home', 'Services', 'Book Appointment', 'Contact Us']
selection = st.sidebar.radio('Go to', pages)

# Home page
if selection == 'Home':
    st.header('About Us')
    st.write('We are a leading provider of home healthcare services, dedicated to offering professional and compassionate care to our clients.')

    st.header('Our Mission')
    st.write('Our mission is to improve the quality of life for our clients by providing personalized healthcare services in a safe and comfortable environment.')

# Services page
elif selection == 'Services':
    st.header('Our Services')
    services = {
        'Nursing Care': 'Professional nursing care at home for medical needs.',
        'Physical Therapy': 'Rehabilitation and physical therapy services to aid recovery.',
        'Elderly Care': 'Comprehensive care services for elderly individuals.',
        'Palliative Care': 'Supportive care for those with serious illnesses.',
        'Personal Care': 'Assistance with daily activities and personal hygiene.'
    }
    
    for service, description in services.items():
        st.subheader(service)
        st.write(description)

# Book Appointment page
elif selection == 'Book Appointment':
    st.header('Book an Appointment')
    st.write('Please provide your details to book an appointment with us.')

    name = st.text_input('Name')
    contact = st.text_input('Contact Number')
    service_needed = st.selectbox('Service Needed', list(services.keys()))
    date = st.date_input('Preferred Appointment Date', min_value=datetime.today())
    time = st.time_input('Preferred Appointment Time')

    if st.button('Submit'):
        st.success(f'Appointment booked for {name} on {date} at {time} for {service_needed}. We will contact you soon.')

# Contact Us page
elif selection == 'Contact Us':
    st.header('Contact Us')
    st.write('If you have any questions or need further information, please feel free to contact us.')

    st.subheader('Phone')
    st.write('+1 234 567 890')

    st.subheader('Email')
    st.write('info@homehealthcare.com')

    st.subheader('Address')
    st.write('123 Healthcare Street, Home City, HC 12345')

# Run the app
if __name__ == '__main__':
    st.write("Home Healthcare Streamlit App")

