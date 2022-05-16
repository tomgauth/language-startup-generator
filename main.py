import streamlit as st
from random import choice, sample, randrange, shuffle

if st.button("Generate A New Language Startup!"):
    st.experimental_rerun()

c = choice

name_prefix = [
    "lingo",
    "ling",
    "language",
    "talk",
    "speak",
    "speech",
    "fluent",
    "trio",
    "e-"

]
name_main = [
    "talk",
    "lingo",
    "lingua",
    "pal",
    "friend",
    "mate",
    "owl",
    "owl",
    "parrot",
    "glot",
    "ai"
]

suffix = [".io",".ai", ".com"]

logo = ["🦉", "💬", "🗯",  "🦜", "👋", "🙊"]

headline_1 = ["Speak ", "Talk ", "Get fluent in ", "Understand ", "Have conversations in ", "Learn "]
headline_2 = ["any language "]
headline_3 = ["like a native ", "in 3 months ", "better ", "in 12 weeks ", "like a child ", "in 90 days "]
headline_4 = ["from day 1", "without learning grammar", "using AI", "in 5 minutes a day", "from the comfort of your home", "online", "during your commute"]

techniques = [
    "absorb the language like a sponge", 
    "learn the 20% you will use 80% of the time", 
    "learn the top 1000 words quickly"
    "learn the most frequent phrases first", 
    "tailored for your needs",
    "learn the language like a child",
    "pronounce like a native",
    "proven method",
    "trusted by polyglots",
    "learn while having fun!",
    "customized learning",
    "learn on the go"
    ]


app_name = f"{c(name_prefix)}{c(name_main)}"

n_benefits = randrange(3, 6)
benefits = sample(techniques, n_benefits)

icons = sample(list("🚀🎯🎁✅🤖🧠🌎💊🔑🕙🗓💪🔥"),n_benefits)

images = sample([
        "https://source.unsplash.com/random/500x500/?language",
        "https://source.unsplash.com/random/500x500/?chatting",
        "https://source.unsplash.com/random/500x500/?travel",
        "https://source.unsplash.com/random/500x500/?study",
        "https://source.unsplash.com/random/500x500/?conversation",
        "https://source.unsplash.com/random/500x500/?learn",
        "https://source.unsplash.com/random/500x500/?words",
        "https://source.unsplash.com/random/500x500/?trip",
        "https://source.unsplash.com/random/500x500/?smart",
        "https://source.unsplash.com/random/500x500/?write",
        "https://source.unsplash.com/random/500x500/?think",
        "https://source.unsplash.com/random/500x500/?woman"],
        4)
        
blog_number = ["3","6","7","12","15","20","50"]
blog_adj = ["best","top","amazing","weird","curious","new","surprising"]
blog_noun = ["French movies to watch", "reasons to learn a language", "reasons to learn Spanish", "ways to learn a language", "Italian movies to watch this weekend", "Reasons you should learn German", "Chinese characters to know", "ways to memorize new words", "podcasts to improve your listening"]
        

st.text(f"{app_name}{c(suffix)}")
st.write("")

st.title(f"{c(logo)} {app_name}")
st.write("")


st.header(f"_{c(headline_1)}{c(headline_2)}{c(headline_3)}{c(headline_4)}_".title())
st.write("")


st.subheader("Benefits")
for i in range(len(benefits)):

    st.subheader(f"{icons[i]} - {benefits[i]}".title())

st.write("")
st.write("")


st.subheader("Latest from the Blog")
col1, col2 = st.columns(2)
with col1:
    st.image(f"{images[0]}")
    st.header(f"{c(blog_number)} {c(blog_adj)} {c(blog_noun)}")
    

with col2:
    st.image(f"{images[1]}")
    st.header(f"{c(blog_number)} {c(blog_adj)} {c(blog_noun)}")
    
col3, col4 = st.columns(2)

with col3:    
    st.image(f"{images[2]}")
    st.header(f"{c(blog_number)} {c(blog_adj)} {c(blog_noun)}")

with col4:
    st.image(f"{images[3]}")
    st.header(f"{c(blog_number)} {c(blog_adj)} {c(blog_noun)}")
st.write("")  
st.write("")

st.write('<a target="" href="https://www.malt.fr/profile/tomgauthier" >This is funny, let‘s hire this dev</a>', unsafe_allow_html=True)
st.write('_With the awesomness of <a target="" href="https://uk.linkedin.com/in/krzeminskamarta" >Marta K.</a>_', unsafe_allow_html=True)