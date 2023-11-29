import boto3
from botocore.exceptions import NoCredentialsError

def shared_url(session, filename):
    # Kiểm tra xem phiên làm việc (session) đã được thiết lập chưa
    if session is not None:
        # Lấy thông tin đăng nhập IAM
        iam_client = session.client('iam')
        response = iam_client.get_user()
        username = response["User"]["UserName"]

        # Tạo đối tượng S3 từ phiên làm việc và sử dụng chữ ký v4
        s3 = session.resource('s3', config=boto3.session.Config(signature_version='s3v4'))

        # Xác định tên bucket và đường dẫn (key) đối tượng trong S3
        bucket_name = 'storage-and-sharing-file-kbh'
        object_key = f'{username}/{filename}'

        try:
            # Tạo URL có thể chia sẻ (presigned URL) cho việc tải file
            url = s3.meta.client.generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': bucket_name,
                    'Key': object_key
                },
                ExpiresIn=3600,  # Thời gian hiệu lực của URL (đơn vị là giây)
                HttpMethod='GET'
            )

            return url

        except NoCredentialsError:
            # Hiển thị thông báo lỗi nếu thông tin đăng nhập không khả dụng
            print("Thông tin đăng nhập không khả dụng")
            return None
