# asl-translate
# English to ASL Translator

This project is a simple desktop application that translates spoken or typed English into American Sign Language (ASL) by generating a video sequence from individual ASL word clips.

## How It Works

1. The user either types English text or records their voice through a microphone.
2. If voice input is used, the application converts speech to text using Google's Speech Recognition API.
3. The text is cleaned (punctuation removed, all lowercase).
4. Each word in the sentence is matched with a corresponding ASL video clip.
5. All matching video clips are concatenated into one video and played:

   ![tg_image_3910089056](https://github.com/user-attachments/assets/6422a81e-556d-4641-a08e-8d82c9ffbdb6)

   ![tg_image_1404379913](https://github.com/user-attachments/assets/2b51d3bf-20c8-4c04-b1a9-6eaa6916f17c)

   Figure 1-2. 3D character made in Blender that demonstrates ASL signs as an output.

   ![tg_image_3520562522](https://github.com/user-attachments/assets/a3e94334-20ec-433f-8e53-953a9575ba54)

   Figure 3. User interface to input words to transalte.

6. Watch the video as a manual:
  
   https://www.youtube.com/watch?v=0IGXJRZGLAY

## Technology Stack

- **Python**: Core programming language.
- **Tkinter**: GUI for user interaction.
- **SpeechRecognition**: Converts voice to text using Google's Web Speech API.
- **moviepy**: Concatenates video clips into a single output.
- **FFmpeg**: Required by `moviepy` for processing video files.

## Folder Structure

```
project/
│
├── database/          # Folder containing individual ASL word video clips (e.g., hello.mp4)
├── result/            # Folder where the final translated video is saved
├── main.py            # Main application file
└── README.md          # Project description
```

## Setup Instructions

1. Install the required Python packages:
   ```
   pip install speechrecognition moviepy
   ```

2. Ensure FFmpeg is installed and available in your system PATH.

3. Add `.mp4` ASL video files to the `database/` folder. Each file should be named exactly as the corresponding word (e.g., `thank.mp4`, `you.mp4`).

4. Run the application:
   ```
   python main.py
   ```

## Notes

- Only words with corresponding video clips in the `/database` folder will be translated.
- The application assumes that video clips are named in lowercase without punctuation.

## License

This project is intended for educational and demonstrative purposes.
