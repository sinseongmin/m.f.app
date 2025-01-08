import streamlit as st
import random

st.title("무작위 나무위키 페이지")
st.text('／n／n')
st.write('안녕하시오. 나는 □□이다')
st.write('나의 이메일 주소는 23_10514@daejin.sen.hs.kr 이다')

image_url = "https://mblogthumb-phinf.pstatic.net/MjAyMjAxMjVfMjIy/MDAxNjQzMTAyOTg1MTc0.iCRKrVZvLQgyEfwKYVyGDQAM5R6Rm8Kbh6KOr9Rc2ykg.8-XafjqGUwLSQIa-G_8L6wonoOGwJBmKqAA0yLIOGWMg.JPEG.minziminzi128/IMG_7373.JPG?type=w800"
st.image(image_url, use_column_width=True)

st.button("초기화", type="primary")

if st.button("난수생성"):
     st.write(random.randint(1,1000))
else:
    st.write("잘가")


import streamlit as st
import random
import webbrowser

# Streamlit 앱 제목
st.title("무작위 나무위키 페이지 열기")

# 무작위 페이지 버튼
if st.button("무작위 페이지 열기"):
    # 나무위키의 무작위 페이지 URL
    random_url = "https://namu.wiki/random"
    
    # 브라우저에서 해당 URL 열기
    webbrowser.open(random_url)
     
    st.success("무작위 페이지를 열었습니다!")
else:
    st.write("버튼을 클릭하여 무작위 나무위키 페이지를 열어보세요!")
