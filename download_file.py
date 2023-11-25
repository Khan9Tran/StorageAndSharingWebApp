import boto3
import os

import subprocess


# def download_file_from_s3(session, file_download):
   # pass
    # s3 = session.client('s3')

    # bucket_name = 'storage-and-sharing-file-kbh'
    # iam_client = session.client('iam')
    # response = iam_client.get_user()

    # username = response["User"]["UserName"]
    # file_name, file_extension = os.path.splitext(file_download)
    # object_key = f"{username}/{file_name}{file_extension}"
    # try:
    #     # Tải tệp từ S3 và lưu vào máy tính cục bộ
    #     s3.download_file(bucket_name, object_key, local_filename)
    #     print(f"Download successful. File saved to {local_filename}")
    # except Exception as e:
    #     print(f"Download failed: {e}")


# import streamlit as st
# import base64

# def create_download_link(content, filename):
#     encoded_content = base64.b64encode(content.encode()).decode()
#     href = f'<a href="data:file/txt;base64,{encoded_content}" download="{filename}">Click here to download {filename}</a>'
#     return href

# # Example usage
# file_content = 'Hello, this is an example content.'
# file_name = 'example.txt'

# # Create a download link
# download_link = create_download_link(file_content, file_name)

# # Display the link
# st.markdown(download_link, unsafe_allow_html=True)
def download_file_from_s3(session, file_download):
    if session is not None:
        s3 = session.client('s3')

        bucket_name = 'storage-and-sharing-file-kbh'
        iam_client = session.client('iam')
        response = iam_client.get_user()

        username = response["User"]["UserName"]
        file_name, file_extension = os.path.splitext(file_download)
        object_key = f"{username}/{file_name}{file_extension}"

        try:
            # Get the user's home directory and create the full path for the local download
            user_home = os.path.expanduser("~")
            local_filename = os.path.join(user_home, 'Downloads', file_download)

            # Download the file from S3 and save it locally
            s3.download_file(bucket_name, object_key, local_filename)
            print(f"Download successful. File saved to {local_filename}")
        except Exception as e:
            print(f"Download failed: {e}")

import login 
if __name__ == '__main__':
    session = login.show_login_form()
    download_file_from_s3(session,'DSCF6782_750x960.webp')