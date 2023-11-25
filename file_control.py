import streamlit as st
import upload as ul

def new_upload(session):
    st.title("New Upload")
    uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)

    # Kiểm tra xem đã có file được chọn chưa
    if uploaded_files is not None:
        submit_button = st.button("Submit")
        if submit_button and uploaded_files is not None:
            ul.upload_to_s3(uploaded_files, session)


