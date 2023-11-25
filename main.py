import streamlit as st
import boto3
import login


def list_files():
    # Create a button to copy the link to the clipboard
    if st.button("Copy Link to Clipboard"):
        copy_to_clipboard(link)

def copy_to_clipboard(link):
    # Use pyperclip to copy the link to the clipboard
    pyperclip.copy(link)
    st.success("Link copied to clipboard!")

def new_upload():
    # Thực hiện các thao tác để tải lên file mới
    st.write("Upload a new file:")

def main_menu():
    st.sidebar.title("Menu")
    options = ["List Files", "New Upload"]
    choice = st.sidebar.selectbox("Select Option", options)

if __name__ =="__main__":
    session = login.show_login_form()
    if session is not None: 
        