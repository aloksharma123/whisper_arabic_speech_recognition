import whisper

print("Loading Whisper model...")

model = whisper.load_model("base")

print("Model loaded successfully!")


def transcribe(audio_path):
    """
    Transcribes one audio file.
    """

    result = model.transcribe(
        audio_path,
        language="ar"
    )

    return result["text"]