import os
import requests
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-70b-chat-hf"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

def recognize_emotion(text):
    prompt = f"Identify the primary emotion in this text. Respond with only one word from the following list: joy, sadness, anger, fear, surprise, disgust, neutral. Text: '{text}'"
    
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 1,
            "temperature": 0.5,
            "top_p": 0.9,
            "do_sample": True,
        }
    }

    response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()[0]['generated_text'].strip()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")