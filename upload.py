import boto3
import streamlit as st
import os

import os
import streamlit as st


def upload_to_s3(uploaded_files, session):
    if session is not None:
        st.write("Uploading files to S3...")
        try:
            # AWS credentials
            bucket_name = "test-bucket-tlnk"
            iam_client = session.client('iam')

            # get username
            response = iam_client.get_user()
            username = response["User"]["UserName"]

            # Create a Boto3 S3 client
            s3 = session.client('s3')

            for uploaded_file in uploaded_files:
                # Get the file name and extension
                file_name, file_extension = os.path.splitext(uploaded_file.name)

                # Specify the S3 key (file path in the bucket)
                s3_key = f"{username}/{file_name}{file_extension}"

                # Upload the file to S3
                s3.upload_fileobj(uploaded_file, bucket_name, s3_key)

            st.success("Files uploaded to S3 successfully!")
            st.balloons()
        except Exception as e:
            st.error("Error uploading files")
            st.exception(e)
    else: 
        st.error("Error uploading files")