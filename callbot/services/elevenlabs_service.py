import os
from dotenv import load_dotenv
from elevenlabs import generate, set_api_key

load_dotenv()

class ElevenLabsService:
    def __init__(self):
        set_api_key(os.getenv("ELEVENLABS_API_KEY"))

    def text_to_speech(self, text, voice="Bella", model="eleven_monolingual_v1"): #voice and model can be changed.
        try:
            audio = generate(text=text, voice=voice, model=model)
            return audio
        except Exception as e:
            print(f"ElevenLabs TTS error: {e}")
            return None

    def save_audio(self, audio, file_path):
        with open(file_path, "wb") as f:
            f.write(audio)

#example use.
#elevenlabs_service = ElevenLabsService()
#audio = elevenlabs_service.text_to_speech("Hello, this is a test.")
#if audio:
#    elevenlabs_service.save_audio(audio, "output.wav")