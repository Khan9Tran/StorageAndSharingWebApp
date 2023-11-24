import streamlit as st
import subprocess

# Streamlit app
st.title("AWS IAM Login")

# Kiểm tra xem đã có thông tin xác thực chưa
if not st.session_state.get('aws_authenticated'):
    st.warning("Please authenticate with AWS before using the app.")

    # Hiển thị form xác thực
    aws_access_key_id = st.text_input("AWS Access Key ID")
    aws_secret_access_key = st.text_input("AWS Secret Access Key", type="password")
    aws_region = st.text_input("AWS Region")

