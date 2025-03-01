import streamlit as st
import os

# Đường dẫn tệp tương đối
FILE_PATH = os.path.join(os.path.dirname(__file__), "db.txt")

# Hàm để lưu dữ liệu người dùng vào tệp văn bản
def save_data(file_path, name, question):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f'{name},{question}\n')

# Giao diện người dùng
st.title("User Data Collection")

name = st.text_input("Name")
question = st.text_input("Question")

if st.button("Submit"):
    if name and question:
        save_data(FILE_PATH, name, question)
        st.success("User data has been saved!")
    else:
        st.error("Please enter both name and question.")

# Đọc và hiển thị dữ liệu đã lưu
if st.button("Show Data"):
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            data = file.read()
        st.text_area("Stored Data", data)
    except FileNotFoundError:
        st.error("The data file does not exist.")
