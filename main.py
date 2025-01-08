import streamlit as st
import random

st.title("나의 첫번째 앱")
st.text('／n／n')
st.write('안녕하시오. 나는 □□이다')
st.write('나의 이메일 주소는 23_10514@daejin.sen.hs.kr 이다')

st.title(https://i.namu.wiki/i/DxxnonYmddt8njMYPO0Mogb0eGS-4rxun2-6godbXnMT78C8BXNvYxQZHiVCQ_s64yhi9mCDesCzdi0Ods-F5tEr_Z3ccQUw7rzBJAUYZNlckDwafJZBW_-WOSbAOm9hHGWOuGsUxUNqbaOQ6XXU2w.webp)

st.button("초기화", type="primary")
if st.button("난수 생성"):
    st.write(random.randint(1,1000))
else:
    st.write("잘가")
