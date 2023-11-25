import streamlit as st
import boto3
import login
import share_file as sf

def list_files(session):
    # Create a button to copy the link to the clipboard
    if st.button("Copy Link to Clipboard"):
        copy_to_clipboard(link)

def new_upload(session):
    # Thực hiện các thao tác để tải lên file mới
    st.write("Upload a new file:")
    st.u

def main_menu(session):
    st.sidebar.title("Menu")
    options = ["List Files", "New Upload"]
    choice = st.sidebar.selectbox("Select Option", options)

    if choice == "List Files":
        list_files(session)
    elif choice == "New Upload":
        new_upload(session)


if __name__ =="__main__":

    session = login.show_login_form()

    if session is not None: 
        main_menu(session)
        print(sf.shared_url(session,'category1.jpg'))