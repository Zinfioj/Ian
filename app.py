import streamlit as st

# Tiêu đề của ứng dụng
st.title('Ứng dụng Web với Streamlit')

def save(file_path,text):
    with open(file_path, "a") as file:
        file.write(f'{text}\n')
        
st.write('Hi!')

name = st.text_input('Nhập tên của bạn:')
st.write(f'Xin chào, {name}!')

st.write('hãy hỏi 1 điều gì đó ')
ques = st.text_input('Nhập câu hỏi:')

save("db.txt",f'{name}:::{ques}')

