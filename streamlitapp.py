import streamlit as st
import subprocess
import os

# Global variable to store the process
process_name = None

# Function to start the aimbot script
def start_aimbot():
    global process_name
    if process_name is None or process_name.poll() is not None:
        process_name = subprocess.Popen([".venv/Scripts/python", "aimbot_Baseline.py"])
        st.success("Aimbot started.")
    else:
        st.warning("Aimbot is already running.")

# Function to stop the aimbot script
def stop_aimbot():
    global process_name
    if process_name is not None and process_name.poll() is None:
        process_name.terminate()
        st.success("Aimbot stopped.")
    else:
        st.warning("Aimbot is not running.")

# Streamlit app
st.title("Script Controller")

if st.button("Start Aimbot"):
    start_aimbot()

if st.button("Stop Aimbot"):
    stop_aimbot()