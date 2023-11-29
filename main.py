import streamlit as st
import login
import file_control as fc

def list_files(session):
    # Gọi hàm từ module file_control để hiển thị danh sách file
    fc.get_list_files(session)

def new_upload(session):
    # Gọi hàm từ module file_control để thực hiện quá trình tải lên mới
    if session is not None: 
        fc.new_upload(session)

def main_menu(session):
    # Hiển thị thông tin người dùng ở thanh bên
    st.sidebar.write("Hello: " + session.client('iam').get_user()["User"]["UserName"])
    st.sidebar.title("Menu")
    options = ["List Files", "New Upload"]
    # Hiển thị lựa chọn menu
    choice = st.sidebar.selectbox("Select Option", options)

    # Xử lý tùy chọn được chọn
    if choice == "List Files":
        list_files(session)
    elif choice == "New Upload":
        new_upload(session)

# Kiểm tra xem người dùng đã được xác thực hay chưa
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Hiển thị mẫu đăng nhập nếu chưa được xác thực
if not st.session_state.authenticated:
    session = login.show_login_form()
session = st.session_state.session

# Nếu đã xác thực, hiển thị menu chính
if  session is not None:
    main_menu(session)