import whisper

print("Loading Whisper model...")

#model = whisper.load_model("base")
model = whisper.load_model("small")

print("Model loaded successfully!")


def transcribe(audio_path, task="transcribe"):
    """
    Transcribe or translate one audio file.

    task="transcribe" -> Arabic text
    task="translate"  -> English translation
    """

    result = model.transcribe(
        audio_path,
        language="ar",
        task=task
    )

    return result["text"]