# app.py -- Society Donation Receipt Apps Hub
# A simple public landing page linking to each society's donation receipt web app.
# Run with: python -m streamlit run app.py

import base64
import streamlit as st

st.set_page_config(page_title="Society Donation Receipt Apps", page_icon="assets/logo.png", layout="centered")

_logo_b64 = base64.b64encode(open("assets/logo.png", "rb").read()).decode()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(180deg, #f5f8fc 0%, #eef3fa 100%);
}

.hub-header {
    text-align: center;
    padding: 2.4rem 0 1.2rem 0;
}

.hub-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 6rem;
    height: 6rem;
    margin-bottom: 0.6rem;
}
.hub-badge img {
    width: 100%;
    height: 100%;
    object-fit: contain;
}

.hub-title {
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    font-size: 2.1rem;
    letter-spacing: -0.5px;
    margin: 0.2rem 0 0.5rem 0;
    color: #0f172a;
}

.hub-subtitle {
    font-size: 0.92rem;
    color: #64748b;
    margin-bottom: 0.6rem;
}

.hub-chip {
    display: inline-block;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.6px;
    color: #2563eb;
    background: rgba(37, 99, 235, 0.08);
    border: 1px solid rgba(37, 99, 235, 0.2);
    padding: 0.28rem 0.8rem;
    border-radius: 999px;
    margin-bottom: 1rem;
    text-transform: uppercase;
}

.society-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 1.3rem 1.6rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
    transition: all 0.15s ease;
}
.society-card:hover {
    border-color: #93c5fd;
    box-shadow: 0 8px 24px rgba(37, 99, 235, 0.10);
    transform: translateY(-2px);
}

.society-icon {
    font-size: 1.4rem;
    width: 2.9rem;
    height: 2.9rem;
    min-width: 2.9rem;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #eff6ff;
    border: 1px solid #dbeafe;
    border-radius: 12px;
    margin-right: 1rem;
}

.society-name {
    font-weight: 600;
    font-size: 1.05rem;
    color: #0f172a;
    margin: 0;
}

.society-fullname {
    font-size: 0.8rem;
    color: #64748b;
    margin: 0.15rem 0 0 0;
}

.status-live {
    background: linear-gradient(135deg, #2563eb, #38bdf8);
    color: white;
    padding: 0.5rem 1.2rem;
    border-radius: 10px;
    font-size: 0.82rem;
    font-weight: 600;
    text-decoration: none;
    white-space: nowrap;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
    transition: box-shadow 0.15s ease, transform 0.15s ease;
}
.status-live:hover {
    box-shadow: 0 6px 18px rgba(37, 99, 235, 0.35);
    transform: scale(1.03);
    color: white;
}

.status-soon {
    background: #f1f5f9;
    color: #94a3b8;
    border: 1px solid #e2e8f0;
    padding: 0.5rem 1.2rem;
    border-radius: 10px;
    font-size: 0.82rem;
    font-weight: 600;
    white-space: nowrap;
}

.hub-footer {
    text-align: center;
    color: #94a3b8;
    font-size: 0.78rem;
    margin-top: 2.4rem;
    letter-spacing: 0.2px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="hub-header">
    <div class="hub-badge"><img src="data:image/png;base64,{_logo_b64}"></div>
    <div class="hub-title">Society Donation Receipt Apps</div>
    <div class="hub-subtitle">AI-assisted receipt automation, powered by Autocount</div>
    <div class="hub-chip">⚡ Intelligent Posting &nbsp;·&nbsp; Auto Reconciliation</div>
</div>
""", unsafe_allow_html=True)

SOCIETIES = [
    {
        "name": "DE Penang",
        "full_name": "Persatuan Dhamma Malaysia (Penang Branch)",
        "url": "https://de-penang-receipt-bot-trhdhg2racjgd9jq7aydes.streamlit.app/",
        "status": "live",
        "icon": "☸️",
    },
    {
        "name": "Maha Mangala Charity",
        "full_name": "Maha Mangala Charity",
        "url": "",
        "status": "coming_soon",
        "icon": "🕉️",
    },
]

for soc in SOCIETIES:
    if soc["status"] == "live":
        action_html = f'<a class="status-live" href="{soc["url"]}" target="_blank">Open App →</a>'
    else:
        action_html = '<span class="status-soon">Coming Soon</span>'

    st.markdown(f"""
    <div class="society-card">
        <div style="display:flex; align-items:center;">
            <div class="society-icon">{soc['icon']}</div>
            <div>
                <p class="society-name">{soc['name']}</p>
                <p class="society-fullname">{soc['full_name']}</p>
            </div>
        </div>
        <div>{action_html}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="hub-footer">
    Each society's app has its own separate login and Autocount connection
</div>
""", unsafe_allow_html=True)
