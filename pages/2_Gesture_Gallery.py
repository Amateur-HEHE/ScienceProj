import streamlit as st
from gestures_data import GESTURES
from style_utils import inject_custom_css

st.set_page_config(page_title="Gesture Gallery | GestureSpeak", page_icon="📖", layout="wide")
inject_custom_css()

st.markdown('<div class="hero-title">📖 Gesture Gallery</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-subtitle">Every gesture GestureSpeak currently understands, '
    'along with tips on how to form it correctly.</div>',
    unsafe_allow_html=True,
)

search = st.text_input("🔍 Search gestures", placeholder="e.g. peace, thumbs, ok...")

filtered = [
    g for g in GESTURES
    if search.lower() in g["name"].lower() or search.lower() in g["meaning"].lower()
] if search else GESTURES

if not filtered:
    st.warning("No gestures match your search.")
else:
    cols = st.columns(3)
    for i, g in enumerate(filtered):
        with cols[i % 3]:
            st.markdown(
                f'<div class="gesture-card">'
                f'<div class="gesture-emoji">{g["emoji"]}</div>'
                f'<div class="gesture-name">{g["name"]}</div>'
                f'<div class="gesture-meaning">Meaning: {g["meaning"]}</div>'
                f'<div class="gesture-tip">💡 {g["tip"]}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )
            st.markdown("<br>", unsafe_allow_html=True)

st.markdown("---")
st.caption("Want to add a custom gesture? Add a rule in `gesture_utils.py` and an entry in `gestures_data.py`.")
