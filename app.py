import streamlit as st
import pandas as pd
from datetime import datetime
import sqlite3
from sqlalchemy import create_engine
import hashlib

# Initialize database connection
engine = create_engine('sqlite:///healthcare_app.db')
conn = engine.connect()

# Create tables if they don't exist
conn.execute('''
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    contact TEXT,
    service_needed TEXT,
    appointment_date DATE,
    appointment_time TIME
)
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
''')

# Hashing function for passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to add a new user
def add_user(username, password):
    hashed_password = hash_password(password)
    conn.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{hashed_password}')")
    conn.commit()

# Function to validate user login
def login_user(username, password):
    hashed_password = hash_password(password)
    result = conn.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{hashed_password}'").fetchone()
    return result is not None

# Function to send email confirmation (stub function for example)
def send_confirmation_email(name, email, service, date, time):
    # Implement email sending functionality here
    return True

# User session management
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = ''

# Login and Signup pages
def login_page():
    st.header('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        if login_user(username, password):
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success('Login successful!')
        else:
            st.error('Invalid username or password')

def signup_page():
    st.header('Sign Up')
    username = st.text_input('Choose a Username')
    password = st.text_input('Choose a Password', type='password')
    password_confirm = st.text_input('Confirm Password', type='password')

    if st.button('Sign Up'):
        if password == password_confirm:
            try:
                add_user(username, password)
                st.success('User registered successfully!')
            except:
                st.error('Username already exists.')
        else:
            st.error('Passwords do not match')

# Streamlit app layout and navigation
st.title('Home Healthcare Services')
st.sidebar.title('Navigation')
pages = ['Home', 'Services', 'Book Appointment', 'Contact Us', 'Testimonials', 'Our Team', 'FAQs']
if not st.session_state['logged_in']:
    pages += ['Login', 'Sign Up']
else:
    pages += ['My Appointments', 'Logout']
selection = st.sidebar.radio('Go to', pages)

# Home page
if selection == 'Home':
    st.header('Welcome to Home Healthcare Services')
    st.write("""
        We are a leading provider of home healthcare services, dedicated to offering professional and compassionate care to our clients.
        Our services are designed to cater to a wide range of healthcare needs right in the comfort of your home.
    """)
    st.image('home_healthcare.jpg', use_column_width=True)
    st.header('Our Mission')
    st.write("""
        Our mission is to improve the quality of life for our clients by providing personalized healthcare services in a safe and comfortable environment.
        We strive to be the preferred choice for home healthcare services through our commitment to excellence and compassionate care.
    """)

# Services page
elif selection == 'Services':
    st.header('Our Services')
    services = {
        'Nursing Care': 'Professional nursing care at home for medical needs including wound care, injections, and monitoring vital signs.',
        'Physical Therapy': 'Rehabilitation and physical therapy services to aid recovery from injuries or surgeries.',
        'Elderly Care': 'Comprehensive care services for elderly individuals, including assistance with daily activities and companionship.',
        'Palliative Care': 'Supportive care for those with serious illnesses, focusing on relief from symptoms and stress.',
        'Personal Care': 'Assistance with daily activities such as bathing, dressing, and grooming to maintain personal hygiene.',
        'Medical Social Services': 'Support for clients and families to address social, emotional, and financial challenges related to healthcare.',
        'Home Health Aide Services': 'Personal care assistance and support for activities of daily living, ensuring safety and comfort.'
    }
    
    for service, description in services.items():
        st.subheader(service)
        st.write(description)

# Book Appointment page
elif selection == 'Book Appointment':
    if not st.session_state['logged_in']:
        st.error('You need to log in to book an appointment.')
        login_page()
    else:
        st.header('Book an Appointment')
        st.write('Please provide your details to book an appointment with us.')

        name = st.text_input('Name', st.session_state['username'])
        email = st.text_input('Email')
        contact = st.text_input('Contact Number')
        service_needed = st.selectbox('Service Needed', list(services.keys()))
        date = st.date_input('Preferred Appointment Date', min_value=datetime.today())
        time = st.time_input('Preferred Appointment Time')

        if st.button('Submit'):
            conn.execute(
                "INSERT INTO appointments (name, email, contact, service_needed, appointment_date, appointment_time) VALUES (?, ?, ?, ?, ?, ?)",
                (name, email, contact, service_needed, date, time)
            )
            conn.commit()
            if send_confirmation_email(name, email, service_needed, date, time):
                st.success(f'Appointment booked for {name} on {date} at {time} for {service_needed}. A confirmation email has been sent to {email}.')
            else:
                st.error('Failed to send confirmation email. Please check your email address and try again.')

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

# Testimonials page
elif selection == 'Testimonials':
    st.header('Customer Testimonials')
    testimonials = [
        ("John Doe", "The nursing care provided by Home Healthcare Services was exceptional. The nurses were professional and compassionate."),
        ("Jane Smith", "Thanks to their physical therapy services, my recovery after surgery was smooth and quick. Highly recommend!"),
        ("Michael Johnson", "The elderly care services have been a blessing for my parents. The caregivers are kind and attentive.")
    ]

    for name, testimonial in testimonials:
        st.subheader(name)
        st.write(f'"{testimonial}"')

# Our Team page
elif selection == 'Our Team':
    st.header('Meet Our Team')
    team_members = [
        ("Dr. Emily Carter", "Chief Medical Officer", "Dr. Carter oversees all medical services and ensures the highest standards of care."),
        ("Nurse James Brown", "Head Nurse", "James leads our team of nurses and ensures compassionate and professional care."),
        ("Dr. Sarah Lee", "Physical Therapist", "Dr. Lee specializes in rehabilitation and physical therapy services."),
        ("Ms. Linda Thompson", "Medical Social Worker", "Linda supports our clients and their families by addressing social and emotional challenges.")
    ]

    for name, title, bio in team_members:
        st.subheader(name)
        st.write(f'**{title}**')
        st.write(bio)

# FAQs page
elif selection == 'FAQs':
    st.header('Frequently Asked Questions')
    faqs = {
        "What services do you offer?": "We offer a wide range of services including nursing care, physical therapy, elderly care, palliative care, and personal care.",
        "How can I book an appointment?": "You can book an appointment through our app or by contacting us directly via phone or email.",
        "Do you accept insurance?": "Yes, we accept most major insurance plans. Please contact us for more details.",
        "Are your caregivers certified?": "All our caregivers are fully certified and undergo rigorous background checks and training."
    }

    search_query = st.text_input('Search FAQs')
    if search_query:
        for question, answer in faqs.items():
            if search_query.lower() in question.lower():
                st.subheader(question)
                st.write(answer)
    else:
        for question, answer in faqs.items():
            st.subheader(question)
            st.write(answer)

# Login page
elif selection == 'Login':
    login_page()

# Sign Up page
elif selection == 'Sign Up':
    signup_page()

# My Appointments page
elif selection == 'My Appointments':
    if not st.session_state['logged_in']:
        st.error('You need to log in to view your appointments.')
        login_page()
    else:
        st.header('My Appointments')
        username = st.session_state['username']
        appointments = conn.execute(f"SELECT * FROM appointments WHERE name='{username}'").fetchall()
        
        if appointments:
            for appt in appointments:
                st.subheader(f'Appointment {appt["id"]}')
                st.write(f"""
                    **Service Needed:** {appt['service_needed']}
                    **Date:** {appt['appointment_date']}
                    **Time:** {appt['appointment_time']}
                    **Contact:** {appt['contact']}
                """)
        else:
            st.write('No appointments found.')

# Logout page
elif selection == 'Logout':
    st.session_state['logged_in'] = False
    st.session_state['username'] = ''
    st.success('Logged out successfully.')

# Close the connection
conn.close()
