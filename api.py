from flask import Flask, request, send_file, jsonify
from transcribe import transcribe_audio
from nlp import generate_response, parse_intent
from hass_client import call_hass_service
from tts import speak

app = Flask(__name__)

@app.route('/voice', methods=['POST'])
def handle_voice():
    audio = request.files.get('audio')
    if not audio:
        return "No audio file", 400

    audio.save("input.wav")
    text = transcribe_audio("input.wav")
    response_text = generate_response(text)
    intent = parse_intent(response_text)

    if intent:
        call_hass_service(intent)

    output_path = speak(response_text)
    return send_file(output_path, mimetype="audio/wav")

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "running"})
