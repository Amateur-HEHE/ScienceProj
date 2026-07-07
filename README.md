# 🖐️ GestureSpeak — Real-Time Hand Gesture Recognition

Recognizes hand gestures live from your webcam, shows the result on screen,
speaks it out loud, and includes a gesture reference gallery — all in an
attractive Streamlit web app.

**Tech stack:** Python · OpenCV · MediaPipe · Streamlit · streamlit-webrtc · Text-to-Speech

---

## 📁 Project Structure

```
gesture_app/
├── app.py                      # Home page (entry point)
├── pages/
│   ├── 1_Live_Detection.py     # Webcam gesture detection + voice
│   └── 2_Gesture_Gallery.py    # Reference gallery of all gestures
├── gesture_utils.py            # MediaPipe hand tracking + classification rules
├── gestures_data.py            # Gesture names, meanings, tips
├── style_utils.py              # Shared custom CSS for the UI
├── local_desktop_app.py        # Optional: plain OpenCV window, no browser
├── requirements.txt
├── .streamlit/config.toml      # Theme
└── README.md
```

## ✋ Supported Gestures
Open Palm, Fist, Thumbs Up, Thumbs Down, Peace, Point, OK, I Love You (ASL).
Add more anytime by editing `gesture_utils.py` (add a rule) and
`gestures_data.py` (add the gallery entry).

---

## 🚀 Run Locally

1. **Install Python 3.9–3.11** (MediaPipe doesn't yet support the very latest Python versions — 3.10 is a safe bet).

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
   Your browser opens automatically. Go to **Live Detection** in the sidebar, click **Start**, allow camera access, and show a gesture.

5. **(Optional) Run the simple desktop version instead** (no browser, guaranteed offline voice):
   ```bash
   python local_desktop_app.py
   ```
   Press `q` in the video window to quit.

### 🔊 About the voice
- The main Streamlit app speaks using your **browser's** built-in text-to-speech (`speechSynthesis`), so it works both locally and when deployed online — no server audio setup needed.
- Browsers block auto-playing audio until you've interacted with the page once (click anywhere first), which is a browser security policy, not a bug.
- `local_desktop_app.py` instead uses `pyttsx3`, which speaks offline directly from your machine.

---

## ☁️ Deploy on Streamlit Community Cloud (via GitHub)

1. **Create a GitHub repository** and push this project:
   ```bash
   cd gesture_app
   git init
   git add .
   git commit -m "Initial commit: GestureSpeak app"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo-name>.git
   git push -u origin main
   ```

2. **Go to** [share.streamlit.io](https://share.streamlit.io) and sign in with your GitHub account.

3. Click **"New app"**, then:
   - **Repository:** select `<your-username>/<your-repo-name>`
   - **Branch:** `main`
   - **Main file path:** `app.py`

4. Click **Deploy**. Streamlit Cloud will automatically read `requirements.txt` and install everything.

5. Once deployed, open the app URL, go to **Live Detection**, and allow camera permission in the browser — it will use the *visitor's* webcam (via `streamlit-webrtc`/WebRTC), not the server's, so it works fine for any visitor.

### Notes for cloud deployment
- `streamlit-webrtc` needs a STUN server for the peer connection, which is already configured in `1_Live_Detection.py` using a public Google STUN server — no extra setup needed.
- MediaPipe can be slightly slow to install the first time on Streamlit Cloud's free tier; this is normal and only happens once per deploy.
- If the webcam feed doesn't start, check that your browser has granted camera permission for the app's URL.

---

## 🛠️ Customization Ideas
- Add new gestures: write a new rule in `classify_gesture()` in `gesture_utils.py`, then add a matching entry to `GESTURES` in `gestures_data.py`.
- Swap the color theme in `.streamlit/config.toml` and `style_utils.py`.
- Support two hands: change `max_num_hands=1` to `2` in `get_hands_detector()`.

Enjoy building on top of GestureSpeak! 🚀
