from dotenv import load_dotenv
from google import genai
from google.genai import types
import os # Load environment variables from .env file

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents='Why is the sky blue?'
)

print(response.text)