from pytube import YouTube
from moviepy.editor import *

# Replace with your YouTube URL
video_url = 'https://www.youtube.com/watch?v=ChDof6K--GI'

# Create a YouTube object
yt = YouTube(video_url)

# Get the audio stream
audio_stream = yt.streams.filter(only_audio=True).first()

# Download the audio stream
audio_file = audio_stream.download(output_path='.', filename='my_audio.mp4')

# Convert the downloaded file to MP3
audio_clip = AudioFileClip(audio_file)
audio_clip.write_audiofile("my_audio.mp3")

# Close the audio clip to release resources
audio_clip.close()

# Optional: Remove the original MP4 file if you don't need it
import os
os.remove(audio_file)

print('Audio extraction completed!')