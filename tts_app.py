#functional GUI application in Python, integrating various libraries to perform text-to-speech conversion.

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog
from gtts import gTTS
import os
import threading
import pygame

class TTSApp:
    def __init__(self, master):
        self.master = master
        master.title("Text-to-Speech Converter")
        master.geometry("600x400")
        master.configure(bg='#f0f0f0')

        style = ttk.Style()
        style.theme_use('clam')

        # Text input
        ttk.Label(master, text="Text Input:", background='#f0f0f0').pack(pady=5)
        self.text_input = scrolledtext.ScrolledText(master, height=10)
        self.text_input.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        # Language selection
        ttk.Label(master, text="Select Language:", background='#f0f0f0').pack(pady=5)
        self.language_var = tk.StringVar()
        self.language_combo = ttk.Combobox(master, textvariable=self.language_var)
        self.language_combo['values'] = ('English (en)', 'French (fr)', 'Spanish (es)', 'German (de)', 'Italian (it)')
        self.language_combo.current(0)
        self.language_combo.pack(pady=5)

        # Buttons
        button_frame = ttk.Frame(master)
        button_frame.pack(pady=10)

        self.convert_button = ttk.Button(button_frame, text="Convert to Speech", command=self.convert_to_speech)
        self.convert_button.pack(side=tk.LEFT, padx=5)

        self.play_button = ttk.Button(button_frame, text="Play", command=self.play_audio, state=tk.DISABLED)
        self.play_button.pack(side=tk.LEFT, padx=5)

        self.save_button = ttk.Button(button_frame, text="Save", command=self.save_audio, state=tk.DISABLED)
        self.save_button.pack(side=tk.LEFT, padx=5)

        # Status label
        self.status_label = ttk.Label(master, text="", background='#f0f0f0')
        self.status_label.pack(pady=10)

        self.audio_file = None
        pygame.mixer.init()

    def convert_to_speech(self):
        text = self.text_input.get("1.0", tk.END).strip()
        lang = self.language_var.get().split('(')[-1].strip(')')  # Extract language code
        self.audio_file = 'temp_audio.mp3'
        
        def convert():
            try:
                tts = gTTS(text=text, lang=lang)
                tts.save(self.audio_file)
                self.master.after(0, self.conversion_complete)
            except Exception as e:
                self.master.after(0, self.show_error, str(e))

        self.status_label.config(text="Converting...")
        threading.Thread(target=convert).start()

    def show_error(self, error_message):
        self.status_label.config(text=f"Error: {error_message}")

    def conversion_complete(self):
        self.status_label.config(text="Conversion successful!")
        self.play_button.config(state=tk.NORMAL)
        self.save_button.config(state=tk.NORMAL)

    def play_audio(self):
        if self.audio_file:
            try:
                pygame.mixer.music.load(self.audio_file)
                pygame.mixer.music.play()
            except Exception as e:
                self.status_label.config(text=f"Error playing audio: {str(e)}")

    def save_audio(self):
        if self.audio_file:
            file_name = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
            if file_name:
                try:
                    os.rename(self.audio_file, file_name)
                    self.status_label.config(text=f"File saved as {file_name}")
                except Exception as e:
                    self.status_label.config(text=f"Error saving file: {str(e)}")

if __name__ == '__main__':
    root = tk.Tk()
    app = TTSApp(root)
    root.mainloop()