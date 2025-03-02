import streamlit as st
import pandas as pd

st.title("Thu thập thông tin người dùng")

# Thu thập tên
name = st.text_input("Họ và tên:")

# Thu thập tuổi
age = st.number_input("Tuổi:", min_value=0, max_value=100, step=1)

# Thu thập giới tính
gender = st.radio("Giới tính:", ("Nam", "Nữ", "Khác"))

# Thu thập sở thích
hobbies = st.multiselect(
    "Sở thích:",
    ["Đọc sách", "Xem phim", "Chơi thể thao", "Đi du lịch", "Khác"]
)

# Thu thập ý kiến người dùng
feedback = st.text_area("Ý kiến của bạn:")

# Xác nhận và hiển thị thông tin đã thu thập
if st.button("Gửi"):
    # Lưu thông tin vào tệp CSV
    user_data = {
        "Họ và tên": [name],
        "Tuổi": [age],
        "Giới tính": [gender],
        "Sở thích": [", ".join(hobbies)],
        "Ý kiến": [feedback]
    }
    
    df = pd.DataFrame(user_data)
    
    # Ghi thông tin vào tệp CSV (tạo tệp mới nếu chưa tồn tại, bổ sung dữ liệu nếu đã tồn tại)
    df.to_csv("user_data.csv", mode='a', index=False, header=False)
    
    st.write("Thông tin đã được lưu thành công!")
    st.write("Họ và tên:", name)
    st.write("Tuổi:", age)
    st.write("Giới tính:", gender)
    st.write("Sở thích:", ", ".join(hobbies))
    st.write("Ý kiến của bạn:", feedback)
