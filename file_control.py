import streamlit as st
import upload as ul
import list_file as lf
import pandas as pd

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

    # Tạo một DataFrame để hiển thị dữ liệu dưới dạng bảng
    file_data = {'File Name': object_names}
    df = pd.DataFrame(file_data)

    # Hiển thị nút cho mỗi file
    for index, row in df.iterrows():
        # Sử dụng `st.columns` để tạo cột
        col1, col2, col3, col4 = st.columns(4)

        # Hiển thị tên file
        col1.write(row['File Name'])

        # Button để download
        download_button = col2.button("Download", key=f"download_{index}")
        if download_button:
            # Đưa logic download vào đây
            st.success(f"{row['File Name']} đã được tải về.")

        # Button để share
        share_button = col3.button("Share", key=f"share_{index}")
        if share_button:
            # Đưa logic chia sẻ vào đây
            st.info(f"Chia sẻ {row['File Name']} với người khác.")

        # Button để delete
        delete_button = col4.button("Delete", key=f"delete_{index}")
        if delete_button:
            # Đưa logic delete vào đây
            st.success(f"{row['File Name']} đã được xóa.")
        
        st.write("")  # Xuống dòng cho dòng tiếp theo

    