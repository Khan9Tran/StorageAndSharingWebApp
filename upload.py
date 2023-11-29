import os
import streamlit as st
import datetime

def upload_to_s3(uploaded_files, session):
    # Kiểm tra xem phiên làm việc (session) đã được thiết lập chưa
    if session is not None:
        st.write("Đang tải lên file lên S3...")
        try:
            # Lấy thông tin đăng nhập AWS
            bucket_name = "storage-and-sharing-file-kbh"
            iam_client = session.client('iam')
            response = iam_client.get_user()

            # Lấy tên người dùng từ thông tin đăng nhập
            username = response["User"]["UserName"]
            # Tạo một client S3 từ Boto3
            s3 = session.client('s3')

            # Lặp qua từng file được tải lên
            for uploaded_file in uploaded_files:
                # Lấy tên và phần mở rộng của file
                file_name, file_extension = os.path.splitext(uploaded_file.name)
                # Thêm timestamp vào tên file để tránh trùng lặp
                file_name = file_name + '_' + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                # Xác định đường dẫn S3 (file path trong bucket)
                s3_key = f"{username}/{file_name}{file_extension}"
                # Tải file lên S3
                s3.upload_fileobj(uploaded_file, bucket_name, s3_key)

            # Hiển thị thông báo thành công nếu không có lỗi xảy ra
            st.success("Files uploaded to S3 successfully!")
            st.balloons()
        except Exception as e:
            # Hiển thị thông báo lỗi nếu có lỗi xảy ra
            st.error("Error uploading files")
            st.exception(e)
    else: 
        # Hiển thị thông báo lỗi nếu phiên làm việc chưa được thiết lập
        st.error("Error uploading files")