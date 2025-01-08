import streamlit as st
import random

st.title("나의 첫번째 앱")
st.text('／n／n')
st.write('안녕하시오. 나는 □□이다')
st.write('나의 이메일 주소는 23_10514@daejin.sen.hs.kr 이다')

image_url = "https://www.reddit.com/media?url=https%3A%2F%2Fpreview.redd.it%2Fmy-cat-wakes-me-up-every-morning-but-today-i-woke-him-up-v0-vd3umbwyfmbe1.jpg%3Fwidth%3D640%26crop%3Dsmart%26auto%3Dwebp%26s%3D7a75550c5eaba3ff6c056912f72abd3ec7252b18"
st.image(image_url, use_column_width=True)

st.button("초기화", type="primary")
if st.button("난수 생성"):
    st.write(random.randint(1,1000))
else:
    st.write("잘가")
