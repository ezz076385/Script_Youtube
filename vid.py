from pytube import YouTube
link = input ("Enter Link: ")
yt = YouTube(link)
vid = yt.streams.get_highest_resolution()
vid.download()
print("Done....!")