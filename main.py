import streamlit as st
from random import choice, sample

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
headline_4 = ["without learning grammar", "using AI", "in 5 minutes a day", "from the comfort of your home", "online", "during your commute"]

techniques = ["absorb the language like a sponge", "with the 80/20 rule", "learn the most frequent phrases first", "tailored for your needs"]

app_name = f"{c(name_prefix)}{c(name_main)}"

benefits = sample(techniques, 3)

st.text(f"{app_name}{c(suffix)}")

st.title(f"{c(logo)} {app_name}")


st.header(f"{c(headline_1)}{c(headline_2)}{c(headline_3)}{c(headline_4)}")


st.subheader(f"🎯 {benefits[0]}")

st.subheader(f"🚀 {benefits[1]}")

st.subheader(f"✅ {benefits[2]}")