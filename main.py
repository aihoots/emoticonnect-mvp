from src.preprocessor import preprocess_input
from src.emotion_recognizer import recognize_emotion

def main():
    while True:
        user_input = input("Enter your text (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        
        processed_text = preprocess_input(user_input)
        claude_emotion = recognize_emotion(processed_text, model="claude")
        chatgpt_emotion = recognize_emotion(processed_text, model="chatgpt")
        
        print(f"Processed text: {processed_text}")
        print(f"Claude detected emotion: {claude_emotion}")
        print(f"ChatGPT detected emotion: {chatgpt_emotion}")
        print("---")

if __name__ == "__main__":
    main()