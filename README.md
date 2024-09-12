# Google_Text-to-Speech Converter

This is a simple Text-to-Speech converter application built with Python and Tkinter. It allows users to input text, select a language, and convert the text to speech. The application also provides options to play the generated audio and save it as an MP3 file.

## Features

- Convert text to speech in multiple languages (English, French, Spanish, German, Italian)
- User-friendly graphical interface
- Play generated audio directly from the application
- Save generated audio as MP3 files
- Real-time status updates and error handling

## Requirements

- Python 3.6 or higher
- tkinter (usually comes pre-installed with Python)
- gTTS (Google Text-to-Speech)
- pygame

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/text-to-speech-converter.git
   cd text-to-speech-converter
   ```

2. Install the required packages:
   ```
   pip install gtts pygame
   ```

## Usage

1. Run the script:
   ```
   python tts_app.py
   ```

2. The application window will open.

3. Enter the text you want to convert in the text box.

4. Select the desired language from the dropdown menu.

5. Click the "Convert to Speech" button.

6. Once conversion is complete, you can:
   - Click "Play" to listen to the audio
   - Click "Save" to save the audio as an MP3 file

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/text-to-speech-converter/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgments

- Google Text-to-Speech (gTTS) library
- Pygame for audio playback
- Tkinter for the graphical user interface
