# app.py -- Society Donation Receipt Apps Hub
# A simple public landing page linking to each society's donation receipt web app.
# Run with: python -m streamlit run app.py

import streamlit as st

st.set_page_config(page_title="Society Donation Receipt Apps", page_icon="🏛️", layout="centered")

st.title("Society Donation Receipt Apps")
st.caption("Select a society below to open its Autocount donation receipt web app.")
st.divider()

SOCIETIES = [
    {
        "name": "DE Penang",
        "full_name": "Persatuan Dhamma Malaysia (Malaysia Dhamma Society - Penang Branch)",
        "url": "https://de-penang-receipt-bot-trhdhg2racjgd9jq7aydes.streamlit.app/",
        "status": "live",
    },
    {
        "name": "Maha Mangala Charity",
        "full_name": "Maha Mangala Charity",
        "url": "",
        "status": "coming_soon",
    },
]

for soc in SOCIETIES:
    with st.container(border=True):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.subheader(soc["name"])
            st.caption(soc["full_name"])
        with col2:
            if soc["status"] == "live":
                st.link_button("Open App →", soc["url"], use_container_width=True)
            else:
                st.button("Coming Soon", disabled=True, use_container_width=True)

st.divider()
st.caption("Each society's app has its own separate login and Autocount connection.")
