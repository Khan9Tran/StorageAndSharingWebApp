import streamlit as st
import boto3
import login
import share_file as sf
import file_control as fc


def list_files(session):
    fc.get_list_files(session)

def new_upload(session):
    if session is not None: 
        fc.new_upload(session)

def main_menu(session):
    st.sidebar.write("Hello: " + session.client('iam').get_user()["User"]["UserName"])
    st.sidebar.title("Menu")
    options = ["List Files", "New Upload"]
    choice = st.sidebar.selectbox("Select Option", options)

    if choice == "List Files":
        list_files(session)
    elif choice == "New Upload":
        new_upload(session)


if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Display login form if not authenticated
if not st.session_state.authenticated:
    session = login.show_login_form()
session = st.session_state.session
if  session is not None:
    main_menu(session)