"""
gesture_utils.py
-----------------
MediaPipe-based hand tracking + rule-based (geometric) gesture classification.

Why rule-based instead of a trained ML model?
- No dataset/training needed -> works out of the box.
- Runs extremely fast (CPU friendly, real-time).
- Easy to extend: add a new "if" rule for any custom gesture.
"""

import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Landmark index reference (MediaPipe Hands, 21 points):
# 0 Wrist
# 1-4   Thumb  (CMC, MCP, IP, TIP)
# 5-8   Index  (MCP, PIP, DIP, TIP)
# 9-12  Middle (MCP, PIP, DIP, TIP)
# 13-16 Ring   (MCP, PIP, DIP, TIP)
# 17-20 Pinky  (MCP, PIP, DIP, TIP)

TIP_IDS = {"index": 8, "middle": 12, "ring": 16, "pinky": 20}
PIP_IDS = {"index": 6, "middle": 10, "ring": 14, "pinky": 18}


def get_hands_detector(max_num_hands=1, min_detection_confidence=0.6, min_tracking_confidence=0.6):
    """Factory for a configured MediaPipe Hands detector."""
    return mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=max_num_hands,
        min_detection_confidence=min_detection_confidence,
        min_tracking_confidence=min_tracking_confidence,
    )


def _finger_states(landmarks, handedness_label):
    """Return a dict of finger_name -> True(extended)/False(curled)."""
    states = {}
    for finger, tip_idx in TIP_IDS.items():
        pip_idx = PIP_IDS[finger]
        # Smaller y = higher up in the image => finger is extended (pointing up)
        states[finger] = landmarks[tip_idx].y < landmarks[pip_idx].y

    # Thumb moves sideways, so we compare x instead of y, and the direction
    # depends on which hand it is (mirrored webcam view).
    if handedness_label == "Right":
        states["thumb"] = landmarks[4].x < landmarks[3].x
    else:
        states["thumb"] = landmarks[4].x > landmarks[3].x

    return states


def classify_gesture(landmarks, handedness_label):
    """
    Classify a single hand's 21 landmarks into one of the supported gesture
    labels. Returns "Unknown" if no rule matches confidently.

    `landmarks` should be the .landmark list from a MediaPipe HandLandmarks
    result (normalized 0-1 coordinates).
    """
    f = _finger_states(landmarks, handedness_label)
    thumb, index, middle, ring, pinky = (
        f["thumb"], f["index"], f["middle"], f["ring"], f["pinky"]
    )

    thumb_tip_y = landmarks[4].y
    thumb_mcp_y = landmarks[2].y

    # --- OK sign: thumb tip and index tip pinched together, others extended
    dist_thumb_index = (
        (landmarks[4].x - landmarks[8].x) ** 2 + (landmarks[4].y - landmarks[8].y) ** 2
    ) ** 0.5
    if dist_thumb_index < 0.06 and middle and ring and pinky:
        return "OK 👌"

    # --- All four fingers curled: check thumb direction for up/down/fist
    if not index and not middle and not ring and not pinky:
        if thumb_tip_y < thumb_mcp_y - 0.06:
            return "I Agree 👍"
        elif thumb_tip_y > thumb_mcp_y + 0.06:
            return "Nope 👎"
        else:
            return "Help ✊"

    # --- Peace / Victory
    if index and middle and not ring and not pinky and not thumb:
        return "Victory ✌️"

    # --- I Love You (ASL): thumb + index + pinky, no middle/ring
    if thumb and index and pinky and not middle and not ring:
        return "Love You Sir Ji 🤟"

    # --- Single pointing finger
    if index and not middle and not ring and not pinky:
        return "Attention ☝️"

    # --- Open palm: everything extended
    if thumb and index and middle and ring and pinky:
        return "Hello ✋"

    return "Unknown"
