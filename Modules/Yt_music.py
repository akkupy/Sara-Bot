from youtubesearchpython import VideosSearch
import os
import glob


#     __       _       _           
#    /  \     | |     | | 
#   /    \    | | /\  | | /\   _   _
#  /  /\  \   | |/ /  | |/ /  | | | |  
# /  ____  \  | |\ \  | |\ \  | |_| |
#/__/    \__\ |_| \_\ |_| \_\  \___/
#
# Copyright of Akash, 2021          
# https://www.github.com/AkkuPY     
# https://t.me/Akku_Legend         



def yt_music(song_name, chat_id, msg_id, bot):
    try:
        videosSearch = VideosSearch(song_name, limit=1)

        result = videosSearch.result()
        first_result = result["result"]
        yt_url = first_result[0]["link"]
        yt_title = first_result[0]["title"]
        yt_pub_time = first_result[0]["publishedTime"]
        yt_id = first_result[0]["id"]
        yt_duration = first_result[0]["duration"]

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
            try:
                bot.sendChatAction(chat_id=chat_id, action="upload_audio")
                bot.send_audio(audio=open(dir, 'rb'), caption=capy, chat_id=chat_id, reply_to_message_id=msg_id)
                os.remove(dir)
            except:
                bot.sendMessage(chat_id=chat_id, text="Audio Size is too large,Check the link below",
                                reply_to_message_id=msg_id)
                bot.sendMessage(chat_id=chat_id, text=yt_url, reply_to_message_id=msg_id)
                os.remove(dir)
        elif os.path.exists(dir1):
            try:
                bot.sendChatAction(chat_id=chat_id, action="upload_audio")
                bot.send_audio(audio=open(dir1, 'rb'), caption=capy, chat_id=chat_id, reply_to_message_id=msg_id)
                os.remove(dir1)
            except:
                bot.sendMessage(chat_id=chat_id, text="Audio Size is too large,Check the link below",
                                reply_to_message_id=msg_id)
                bot.sendMessage(chat_id=chat_id, text=yt_url, reply_to_message_id=msg_id)
                os.remove(dir1)

        else:
            bot.sendChatAction(chat_id=chat_id, action="typing")
            bot.sendMessage(chat_id=chat_id, text="Song Not Found!", reply_to_message_id=msg_id)


    except:
        bot.sendChatAction(chat_id=chat_id, action="typing")
        bot.sendMessage(chat_id=chat_id, text="Unable to retreive the Song :( Check out the link", reply_to_message_id=msg_id)
        if yt_url is not "":
            bot.sendMessage(chat_id=chat_id, text=yt_url, reply_to_message_id=msg_id)
