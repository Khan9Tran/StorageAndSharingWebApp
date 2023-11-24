import boto3
import streamlit as st
# Tạo URL ký trước cho việc tải xuống đối tượng
def shared_url(s3_client, username):
    url = s3_client.generate_presigned_url(
    ClientMethod='get_object',
    Params={'Bucket': 'test-bucket-tlnk', 'Key': '{}/category.jpg'.format(username)},
    ExpiresIn=3600
    )
    return url
if __name__ == "__main__": 
    aws_access_key_id = 'AKIAYIZEJF73OJH7D4XE'
    aws_secret_access_key = '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'

    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    # Sử dụng phiên làm việc để tạo client S3
    s3_client = session.client('s3')


    iam_client = session.client('iam')

    # Gọi hàm GetUser để lấy thông tin về người dùng hiện tại
    response = iam_client.get_user()

    # Lấy tên người dùng từ kết quả
    username = response["User"]["UserName"]

    
    print(shared_url(s3_client,username))