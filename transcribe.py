import subprocess

def transcribe_audio(audio_path):
    # Giả lập dùng whisper nhỏ (tiny)
    try:
        import whisper
        model = whisper.load_model("tiny")
        result = model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        return f"Lỗi STT: {str(e)}"
