from pytube import Playlist

py = Playlist(input("Enter the Url: "))

print(f"Downloading : {py.title} ")

for video in py.videos:
    video.streams.first().download()
    print('Downloading Completed')