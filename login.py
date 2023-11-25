import streamlit as st
import boto3
import logging

# Thiết lập logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Hàm lấy thông tin đăng nhập
def get_credentials():
    aws_access_key_id = st.text_input("AWS Access Key ID")
    aws_secret_access_key = st.text_input("AWS Secret Access Key", type="password")
    return aws_access_key_id, aws_secret_access_key

# Hàm xác thực và trả về session
def authenticate(aws_access_key_id, aws_secret_access_key):
    try:
        session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

        # Kiểm tra đăng nhập bằng cách gọi lệnh cơ bản
        iam = session.client('iam')
        iam.get_user()
        st.success("Login successful")
        return session
    except Exception as e:
        logger.warning("Error during login")
        logger.warning(f"Details: {str(e)}")
        st.warning("Error during login. Please check your credentials.")
        return None

# Hàm hiển thị form đăng nhập
def show_login_form():
    placeholder = st.empty()
    with placeholder.form("login_form"):
        aws_access_key_id, aws_secret_access_key = get_credentials()
        submitted = st.form_submit_button("Login")
        if submitted:
            session = authenticate(aws_access_key_id, aws_secret_access_key)
            placeholder.empty()
            return session
    return None

if __name__ == "__main__":
    session = show_login_form()

    if session is not None:
        # Thực hiện các thao tác cần thiết với session
        pass
