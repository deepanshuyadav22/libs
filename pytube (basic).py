from pytube import YouTube

path = "E:/"
yt = YouTube("https://www.youtube.com/watch?v=Ju3zDvV_xzQ")

print("Title: " + yt.title)
print("\nDuration: " + str(yt.length) + "seconds")
print("\nThumbnail Link: " + yt.thumbnail_url)
print("\nDescription: " + yt.description)
print("\nViews: " + str(yt.views))
print("\nAge Restricted: " + "No" if yt.age_restricted == False else "Yes")
print("\nVideo ID: " + yt.video_id)

yt.streams.first().download(path)
