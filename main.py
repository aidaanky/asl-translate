import os
from tkinter import *
import speech_recognition as sr
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Global variable to store recognized speech text
recognized_text = ""

# Set up microphone input (device_index might need to be adjusted)
mic = sr.Microphone(device_index=1)

# Function to recognize speech and extract text from audio
def obtain_audio():
    global recognized_text
    recognizer = sr.Recognizer()

    with mic as source:
        print("Say something...")
        audio = recognizer.listen(source)

    try:
        # Recognize speech using Google's API (set language as needed)
        recognized_text = recognizer.recognize_google(audio, language='en-US')
        print(f"You said: {recognized_text}")
    except sr.UnknownValueError:
        print("Speech recognition could not understand the audio.")
        return
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return

    textbox.delete(0, END)
    textbox.insert(0, recognized_text)

# Function to convert recognized text to video
def translate_to_video():
    global recognized_text

    # Fetch text from the textbox
    recognized_text = textbox.get().lower()

    # Clean up punctuation and symbols
    for char in ['.', ',', '?', '!', ';']:
        recognized_text = recognized_text.replace(char, "")
    recognized_text = recognized_text.replace("&", "and")

    # Split text into individual words
    words = recognized_text.split()

    # Create the video by concatenating matching clips from the database
    try:
        result_clip = VideoFileClip(f'database/{words[0]}.mp4')
        for word in words[1:]:
            next_clip = VideoFileClip(f'database/{word}.mp4')
            result_clip = concatenate_videoclips([result_clip, next_clip])

        # Export final video
        output_path = 'result/result.mp4'
        result_clip.write_videofile(output_path)

        # Automatically open the resulting video
        os.startfile(os.path.abspath(output_path))
    except Exception as e:
        print(f"Error creating video: {e}")

# GUI setup
root = Tk()
root.configure(bg='#fafafa')
root.title("English to ASL Translator")
root.geometry("400x300")
root.resizable(width=True, height=True)

# Title Frame
title_frame = Frame(root, bg='#999ac6')
title_frame.place(relx=0, rely=0, relwidth=1, relheight=0.2)

title_label = Label(title_frame, text='ASL Translator', font=('Arial', 20), bg='#999ac6')
title_label.pack(pady=10)

# Main Working Frame
main_frame = Frame(root, bg='#8bacf')
main_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

# Textbox for user input
textbox = Entry(main_frame, bg='white', font=('Arial', 14))
textbox.place(relx=0.1, rely=0.1, relwidth=0.8)

# Button to record voice
record_button = Button(
    main_frame,
    text="Record Voice",
    bg='#798071',
    fg='white',
    font=('Arial', 12),
    command=obtain_audio
)
record_button.place(relx=0.1, rely=0.3, relwidth=0.35)

# Button to translate text to video
translate_button = Button(
    main_frame,
    text="Translate",
    bg='#798071',
    fg='white',
    font=('Arial', 12),
    command=translate_to_video
)
translate_button.place(relx=0.55, rely=0.3, relwidth=0.35)

# Start the GUI loop
root.mainloop()
