import streamlit as st
import os

from stt import transcribe_audio
from intent import detect_intent
from actions import execute_action

# Title
st.title("🎙️ Voice AI Agent")

# Upload audio
audio_file = st.file_uploader("Upload an audio file (.wav or .mp3)", type=["wav", "mp3"])

if audio_file is not None:
    # Save audio temporarily
    temp_path = os.path.join("temp", audio_file.name)

    with open(temp_path, "wb") as f:
        f.write(audio_file.read())

    st.info("Processing audio...")

    # Step 1: Speech-to-Text
    text = transcribe_audio(temp_path)
    st.subheader("📝 Transcribed Text")
    st.write(text)

    # Step 2: Intent Detection
    intent_data = detect_intent(text)
    st.subheader("🧠 Detected Intent")
    st.write(intent_data)

    # Step 3: Execute Action
    result = execute_action(intent_data, text)
    st.subheader("⚙️ Action Result")
    st.write(result)