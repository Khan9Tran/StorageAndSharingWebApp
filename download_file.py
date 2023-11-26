import os
from tkinter import Tk, filedialog

def select_folder_dialog():
    root = Tk()
    root.attributes('-topmost', True)
    root.withdraw()

    folder_selected = filedialog.askdirectory()

    # Kiểm tra xem người dùng đã chọn một thư mục hay chọn cancel
    if folder_selected:
        root.destroy()
        return folder_selected
    else:
        root.destroy()
        return None

def download_file_from_s3(session, file_download):
    if session is not None:
        s3 = session.client('s3')
        path = select_folder_dialog()
        if path is None:
            print(f"Please, select folder")
            return False
        bucket_name = 'storage-and-sharing-file-kbh'
        iam_client = session.client('iam')
        response = iam_client.get_user()

        username = response["User"]["UserName"]
        file_name, file_extension = os.path.splitext(file_download)
        object_key = f"{username}/{file_name}{file_extension}"

        try:
            # Get the user's home directory and create the full path for the local download
            user_home = os.path.expanduser("~")
            local_filename = os.path.join(user_home, path, file_download)

            # Download the file from S3 and save it locally
            s3.download_file(bucket_name, object_key, local_filename)
            print(f"Download successful. File saved to {local_filename}")
        except Exception as e:
            print(f"Download failed: {e}")
            return False
    return True
