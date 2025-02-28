import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIService:
    def generate_response(self, prompt, conversation_history):
        messages = [{"role": "system", "content": "You are a helpful sales assistant."}]
        messages.extend(conversation_history)
        messages.append({"role": "user", "content": prompt})

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=messages,
        )
        return response.choices[0].message.content
#example use.
#openai_service = OpenAIService()
#response = openai_service.generate_response("Hello, how are you?", [{"role": "assistant", "content": "I am doing well"}])
#print(response)