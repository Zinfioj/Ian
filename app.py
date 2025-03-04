import streamlit as st
st.title('WELCOM')
st.text('hãy nhập tên người dùng')
name = st.text_input('nhập username')
if str(name)[:len(name)-6] != 'gay123':
    st.text('nhập lại tên của bạn')
    name = st.text_input(':)))')

st.text('nhập mật khẩu')
password = st.text_input('password')

if str(password.lower()) != 'taobigay':
    st.text('nhập lại mật khẩu')
    password = st.text_input('bạn có bị gay không')
st.text('chào '+name[:len(name)-6])
