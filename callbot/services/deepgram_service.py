import asyncio
import os
from dotenv import load_dotenv
from deepgram import Deepgram

load_dotenv()

class DeepgramService:
    def __init__(self):
        self.deepgram = Deepgram(os.getenv("DEEPGRAM_API_KEY"))

    async def transcribe_audio(self, audio_file_path):
        with open(audio_file_path, 'rb') as audio:
            source = {'buffer': audio, 'mimetype': 'audio/wav'} #make sure the audio is in wav format.
            options = {'punctuate': True, 'diarize': False}
            try:
                results = await self.deepgram.transcription.prerecorded(source, options)
                transcript = results['results']['channels'][0]['alternatives'][0]['transcript']
                return transcript
            except Exception as e:
                print(f"Deepgram transcription error: {e}")
                return None

#example use.
#async def main():
#    deepgram_service = DeepgramService()
#    transcript = await deepgram_service.transcribe_audio("path/to/your/audio.wav")
#    if transcript:
#       print(f"Transcript: {transcript}")

#if __name__ == "__main__":
#    asyncio.run(main())
