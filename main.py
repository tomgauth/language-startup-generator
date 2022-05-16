import streamlit as st
from random import choice, sample, randrange

c = choice

name_prefix = [
    "lingo",
    "ling",
    "language",
    "talk",
    "speak",
    "speech",
    "fluent",
    "trio"

]
name_main = [
    "talk",
    "lingo",
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
    "with the 80/20 rule", 
    "learn the most frequent phrases first", 
    "tailored for your needs",
    "learn the language like a child",
    "pronunce like a native",
    "proven method",
    "trusted by polyglots",
    "learn while having fun!",
    "customized learning",
    "learn on the go"
    ]

app_name = f"{c(name_prefix)}{c(name_main)}"

n_benefits = randrange(3, 6)
benefits = sample(techniques, n_benefits)

st.text(f"{app_name}{c(suffix)}")

st.title(f"{c(logo)} {app_name}")


st.header(f"{c(headline_1)}{c(headline_2)}{c(headline_3)}{c(headline_4)}".title())
st.write("")

icons = sample(list("🚀🎯🎁✅🤖🧠🌎💊🔑🕙🗓💪🔥"),n_benefits)

for i in range(len(benefits)):

    st.subheader(f"{icons[i]} {benefits[i]}".title())
