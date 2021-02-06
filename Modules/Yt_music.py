from youtubesearchpython import VideosSearch
import os
import wget
import glob
import youtube_dl


def yt_music(song_name):
    try:
        videosSearch = VideosSearch(song_name, limit=1)

        result = videosSearch.result()
        first_result = result["result"]
        yt_url = first_result[0]["link"]
        yt_title = first_result[0]["title"]
        yt_pub_time = first_result[0]["publishedTime"]
        yt_id = first_result[0]["id"]
        yt_duration = first_result[0]["duration"]
        yt_image = f"https://img.youtube.com/vi/{yt_id}/hqdefault.jpg"

        if not os.path.isdir("./Downloads/"):
            os.makedirs("./Downloads/")

        yt_image = wget.download(yt_image, out="./Downloads/")

        if not os.path.isdir("./music/"):
            os.makedirs("./music/")
        yt_song = (
                f'youtube-dl --force-ipv4 -q -o "./music/{yt_title}.%(ext)s" --extract-audio --audio-format mp3 --audio-quality 128k '
                + yt_url
        )

        os.system(yt_song)
        try:
            a = glob.glob("./music/*.webm")
            b = a[0]
            c = b[8:]
        except:
            a = glob.glob("./music/*.mp3")
            b = a[0]
            c = b[8:]
        dir = f"./music/{c}"
        dir1 = f"./music/{c}"
        capy = f"**Song Name ➠** `{yt_title}` \n**Published On ➠** `{yt_pub_time}` \n**Duration ➠** `{yt_duration}` \n**Link ➠** `{yt_url}`"
        if os.path.exists(dir):
            return yt_image, dir, capy
        elif os.path.exists(dir1):
            return yt_image, dir1, capy
        else:
            return "Somethings Wrong!", "Please Try Again", "ee"

    except:
        return "Please Try Again"

