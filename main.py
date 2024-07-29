from src.preprocessor import preprocess_input
from src.emotion_recognizer import recognize_emotion

def main():
    while True:
        user_input = input("Enter your text (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        
        processed_text = preprocess_input(user_input)
        emotion = recognize_emotion(processed_text)
        
        print(f"Processed text: {processed_text}")
        print(f"Detected emotion: {emotion}")
        print("---")

if __name__ == "__main__":
    main()