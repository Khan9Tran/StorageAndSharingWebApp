import streamlit as st
import upload as ul
import list_file as lf

def new_upload(session):
    st.title("New Upload")
    uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)

    # Kiểm tra xem đã có file được chọn chưa
    if uploaded_files is not None:
        submit_button = st.button("Submit")
        if submit_button and uploaded_files is not None:
            ul.upload_to_s3(uploaded_files, session)


def get_list_files(session):
    object_names = lf.list_objects_in_folder(session)

    # Hiển thị danh sách các file
    print("Danh sách các file trong thư mục:")
    for object_name in object_names:
        st.write(object_name)

    