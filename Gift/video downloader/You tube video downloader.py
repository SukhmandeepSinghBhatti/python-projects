from pytube import YouTube

link = input('Enter the Url here: ')

YouTube_1 = YouTube(link)

videos = YouTube_1.streams.all()

vid =list(enumerate(videos))

for i in vid:
    print(i)

print()

strm = int(input("Enter: "))

videos[strm].download()
print("Video Sucessfully Downloaded")