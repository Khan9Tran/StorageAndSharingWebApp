import boto3
import streamlit as st
import os

def download_file_from_s3(session):
    s3 = session.client('s3')
    bucket_name = 'storage-and-sharing-file-kbh'
    iam_client = session.client('iam')
    
    response = iam_client.get_user()
    username = response["User"]["UserName"]

    # Hiển thị widget tải lên tệp
    uploaded_file = st.file_uploader("Chọn tệp để tải xuống")

    if uploaded_file is not None:
        # Hiển thị widget để chọn nơi lưu trữ và nhập tên tệp lưu trữ
        local_path = st.text_input("Nhập đường dẫn nơi lưu trữ", "")
        file_name = st.text_input("Nhập tên tệp lưu trữ", uploaded_file.name)

        # Nếu người dùng nhập đường dẫn và tên tệp, thực hiện tải xuống
        if st.button("Tải xuống"):
            st.write("Đang tải xuống...")

            # Kiểm tra xem người dùng đã nhập đủ thông tin hay chưa
            if local_path and file_name:
                # Tạo đường dẫn đầy đủ
                local_filename = os.path.join(local_path, file_name)

                # Lưu tệp tải xuống vào đường dẫn được chỉ định
                object_key = f"{username}/{uploaded_file.name}"
                s3.download_file(bucket_name, object_key, local_filename)
                st.success(f"Tải xuống thành công. Tệp được lưu tại: {local_filename}")
            else:
                st.warning("Vui lòng nhập đường dẫn và tên tệp lưu trữ.")
