# importing
import os
import telegram
from flask import Flask, request
from Modules.Intro_Notes import intro, note
from Modules.Wiki import wiki
from Modules.Yt_music import yt_music
from Modules.credentials import *

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
            intro(chat_id,msg_id,bot)

        if text == "/notes":
            note(chat_id,msg_id,bot)

        if text[0:5] == "/wiki":
            wiki(text[6:],chat_id,msg_id,bot)

        if text[0:9] == "/yt_music":
            yt_music(text[10:], chat_id, msg_id, bot)

        # bot.sendChatAction(chat_id=chat_id, action="upload_photo")
        #bot.sendPhoto(chat_id=chat_id, photo=url,caption="df" reply_to_message_id=msg_id)

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
    app.run(threaded=True)
