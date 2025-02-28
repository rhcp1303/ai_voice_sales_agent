from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

class TwilioService:
    def __init__(self):
        self.client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
        self.twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")

    def make_call(self, to_phone_number):
        call = self.client.calls.create(
            to=to_phone_number,
            from_=self.twilio_phone_number,
            url="http://demo.twilio.com/docs/voice.xml",

            # twiml=f'<Response><Dial>{twiml_url}</Dial></Response>'
        )
        print(call.sid)
        return call