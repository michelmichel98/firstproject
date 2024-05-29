from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title= "My Webpage", page_icon=":tada:", layout ="wide" )

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True) 

local_css("style\\style.css")
# ----LOAD ASSETS BABY----
lottie_coding = load_lottieurl("https://lottie.host/18e0a272-7edf-4e31-82df-1f7931866faf/dFqxwEX8Rt.json")
img_coding_languages = Image.open("C:\\Users\\miche\\Bureaublad\\firstproject\\images\\coding.png")
img_udemy = Image.open("C:\\Users\\miche\\Bureaublad\\firstproject\\images\\udemy_logo.png")


#----Header section----
with st.container():
    st.subheader("Hi, I am Michel :wave:")
    st.title("A man from The Netherlands") 
    st.write("I like coding") 
    st.write("[Learn More >](https://facebook.com/yourmom)")

# ---- What I do ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I wake up and depending on what day it is and how many days I've worked from home already, I either go to work or I work from home.
            Work is learning to code, mostly. Apart from that I browse courses such as a course on cyber security. Right now I am waiting for an assignment
            in the business & IT domain. It has been three months or so, that I am now waiting. Am I impatient? I don't think so! I'm keeping myself entertainded and 
            enjoying the time that I have while I'm not necessarily expected anywhere. I am expected at the workplace of the agency for two days a week. I can choose the days myself.
            Apart from working I read. Literature mostly, but also some non-fiction in the form of biography's or history. Other than that I work out. It is
            my guilty pleasure: lifting weights. That's really all of what I do. Except smoking and doing chores around the place I live. I try not to do certain other things also, but failed many times.
            Finally I pray.
            """

        )
        st.write("[LinkedIn page >](https://linkedin.com/michel)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

#----PROJECTS----
with st.container():
    st.write("---")
    st.header("How can YOU learn to code?")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_coding_languages)
    with text_column:
        st.subheader("Learn to code using various resources")
        st.write(
            """
           There are various coding languages you can learn. 
           Among the most popular ones are Python, Java, and C++.
           Programming languages transform binary computer code that most humans can't read, into functional instructions that can then be passed
           back into the computer. In this way, humans can interact with computers to create apps, websites and more, and make computers do what humans want.
            """
        )
        st.markdown("[Learn more about coding](https://www.computerscience.org/resources/what-is-coding-used-for/)")
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_udemy)
    with text_column:
        st.subheader("Python")
        st.write(
            """
            Learn how to code using various resources!
            Anyone can learn how to code in a language they prefer.
            For this instruction, I will refer you to a Python instructor that has been very helpful to me.
            """
        )
        st.markdown("[Course on Udemy](https://www.udemy.com/course/complete-python-bootcamp/?couponCode=KEEPLEARNING)")

#----CONTACT FORM----
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")

    #Documentation: 
    contact_form = """
     <form action="https://www.formbackend.com/f/a22ed7d8165d888b" method="POST">  
        <input type="hidden" name= "_captcha" value="false">
        <input type="text" name="name" placeholder= "Your name "required>
        <input type="email" name="email" placeholder= "Your email" required>
        <textarea name ="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
<!-- Required for hCaptcha -->
<script src="https://web3forms.com/client/script.js" async defer></script>

    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()