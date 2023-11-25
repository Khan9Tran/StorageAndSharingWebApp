import boto3
import streamlit as st

def list_objects_in_folder(session):
    bucket_name = "storage-and-sharing-file-kbh"
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
    object_names = [obj['Key'].split('/')[-1] for obj in objects if obj['Key'] != f"{username}/"]

    return object_names

