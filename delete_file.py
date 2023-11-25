import boto3

def delete_file(session, filename):
    try:
        s3 = session.client('s3')

        bucket_name = 'storage-and-sharing-file-kbh'
        # Delete the file
        s3.delete_object(Bucket=bucket_name, Key=filename)

        print(f"The file {filename} has been deleted from {bucket_name}.")
        return True
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")
        return False
