from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()  
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_response(messages):
    try:
        response = client.chat.completions.create(
            messages=messages,
            model="llama-3.1-8b-instant",
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"