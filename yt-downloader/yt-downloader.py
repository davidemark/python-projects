from pytube import YouTube

# Replace with your YouTube URL
video_url = 'https://www.youtube.com/watch?v=ChDof6K--GI'
yt = YouTube(video_url)

# Get the highest resolution stream
stream = yt.streams.get_highest_resolution()

# Download the video
stream.download(output_path='.', filename='my_video.mp4')

print('Download completed!')
