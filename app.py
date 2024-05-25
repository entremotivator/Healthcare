import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Initialize Streamlit app
st.set_page_config(page_title="Home Healthcare Checklist")

# UI
st.title("***Home Healthcare Checklist***")
st.subheader("Organize, Prioritize, and Manage your tasks effectively!")

# Local Database
@st.cache(allow_output_mutation=True)
def get_local_data():
    return pd.DataFrame(columns=["Task", "Category", "Due Date", "Priority", "Completed", "Subtasks"])

data = get_local_data()

# Functions for interacting with local data
def save_local_data():
    data.to_csv("local_data.csv", index=False)

def load_local_data():
    return pd.read_csv("local_data.csv") if "local_data.csv" in os.listdir() else pd.DataFrame(columns=["Task", "Category", "Due Date", "Priority", "Completed", "Subtasks"])

def add_task(task, category, due_date, priority, completed, subtasks):
    global data
    new_task = {"Task": task, "Category": category, "Due Date": due_date, "Priority": priority, "Completed": completed, "Subtasks": subtasks}
    data = data.append(new_task, ignore_index=True)
    save_local_data()

def edit_task(task_id, updated_task, updated_category, updated_due_date, updated_priority, completed, updated_subtasks):
    global data
    task_index = task_id
    data.at[task_index, "Task"] = updated_task
    data.at[task_index, "Category"] = updated_category
    data.at[task_index, "Due Date"] = updated_due_date
    data.at[task_index, "Priority"] = updated_priority
    data.at[task_index, "Completed"] = completed
    data.at[task_index, "Subtasks"] = updated_subtasks
    save_local_data()

def clone_task(task_id):
    global data
    task_to_clone = data.iloc[task_id]
    clone_task = task_to_clone.copy()
    clone_task["Task"] = f"Copy of {clone_task['Task']}"
    data = data.append(clone_task, ignore_index=True)
    save_local_data()

def delete_task(task_id):
    global data
    data = data.drop(index=task_id).reset_index(drop=True)
    save_local_data()

# Load data from CSV
load_local_data()

# Add example home healthcare tasks with subtasks
example_tasks = [
    {
        "Task": "Medication Management",
        "Category": "Medical",
        "Due Date": "2024-06-01",
        "Priority": "High",
        "Completed": False,
        "Subtasks": [
            "Organize medications by time of day",
            "Create a medication schedule",
            "Ensure medications are refilled on time",
            "Monitor for side effects",
            "Coordinate with the pharmacy for delivery",
            "Set reminders for medication times"
        ]
    },
    {
        "Task": "Patient Hygiene",
        "Category": "Personal Care",
        "Due Date": "2024-05-30",
        "Priority": "Medium",
        "Completed": False,
        "Subtasks": [
            "Assist with bathing",
            "Help with grooming",
            "Ensure clean clothes are available",
            "Change bed linens",
            "Maintain oral hygiene"
        ]
    },
    {
        "Task": "Physical Therapy Exercises",
        "Category": "Rehabilitation",
        "Due Date": "2024-05-28",
        "Priority": "High",
        "Completed": False,
        "Subtasks": [
            "Follow the prescribed exercise regimen",
            "Ensure proper form during exercises",
            "Record progress and any discomfort",
            "Schedule regular therapy sessions"
        ]
    },
    {
        "Task": "Meal Preparation",
        "Category": "Nutrition",
        "Due Date": "2024-05-29",
        "Priority": "Medium",
        "Completed": False,
        "Subtasks": [
            "Plan a weekly menu",
            "Ensure dietary restrictions are met",
            "Prepare meals in advance",
            "Maintain food hygiene",
            "Assist with feeding if necessary"
        ]
    },
    {
        "Task": "Monitoring Vital Signs",
        "Category": "Medical",
        "Due Date": "2024-06-02",
        "Priority": "High",
        "Completed": False,
        "Subtasks": [
            "Measure blood pressure",
            "Check heart rate",
            "Monitor blood sugar levels",
            "Track temperature",
            "Record and report any irregularities"
        ]
    },
    {
        "Task": "Housekeeping",
        "Category": "Household",
        "Due Date": "2024-05-31",
        "Priority": "Low",
        "Completed": False,
        "Subtasks": [
            "Clean and sanitize living areas",
            "Do the laundry",
            "Organize the patient's room",
            "Dispose of waste properly",
            "Ensure a safe and clutter-free environment"
        ]
    },
    {
        "Task": "Transportation to Appointments",
        "Category": "Logistics",
        "Due Date": "2024-06-03",
        "Priority": "Medium",
        "Completed": False,
        "Subtasks": [
            "Schedule transportation in advance",
            "Assist the patient into the vehicle",
            "Ensure safety during transit",
            "Accompany patient to the appointment",
            "Collect prescriptions or documents if needed"
        ]
    },
    {
        "Task": "Social Interaction",
        "Category": "Emotional Support",
        "Due Date": "2024-05-27",
        "Priority": "Low",
        "Completed": False,
        "Subtasks": [
            "Schedule regular visits or calls",
            "Engage in meaningful conversations",
            "Encourage participation in social activities",
            "Monitor for signs of depression or anxiety"
        ]
    },
    {
        "Task": "Medical Equipment Management",
        "Category": "Logistics",
        "Due Date": "2024-06-04",
        "Priority": "Medium",
        "Completed": False,
        "Subtasks": [
            "Ensure all equipment is functioning",
            "Clean and maintain equipment",
            "Order supplies as needed",
            "Provide training on equipment use",
            "Schedule regular maintenance checks"
        ]
    },
    {
        "Task": "Care Plan Review",
        "Category": "Administrative",
        "Due Date": "2024-06-05",
        "Priority": "High",
        "Completed": False,
        "Subtasks": [
            "Review the current care plan with healthcare providers",
            "Update the plan based on patient progress",
            "Discuss changes with the patient and family",
            "Document all updates and changes"
        ]
    }
]

# Adding example tasks to the local data
for task in example_tasks:
    add_task(task["Task"], task["Category"], task["Due Date"], task["Priority"], task["Completed"], task["Subtasks"])
