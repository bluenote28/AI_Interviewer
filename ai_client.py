
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

class AiBot():
    def __init__(self):
        self.api_key = os.environ.get("GEMINI_API_KEY")
        self.client = genai.Client(api_key=self.api_key)
        self.model = "gemini-2.0-flash-lite"
        self.system_instruction = "You are a job interviewer. You are interviewing the person for the job."
        self.conversation = {"prompts": [], "answers": [] }
        self.chat = self.client.chats.create(model=self.model, config=types.GenerateContentConfig(system_instruction=self.system_instruction))

    def converse(self, prompt):
        
        response = self.chat.send_message(prompt)

        return response.text
    
    def summarize_text(self, job_text):

        contents = f"Summarize this job description in less than one sentence with the company name and title: {job_text}"

        response = self.client.models.generate_content(model=self.model, contents=contents)

        return response.text

