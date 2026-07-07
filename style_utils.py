"""
style_utils.py
--------------
Small helper to inject shared custom CSS so every page in this
multi-page Streamlit app looks consistent and polished.
"""

import streamlit as st

CUSTOM_CSS = """
<style>
/* Overall app background */
.stApp {
    background: linear-gradient(160deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
}

/* Headings */
h1, h2, h3 {
    color: #ffffff !important;
    font-family: 'Trebuchet MS', sans-serif;
}

/* Hero title gradient text */
.hero-title {
    font-size: 3rem;
    font-weight: 800;
    background: -webkit-linear-gradient(45deg, #ff6ec4, #7873f5, #4ADEDE);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 0;
}

.hero-subtitle {
    text-align: center;
    color: #d3d3f0;
    font-size: 1.2rem;
    margin-top: 0.3rem;
    margin-bottom: 2rem;
}

/* Gesture / feature cards */
.gesture-card {
    background: rgba(255, 255, 255, 0.07);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 16px;
    padding: 22px;
    text-align: center;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    height: 100%;
}
.gesture-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 8px 24px rgba(120, 115, 245, 0.35);
}
.gesture-emoji {
    font-size: 3.2rem;
}
.gesture-name {
    color: #fff;
    font-size: 1.25rem;
    font-weight: 700;
    margin: 8px 0 4px 0;
}
.gesture-meaning {
    color: #b9b9e0;
    font-size: 0.95rem;
    margin-bottom: 6px;
}
.gesture-tip {
    color: #8f8fbd;
    font-size: 0.82rem;
    font-style: italic;
}

/* Detected gesture live banner */
.detected-banner {
    background: rgba(74, 222, 222, 0.12);
    border: 2px solid #4ADEDE;
    border-radius: 14px;
    padding: 18px;
    text-align: center;
    font-size: 1.8rem;
    font-weight: 800;
    color: #4ADEDE;
    margin-top: 12px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #17162b;
}

/* Buttons */
.stButton>button {
    border-radius: 10px;
    border: 1px solid #7873f5;
    color: white;
    background: linear-gradient(45deg, #7873f5, #4ADEDE);
    font-weight: 600;
}
</style>
"""


def inject_custom_css():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
