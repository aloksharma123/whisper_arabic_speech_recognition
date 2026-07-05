import whisper

print("Loading Whisper model...")

model = whisper.load_model("small")   # you can change to base/medium/large

print("Model loaded successfully!")

def transcribe(audio_path):
    """
    Arabic audio → Arabic text ONLY (no translation)
    """

    result = model.transcribe(
        audio_path,
        task="transcribe",   # VERY IMPORTANT
        language="ar",       # force Arabic
        temperature=0.0      # stable decoding
    )

    return result["text"].strip()