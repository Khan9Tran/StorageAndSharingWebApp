import streamlit as st

def new_upload(session):
    st.title("New Upload")

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        upload_to_s3(uploaded_file, session)

def upload_to_s3(uploaded_file, session):
    st.write("Uploading file to S3...")

    # AWS credentials
    aws_access_key_id = "your_access_key_id"
    aws_secret_access_key = "your_secret_access_key"
    bucket_name = "your_bucket_name"

    # Create a Boto3 S3 client
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    # Get the file name and extension
    file_name, file_extension = os.path.splitext(uploaded_file.name)

    # Specify the S3 key (file path in the bucket)
    s3_key = f"uploads/{file_name}{file_extension}"

    # Upload the file to S3
    s3.upload_fileobj(uploaded_file, bucket_name, s3_key)

    st.success("File uploaded to S3 successfully!")

