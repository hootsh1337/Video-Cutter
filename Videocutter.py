import tkinter as tk
from tkinter import filedialog
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os

# Function to select a video file
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mkv")])
    if file_path:
        entry_video_path.delete(0, tk.END)
        entry_video_path.insert(0, file_path)
        
# Function to select audio file
def open_audio_file():
    file_path_audio = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    
    if file_path_audio:
        entry_sound_path.delete(0, tk.END)
        entry_sound_path.insert(0, file_path_audio)

# Function to trim the video
def trim_video():
    input_file = entry_video_path.get()
    output_file = entry_output_path.get()
    start_time = float(entry_start_time.get())
    end_time = float(entry_end_time.get())

    try:
        video = VideoFileClip(input_file)
        trimmed_video = video.subclip(start_time, end_time)
        trimmed_video.write_videofile(output_file, codec="libx264")
        result_label.config(text="Video trimmed successfully!")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

# Function to add audio to video
def add_audio():
    input_file = entry_video_path.get()
    input_audio_file = entry_sound_path.get()
    output_file = entry_output_path.get()

    try:
        video_clip = VideoFileClip(input_file)
        audio_clip = AudioFileClip(input_audio_file)
        final_clip = video_clip.set_audio(audio_clip)
        final_clip.write_videofile(output_file, codec="libx264")
        result_label.config(text="Added audio to video successfully!")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")


# Create the main window
window = tk.Tk()
window.title("Video Trimmer")

# Create and place widgets

# TEXT LABELS

label_video_path = tk.Label(window, text="Video File:")
label_audio_path = tk.Label(window, text="Audio File:")
label_start_time = tk.Label(window, text="Start Time (in seconds):")
label_end_time = tk.Label(window, text="End Time (in seconds):")
label_output_path = tk.Label(window, text="Output File:")
result_label = tk.Label(window, text="")

label_video_path.grid(row=0, column=0, padx=10, pady=5)
label_audio_path.grid(row=1, column=0, padx=10, pady=5)
label_start_time.grid(row=2, column=0, padx=10, pady=5)
label_end_time.grid(row=3, column=0, padx=10, pady=5)
label_output_path.grid(row=4, column=0, padx=10, pady=5)


# ENTRY BOXES
    
entry_video_path = tk.Entry(window)
entry_sound_path = tk.Entry(window)
entry_start_time = tk.Entry(window)
entry_end_time = tk.Entry(window)
entry_output_path = tk.Entry(window)

entry_video_path.grid(row=0, column=1, columnspan=2, padx=10, pady=5)
entry_sound_path.grid(row=1, column=1, columnspan=2, padx=10, pady=5)
entry_start_time.grid(row=2, column=1, columnspan=2, padx=10, pady=5)
entry_end_time.grid(row=3, column=1, columnspan=2, padx=10, pady=5)
entry_output_path.grid(row=4, column=1, columnspan=2, padx=10, pady=5)

# BUTTONS

button_open = tk.Button(window, text="Open Video File", command=open_file)
button_open_audio = tk.Button(window, text="Open Audio File", command=open_audio_file)
button_trim = tk.Button(window, text="Trim Video", command=trim_video)
button_add_audio = tk.Button(window, text="Add Audio to Video", command=add_audio)

button_open.grid(row=5, column=0, padx=10, pady=10)
button_open_audio.grid(row=5, column=1, padx=10, pady=10)
button_trim.grid(row=5, column=2, padx=10, pady=10)
button_add_audio.grid(row=5, column=3, padx=10, pady=10)

result_label.grid(row=5, column=0, columnspan=3)

window.mainloop()
