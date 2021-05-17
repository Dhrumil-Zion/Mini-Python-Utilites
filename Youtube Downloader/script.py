from pytube import YouTube

url ="https://www.youtube.com/watch?v=EJf1x51LvMY&ab_channel=PMRStudio"
video = YouTube(url)


print("Title : {}".format(video.title))

video_info = video.streams.get_highest_resolution()
video_info.download()