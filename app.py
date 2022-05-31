import streamlit as st
from PIL import Image
from model_predict import *
from streamlit_webrtc import webrtc_streamer

st.title("✨ Welcome ✨")
st.sidebar.title("🎇Choose an options🎇")
choice_options=st.sidebar.selectbox("",('Home','Start webcam','About'))

if choice_options=="Home":
    st.title('👨Face Emotion Recognition using Live Web Camera👩')
    image = Image.open('data/future.jpg')
    st.image(image)
    st.sidebar.subheader("""💎 Face Emotion Recognition is a system used to detect the emotions from face.""")
    st.sidebar.subheader("""💎 Nowadays it is widely used applications.Eg: In zoom meeting we can able to detect the student emotion.""")
    st.sidebar.subheader("""💎 It is very helpful for teachers where they can able to teach based on their students emotion and make class more interactive.""")
if choice_options=="Start webcam":
    st.header("Webcam Live Feed")
    st.write("Click on start to use webcam and detect your face emotion")
    webrtc_streamer(key="example", video_processor_factory=VideoProcessor)
if choice_options=="About":
    st.title('Project Members')
    col1, col2= st.columns(2)
    with col1:
        image_1= Image.open('data/pranay.png')
        st.subheader("Pranaysagar Bhelave")
        st.image(image_1)
        st.write("Email:pranaysagarbhelave@gmail.com")
        st.markdown("""[LinkedIn profile](https://www.linkedin.com/in/pranaysagar-bhelave-a88027b0)""")
    with col2:
        image_2 = Image.open('data/kunal.png')
        st.subheader("Kunal Tembhare")
        st.image(image_2)
        st.write("Email:kunaltembhare003@gmail.com")
        st.markdown("""[LinkedIn profile](https://www.linkedin.com/in/kunal-tembhare-b3727a9a)""")

    col1, col2= st.columns(2)
    with col1:
        image_3 = Image.open('data/ankush.png')
        st.subheader("Ankush Bhandarkar")
        st.image(image_3)
        st.write("Email:ankushbhandarkar397@gmail.com")
        st.markdown("""[LinkedIn profile](https://www.linkedin.com/in/ankush-bhandarkar-b144a768)""")
    with col2:
        pass


