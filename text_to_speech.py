from gtts import gTTS
import os

def text_to_speech(text, filename, language='en'):
    tts = gTTS(text=text, lang=language)
    tts.save(filename)
    print(f"Text has been converted to speech and saved as {filename}")

def list_available_languages():
    # This is a simplified list. gTTS supports many more languages.
    languages = {
        'en': 'English',
        'fr': 'French',
        'es': 'Spanish',
        'de': 'German',
        'it': 'Italian'
    }
    for code, lang in languages.items():
        print(f"{code}: {lang}")

if __name__ == "__main__":
    while True:
        print("\n1. Convert text to speech")
        print("2. List available languages")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            text = input("Enter the text you want to convert to speech: ")
            lang = input("Enter language code (default is 'en'): ") or 'en'
            filename = input("Enter output filename (default is 'output.mp3'): ") or 'output.mp3'
            text_to_speech(text, filename, lang)
            
            # Play the audio file (works on macOS and Linux)
            os.system(f"play {filename}")
        elif choice == '2':
            list_available_languages()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
