import os
from dotenv import load_dotenv
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
import openai
# Load environment variables
load_dotenv()

# Initialize Claude client
claude_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

def recognize_emotion(text, model="claude"):
    if model == "claude":
        prompt = f"{HUMAN_PROMPT}Identify the primary emotion in this text. Respond with only one word from the following list: joy, sadness, anger, fear, surprise, disgust, neutral. Text: '{text}'{AI_PROMPT}"
        response = claude_client.completions.create(
            prompt=prompt,
            max_tokens_to_sample=1,
            model="claude-v1"
        )
        return response.completion.strip()
    elif model == "chatgpt":
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Identify the primary emotion in this text. Respond with only one word from the following list: joy, sadness, anger, fear, surprise, disgust, neutral. Text: '{text}'",
            max_tokens=1,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()
    else:
        raise ValueError("Invalid model specified. Choose 'claude' or 'chatgpt'.")


