from pytube import YouTube

if __name__ == "__main__":
    yt = YouTube("https://www.youtube.com/watch?v=GKAtM9xS-fA&ab_channel=ConCherry")
    audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4')
    audio_stream[1].download(output_path='music')
