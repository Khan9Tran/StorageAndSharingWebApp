import boto3
import os

def download_file_from_s3(session, local_file_name):
    
    s3 = session.client('s3')

    bucket_name = 'storage-and-sharing-file-kbh'
    iam_client = session.client('iam')
    response = iam_client.get_user()

    username = response["User"]["UserName"]
    file_name, file_extension = os.path.splitext(local_file_name)
    object_key = f"{username}/{file_name}{file_extension}"
    try:
        # Tải tệp từ S3 và lưu vào máy tính cục bộ
        s3.download_file(bucket_name, object_key, local_filename)
        print(f"Download successful. File saved to {local_filename}")
    except Exception as e:
        print(f"Download failed: {e}")
