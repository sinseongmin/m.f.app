import streamlit as st
import random

st.title("나의 첫번째 앱")
st.text('／n／n')
st.write('안녕하시오. 나는 □□이다')
st.write('나의 이메일 주소는 23_10514@daejin.sen.hs.kr 이다')

st.markdown(
    """
    <style>
    .highlight-text {
        color: red;
        font-weight: bold;
        font-size: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.button("초기화", type="primary")
if st.button("난수 생성"):
    st.write(random.randint(1,1000))
else:
    st.write("잘가")
