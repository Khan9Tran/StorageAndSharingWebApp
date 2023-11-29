def delete_file(session, filename):
    try:
        # Tạo đối tượng S3 từ phiên làm việc
        s3 = session.client('s3')
        bucket_name = 'storage-and-sharing-file-kbh'

        # Lấy thông tin đăng nhập IAM
        iam_client = session.client('iam')
        response = iam_client.get_user()
        username = response["User"]["UserName"]

        # Xác định đường dẫn đối tượng trong S3
        object_key = f"{username}/{filename}"

        # Xóa file từ S3
        s3.delete_object(Bucket=bucket_name, Key=object_key)

        print(f"File {filename} đã được xóa khỏi {bucket_name}.")
        return True
    except Exception as e:
        print(f"Có lỗi xảy ra khi xóa file: {e}")
        return False