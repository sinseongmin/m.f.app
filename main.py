import streamlit as st
import random

st.title("나의 첫번째 앱")
st.text('／n／n')
st.write('안녕하시오. 나는 □□이다')
st.write('나의 이메일 주소는 23_10514@daejin.sen.hs.kr 이다')

 colored_text = f"""
    <div style="color: red; font-size: 20px; font-weight: bold;">
        {name}님, 랜덤 숫자는 {random_number}입니다!
    </div>
    """

st.button("초기화", type="primary")
if st.button("난수 생성"):
    st.write(random.randint(1,1000))
else:
    st.write("잘가")
