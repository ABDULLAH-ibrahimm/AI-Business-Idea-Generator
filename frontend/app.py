import streamlit as st
import requests

st.title("AI Business Idea Generator")

industry = st.text_input("Enter your niche/industry:")

if st.button("Generate Ideas"):
    if industry.strip() == "":
        st.error("Please enter an industry before generating ideas.")
    else:
        res = requests.post("http://localhost:8000/generate/", data={"industry": industry})
        ideas = res.json().get("ideas", "Error generating ideas.")
        st.subheader("Generated Business Ideas:")
        st.write(ideas)
