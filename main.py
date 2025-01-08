import streamlit as st
import random

st.title("나의 첫번째 앱")
st.text('／n／n')
st.write('안녕하시오. 나는 □□이다')
st.write('나의 이메일 주소는 23_10514@daejin.sen.hs.kr 이다')

image_url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fm.inven.co.kr%2Fboard%2Flostark%2F4811%2F2332780&psig=AOvVaw0ZNPFPUDKsz1ViwDwrrYVs&ust=1736390567783000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMDLqYqN5YoDFQAAAAAdAAAAABAE"
st.image(image_url, use_column_width=True)

st.button("초기화", type="primary")
if st.button("난수 생성"):
    st.write(random.randint(1,1000))
else:
    st.write("잘가")
