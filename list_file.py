import boto3
import streamlit as st
# def generate_presigned_url(session, bucket_name, username, filename, expiration=3600):
#     s3_client = session.client('s3')
#     try:
#         key = f"{username}/{filename}"
#         return s3_client.generate_presigned_url(
#             ClientMethod='get_object',
#             Params={'Bucket': bucket_name, 'Key': key},
#             ExpiresIn=expiration
#         )
#     except NoCredentialsError:
#         st.error("Error: Unable to generate presigned URL with the provided session.")
#         return None

# def list_and_download_user_files(session, bucket_name, username):
#     try:
#         s3_client = session.client('s3')
#         objects = s3_client.list_objects(Bucket=bucket_name, Prefix=f"{username}/")

#         st.write("List of Your Uploaded Files:")
#         for obj in objects.get('Contents', []):
#             file_name = obj['Key'].split('/')[-1]  # Get the file name from the full key
#             download_url = generate_presigned_url(session, bucket_name, username, obj['Key'])
#             st.write(f"- [{file_name}]({download_url})")
#     except NoCredentialsError:
#         st.error("Error: Unable to list or download files in S3 bucket with the provided session.")
def list_objects_in_folder(session):
    bucket_name = "test-bucket-tlnk"
    iam_client = session.client('iam')

    # get username
    response = iam_client.get_user()
    username = response["User"]["UserName"]

    # Create a Boto3 S3 client
    s3 = session.client('s3')

    # Thực hiện lệnh ListObjectsV2 để lấy danh sách các đối tượng trong thư mục
    response = s3.list_objects_v2(
        Bucket=bucket_name,
        Prefix=f"{username}/"
    )

    # Lấy danh sách các đối tượng từ response
    objects = response.get('Contents', [])

    # Lọc ra tên của các đối tượng (file) trong thư mục
    object_names = [obj['Key'].split('/')[-1] for obj in objects]

    return object_names
