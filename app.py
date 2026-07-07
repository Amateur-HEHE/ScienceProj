import streamlit as st
from style_utils import inject_custom_css
from gestures_data import GESTURES

st.set_page_config(
    page_title="GestureSpeak | Hand Gesture Recognition",
    page_icon="🖐️",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_custom_css()

st.markdown('<div class="hero-title">🖐️ GestureSpeak</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-subtitle">Real-time hand gesture recognition &nbsp;•&nbsp; '
    'Voice feedback &nbsp;•&nbsp; Built with OpenCV, MediaPipe &amp; Streamlit</div>',
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.info(
        "👉 Use the sidebar to open **Live Detection** and try it with your webcam, "
        "or check the **Gesture Gallery** to see every gesture this app understands."
    )

st.markdown("### ✨ What this app does")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(
        '<div class="gesture-card"><div class="gesture-emoji">📷</div>'
        '<div class="gesture-name">Detects</div>'
        '<div class="gesture-meaning">Tracks your hand live from the webcam using '
        'MediaPipe\'s 21-point landmark model.</div></div>',
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        '<div class="gesture-card"><div class="gesture-emoji">🧠</div>'
        '<div class="gesture-name">Classifies</div>'
        '<div class="gesture-meaning">A geometric rule engine instantly recognizes '
        'which gesture you are making — no training required.</div></div>',
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        '<div class="gesture-card"><div class="gesture-emoji">🔊</div>'
        '<div class="gesture-name">Speaks</div>'
        '<div class="gesture-meaning">Announces the detected gesture out loud '
        'right in your browser using text-to-speech.</div></div>',
        unsafe_allow_html=True,
    )

st.markdown("### 🖐️ Gestures supported")
cols = st.columns(4)
for i, g in enumerate(GESTURES):
    with cols[i % 4]:
        st.markdown(
            f'<div class="gesture-card">'
            f'<div class="gesture-emoji">{g["emoji"]}</div>'
            f'<div class="gesture-name">{g["name"]}</div>'
            f'<div class="gesture-meaning">{g["meaning"]}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
        st.markdown("<br>", unsafe_allow_html=True)

st.markdown("---")
st.caption("Built with ❤️ using Python, OpenCV, MediaPipe and Streamlit.")
