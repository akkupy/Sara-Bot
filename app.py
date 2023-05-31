# importing
import telegram
from flask import Flask, request
from dotenv import load_dotenv,find_dotenv

#     __       _       _           
#    /  \     | |     | | 
#   /    \    | | /\  | | /\   _   _
#  /  /\  \   | |/ /  | |/ /  | | | |  
# /  ____  \  | |\ \  | |\ \  | |_| |
#/__/    \__\ |_| \_\ |_| \_\  \___/
#
# Copyright of Akash, 2021          
# https://www.github.com/akkupy     
# https://t.me/akkupy  


import os

load_dotenv(find_dotenv())

bot_token = os.getenv("BOT_TOKEN")
bot_user_name = os.getenv("BOT_NAME")
URL = os.getenv("URL")


global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)



@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    try:
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        chat_id = update.message.chat.id
        msg_id = update.message.message_id
        text = update.message.text.encode('utf-8').decode()

        if text == "/start":
            from Modules.Intro_Notes import intro
            intro(chat_id,msg_id,bot)

        if text == "/notes":
            from Modules.Intro_Notes import note
            note(chat_id,msg_id,bot)

        if text[0:5] == "/wiki":
            from Modules.Wiki import wiki
            wiki(text[6:],chat_id,msg_id,bot)

        if text[0:9] == "/yt_music":
            from Modules.Yt_music import yt_music
            yt_music(text[10:], chat_id, msg_id, bot)

        return 'ok'
    except:
        bot.sendMessage(chat_id=chat_id, text="Something Fishy.. Give another Try", reply_to_message_id=msg_id)



@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    return 'Sara Is Alive :)'


if __name__ == '__main__':
    app.run(threaded=True,port=80)
