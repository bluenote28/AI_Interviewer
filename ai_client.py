
from google import genai
from google.genai import types
from aws_secret import get_secret

class AiBot():
    def __init__(self):
        self.api_key = get_secret()
        self.client = genai.Client(api_key=self.api_key)
        self.model = "gemini-2.0-flash-lite"
        self.system_instruction = "You are a job interviewer. You are interviewing the person for the job."
        self.conversation = {"prompts": [], "answers": [] }
        self.chat = self.client.chats.create(model=self.model, config=types.GenerateContentConfig(system_instruction=self.system_instruction))

    def call_gemini(self, prompt):
        
        response = self.chat.send_message(prompt)

        return response.text