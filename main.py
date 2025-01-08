import streamlit as st
import random

st.title("나의 첫번째 앱")
#st.text('／n／n')
#st.write('안녕하시오. 나는 □□이다')
#st.write('나의 이메일 주소는 23_10514@daejin.sen.hs.kr 이다')

image_url = "https://mblogthumb-phinf.pstatic.net/MjAyMjAxMjVfMjIy/MDAxNjQzMTAyOTg1MTc0.iCRKrVZvLQgyEfwKYVyGDQAM5R6Rm8Kbh6KOr9Rc2ykg.8-XafjqGUwLSQIa-G_8L6wonoOGwJBmKqAA0yLIOGWMg.JPEG.minziminzi128/IMG_7373.JPG?type=w800"
st.image(image_url, use_column_width=True)

st.button("초기화", type="primary")

if st.button("난수생성"):
     st.write(random.randint(1,1000))
else:
    st.write("잘가")


