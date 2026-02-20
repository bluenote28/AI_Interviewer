
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
from constants import SYSTEM_INSTRUCTION, MODEL

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

class AiBot():
    def __init__(self):
        self.api_key = os.environ.get("GEMINI_API_KEY")
        self.client = genai.Client(api_key=self.api_key)
        self.model = MODEL
        self.system_instruction = SYSTEM_INSTRUCTION
        self.chat = self.client.chats.create(model=self.model, config=types.GenerateContentConfig(thinking_config=types.ThinkingConfig(thinking_budget=1024)))

    def converse(self, prompt):
        
        response = self.chat.send_message(prompt)

        return response.text
    
    def get_job_title_and_company(self, job_text):

        contents = f"Provide the company name and job title in: {job_text}. If there is no company name then just provide the job title. Do not add any other comments. \
        If there is a company name provide it in the form: job title at company name. If there is no company name then just provide the job title"

        try:
            response = self.client.models.generate_content(model=self.model, contents=contents)
            return response.text

        except google.genai.errors.ServerError:
            return Exception("Google is reporting a server error. Please try again later.")
    
    def is_job_description(self, prompt):

        contents = f"Let me know if this is a job description. Simply return 'yes' or 'no' and nothing else: {prompt}"

        try:
            response = self.client.models.generate_content(model=self.model, contents=contents)
            return response.text
        except google.genai.errors.ServerError:
            return Exception("Google is reporting a server error. Please try again later.")

