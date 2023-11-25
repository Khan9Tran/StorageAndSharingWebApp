import logging
from botocore.exceptions import ClientError
import boto3 as boto

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ObjectWrapper:
    """Encapsulates S3 object actions."""

    def __init__(self, s3_object):
        """
        :param s3_object: A Boto3 Object resource. This is a high-level resource in Boto3
                          that wraps object actions in a class-like structure.
        """
        self.object = s3_object
        self.key = self.object.key

    def put(self, data):
        """
        Upload data to the object.

        :param data: The data to upload. This can either be bytes or a string. When this
                     argument is a string, it is interpreted as a file name, which is
                     opened in read bytes mode.
        """
        put_data = data
        if isinstance(data, str):
            try:
                with open(data, "rb") as file:
                    put_data = file.read()
            except FileNotFoundError:
                logger.exception("File not found: '%s'.", data)
                raise
            except IOError:
                logger.exception("Error reading file: '%s'.", data)
                raise

        try:
            self.object.put(Body=put_data)
            self.object.wait_until_exists()
            logger.info(
                "Put object '%s' to bucket '%s'.",
                self.object.key,
                self.object.bucket_name,
            )
        except ClientError:
            logger.exception(
                "Couldn't put object '%s' to bucket '%s'.",
                self.object.key,
                self.object.bucket_name,
            )
            raise

# Example usage:
if __name__ == "__main__":
    # Replace 'your_access_key', 'your_secret_key', and 'your_bucket_name' with your AWS credentials and bucket name
    s3 = boto.resource("s3", aws_access_key_id='AKIAYIZEJF73OJH7D4XE', aws_secret_access_key='cXVJvDtbVcW48teFI7pf/OzaGZnA0HQOEhcpzS0P')
    bucket = s3.Bucket('test-bucket-tlnk')

    # Replace 'your_file_path' with the path to the file you want to upload
    file_path = 'D:/uploads/category/1700440569479.png'
    
    # Replace 'your_object_key' with the desired key for the object in the bucket
    object_key = 'thanhhieu123/category2.jpg'

    # Create an ObjectWrapper instance
    s3_object = ObjectWrapper(bucket.Object(object_key))

    # Upload the file
    s3_object.put(file_path)
