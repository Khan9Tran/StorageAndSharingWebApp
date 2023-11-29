import os
from tkinter import Tk, filedialog

def select_folder_dialog():
    # Tạo một cửa sổ dialog để chọn thư mục
    root = Tk()
    root.attributes('-topmost', True)  # Hiển thị cửa sổ trên cùng
    root.withdraw()  # Ẩn cửa sổ chính

    # Hiển thị dialog và lấy đường dẫn thư mục được chọn
    folder_selected = filedialog.askdirectory()

    # Kiểm tra xem người dùng đã chọn một thư mục hay chọn cancel
    if folder_selected:
        root.destroy()  # Đóng cửa sổ dialog nếu người dùng đã chọn thư mục
        return folder_selected
    else:
        root.destroy()  # Đóng cửa sổ dialog nếu người dùng đã chọn cancel
        return None

def download_file_from_s3(session, file_download):
    # Kiểm tra xem phiên làm việc (session) đã được thiết lập chưa
    if session is not None:
        # Tạo đối tượng S3 từ phiên làm việc
        s3 = session.client('s3')

        # Mở cửa sổ dialog để chọn thư mục lưu trữ file được tải về
        path = select_folder_dialog()
        if path is None:
            print(f"Vui lòng chọn thư mục")
            return False

        # Xác định tên bucket và đường dẫn đối tượng trong S3
        bucket_name = 'storage-and-sharing-file-kbh'
        iam_client = session.client('iam')
        response = iam_client.get_user()
        username = response["User"]["UserName"]
        file_name, file_extension = os.path.splitext(file_download)
        object_key = f"{username}/{file_name}{file_extension}"

        try:
            # Lấy đường dẫn đầy đủ cho file được tải về cục bộ
            local_filename = os.path.join(path, file_download)

            # Tải file từ S3 và lưu trữ nó cục bộ
            s3.download_file(bucket_name, object_key, local_filename)
            print(f"Tải về thành công. File được lưu tại {local_filename}")
        except Exception as e:
            print(f"Tải về thất bại: {e}")
            return False

    return True