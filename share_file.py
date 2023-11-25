# Tạo URL ký trước cho việc tải xuống đối tượng
import login
def shared_url(session, filename):

    iam_client = session.client('iam')
    response = iam_client.get_user()
    username = response["User"]["UserName"]

    s3_client = session.client('s3')
    url = s3_client.generate_presigned_url(
    ClientMethod='get_object',
    Params={'Bucket': 'test-bucket-tlnk', 'Key': '{}/{}'.format(username,filename)},
    ExpiresIn=3600
    )

    return url
# if __name__ == "__main__": 
#     aws_access_key_id = 'AKIAYIZEJF73OJH7D4XE'
#     aws_secret_access_key = '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'
#     session = login.show_login_form()
#     if session is not None:
        
#         print(shared_url(session,'category1.jpg'))