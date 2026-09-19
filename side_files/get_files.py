import tkinter as tk
from tkinter import filedialog
import packages.variables as variables
from .sample import Sample


def get_files():
    root = tk.Tk()
    root.withdraw()


    if variables.background_sample.path == "":
        path = filedialog.askopenfilename(
            title = "Choose a background sample",
            filetypes=[("Audio files", "*.wav *.mp3"),
                        ("WAV files", "*.wav"),
                        ("MP3 files", "*.mp3"),
                        ("All files", "*.*")])

        if path:
            variables.background_sample.path = path

            background_sample_name = ""
            path = path[::-1]
            for letter in path:
                if letter != "/":
                    background_sample_name += letter
                else:
                    break

            background_sample_name = background_sample_name[::-1][:-4]
            if len(background_sample_name) > 21:
                background_sample_name = f"{background_sample_name[:21]}.."
            variables.background_sample.name = background_sample_name
        
    else:
        paths = filedialog.askopenfilenames(
            title = "Choose a background sample",
            filetypes=[("Audio files", "*.wav *.mp3"),
                        ("WAV files", "*.wav"),
                        ("MP3 files", "*.mp3"),
                        ("All files", "*.*")])
        if paths:
            for path in paths:
                Sample(path, len(Sample.samples)+1)
    
    root.destroy()


