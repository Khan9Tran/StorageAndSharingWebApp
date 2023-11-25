import os
import streamlit as st
from tkinter import Tk, filedialog

def select_folder_dialog():
    root = Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    root.destroy()
    return folder_selected

def main():
    st.title("Chọn Thư Mục")

    if st.button("Chọn Thư Mục"):
        selected_folder = select_folder_dialog()
        st.write("Thư mục đã chọn:", selected_folder)

if __name__ == "__main__":
    main()
