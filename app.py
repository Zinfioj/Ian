import streamlit as st
st.title('WELCOM')
st.write('hãy nhập tên người dùng')
name = st.text_input('nhập username')
while str(name)[:len(name)-6] != 'gay123':
    st.write('nhập lại tên của bạn')
    name = st.text_input(':)))')

st.wrtie('nhập mật khẩu')
passs = st.text_input('password')

while str(passs.lower()) != 'taobigay':
    st.write('nhập lại mật khẩu')
    pass = st.text_input('bạn có bị gay không')
st.write('chào '+name[:len(name)-6])
