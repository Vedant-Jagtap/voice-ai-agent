import whisper
import os

# Load model (only once)
model = whisper.load_model("base")

def transcribe_audio(audio_path):
    try:
        if not os.path.exists(audio_path):
            return "Error: Audio file not found."

        result = model.transcribe(audio_path)
        print(result)   # 👈 add this line
        text = result["text"]

        return text.strip()

    except Exception as e:
        return f"Error during transcription: {str(e)}"