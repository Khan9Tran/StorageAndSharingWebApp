import os
import base64
import boto3
import streamlit as st
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
            # Generate a presigned URL for the S3 object
            presigned_url = s3.generate_presigned_url(
                'get_object',
                Params={'Bucket': bucket_name, 'Key': object_key},
                ExpiresIn=3600  # URL expiration time in seconds
            )

            return presigned_url

        except Exception as e:
            print(f"Failed to generate presigned URL: {e}")
            return None

def create_download_link(download_url, filename):
    href = f'<a href="{download_url}" download="{filename}">Click here to download {filename}</a>'
    return href

import login

if __name__ == '__main__':
    session = login.show_login_form()
    download_url = download_file_from_s3(session, 'DSCF6782_750x960.webp')

    if download_url:
        download_link = create_download_link(download_url, 'DSCF6782_750x960.webp')
        st.markdown(download_link, unsafe_allow_html=True)
    else:
        print("Download failed.")
