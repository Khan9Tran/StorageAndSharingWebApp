import boto3
import streamlit as st
import os

def create_kms_key(kms_client):
    try:
        response = kms_client.create_key(
            Description='Streamlit S3 Encryption Key',
            KeyUsage='ENCRYPT_DECRYPT',
            Origin='AWS_KMS'
        )
        key_id = response['KeyMetadata']['KeyId']
        return key_id
    except Exception as e:
        st.error(f"Error creating KMS key: {e}")
        return None

def encrypt_file(file_path, kms_client, key_id):
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()

        response = kms_client.encrypt(
            KeyId=key_id,
            Plaintext=file_data
        )

        return response['CiphertextBlob']
    except Exception as e:
        st.error(f"Error encrypting file: {e}")
        return None

def upload_to_s3(uploaded_files, session):
    if session is not None:
        st.write("Uploading files to S3...")

        try:
            # AWS credentials
            bucket_name = "test-bucket-tlnk"
            iam_client = session.client('iam')
            kms_client = session.client('kms')

            # Get username
            response = iam_client.get_user()
            username = response["User"]["UserName"]

            # Create a Boto3 S3 client
            s3 = session.client('s3')

            # Create a KMS key for encryption
            key_id = create_kms_key(kms_client)

            if key_id:
                for uploaded_file in uploaded_files:
                    # Get the file name and extension
                    file_name, file_extension = os.path.splitext(uploaded_file.name)

                    # Specify the S3 key (file path in the bucket)
                    s3_key = f"{username}/{file_name}{file_extension}"

                    # Encrypt the file
                    encrypted_data = encrypt_file(uploaded_file.name, kms_client, key_id)

                    if encrypted_data:
                        # Upload the encrypted file to S3
                        s3.put_object(
                            Bucket=bucket_name,
                            Key=s3_key,
                            Body=encrypted_data
                        )

                st.success("Files uploaded to S3 successfully!")
                st.balloons()
        except Exception as e:
            st.error("Error uploading files")
            st.exception(e)
    else:
        st.error("Error uploading files")
