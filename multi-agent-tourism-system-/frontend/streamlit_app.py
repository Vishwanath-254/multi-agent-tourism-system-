
import streamlit as st
import requests

st.title("🌍 Multi-Agent Tourism Planner")

place = st.text_input("Enter your destination")

if st.button("Plan My Trip"):
    response = requests.get(
        "http://localhost:8000/tourism",
        params={"place": place, "weather": True, "attractions": True}
    ).json()

    st.success(response["response"])
