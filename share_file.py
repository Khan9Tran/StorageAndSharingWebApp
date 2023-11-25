import boto3
from botocore.exceptions import NoCredentialsError
import login

def shared_url(session, filename):
    if session is not None:
        iam_client = session.client('iam')
        response = iam_client.get_user()
        username = response["User"]["UserName"]

        s3_client = session.client('s3')
        s3 = session.resource('s3', config=boto3.session.Config(signature_version='s3v4'))
        bucket_name = 'storage-and-sharing-file-kbh'
        object_key = f'{username}/{filename}'

        try:
            # Sử dụng chữ ký v4
            url = s3.meta.client.generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': bucket_name,
                    'Key': object_key
                },
                ExpiresIn=3600,
                HttpMethod='GET'
            )
            return url

        except NoCredentialsError:
            print("Credentials not available")
            return None

if __name__ == "__main__":
    aws_access_key_id = 'AKIAYIZEJF73OJH7D4XE'
    aws_secret_access_key = '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'
    session = login.show_login_form()
    if session is not None:
        print(shared_url(session, 'DSCF6782_750x960.webp'))
