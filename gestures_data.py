"""
gestures_data.py
----------------
Central place holding metadata about every gesture the app recognizes.
Used by:
  - pages/2_Gesture_Gallery.py  (to render the reference page)
  - gesture_utils.py            (labels must match exactly)
"""

GESTURES = [
    {
        "name": "Open Palm",
        "emoji": "✋",
        "label": "Open Palm ✋",
        "meaning": "Stop / Hello / High-five",
        "tip": "Show your palm with all five fingers fully extended and spread.",
    },
    {
        "name": "Fist",
        "emoji": "✊",
        "label": "Fist ✊",
        "meaning": "Power / Solidarity / Stop-motion",
        "tip": "Curl all fingers and thumb into your palm tightly.",
    },
    {
        "name": "Thumbs Up",
        "emoji": "👍",
        "label": "Thumbs Up 👍",
        "meaning": "Approval / Good job / Yes",
        "tip": "Make a fist and point only your thumb straight up.",
    },
    {
        "name": "Thumbs Down",
        "emoji": "👎",
        "label": "Thumbs Down 👎",
        "meaning": "Disapproval / No / Bad",
        "tip": "Make a fist and point only your thumb straight down.",
    },
    {
        "name": "Peace",
        "emoji": "✌️",
        "label": "Peace ✌️",
        "meaning": "Peace / Victory / Two",
        "tip": "Raise your index and middle fingers in a V shape, other fingers curled.",
    },
    {
        "name": "Point",
        "emoji": "☝️",
        "label": "Point ☝️",
        "meaning": "One / Pointing / Attention",
        "tip": "Extend only your index finger, keep the rest curled.",
    },
    {
        "name": "OK",
        "emoji": "👌",
        "label": "OK 👌",
        "meaning": "Okay / All good / Perfect",
        "tip": "Touch your thumb tip and index tip together, other 3 fingers up.",
    },
    {
        "name": "I Love You",
        "emoji": "🤟",
        "label": "I Love You 🤟",
        "meaning": "I Love You (ASL sign)",
        "tip": "Extend thumb, index and pinky, keep middle and ring fingers curled.",
    },
]

# Quick lookup dict: label -> meaning (used if needed elsewhere)
LABEL_TO_MEANING = {g["label"]: g["meaning"] for g in GESTURES}
