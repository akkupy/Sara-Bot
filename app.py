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


class Reply:
    def __init__(self, chat_id, message_id, message,cmd):
        self.chat_id = chat_id
        self.message_id = message_id
        self.message = message
        self.cmd=cmd

    def para(self):
        cnt = self.cmd
        bot.sendChatAction(chat_id=self.chat_id, action="typing")
        bot.sendMessage(chat_id=self.chat_id, text=cnt, reply_to_message_id=self.message_id)


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id
    text = update.message.text.encode('utf-8').decode()

    if text == "/start":
        welcome = Reply(chat_id, msg_id, text,intro())
        welcome.para()

    if text == "/notes":
        nt=Reply(chat_id,msg_id,text,note())
        nt.para()

    if text[0:5] == "/wiki":
        wk=Reply(chat_id,msg_id,text,wiki(text[6:]))
        wk.para()

    if text[0:9] == "/yt_music":
        yt_music(text[10:],chat_id,msg_id,bot)


        #bot.sendChatAction(chat_id=chat_id, action="typing")
        #bot.send_audio(audio=open(dir, 'rb'), thumb=yt_image, caption=capy, chat_id=chat_id, reply_to_message_id=msg_id)
        #os.remove(yt_image)
        #os.remove(dir)
    # else:
    # try:
    # clear the message we got from any non alphabets
    # text = re.sub(r"\W", "_", text)
    # create the api link for the avatar based on http://avatars.adorable.io/
    # url = "https://api.adorable.io/avatars/285/{}.png".format(text.strip())
    # reply with a photo to the name the user sent,
    # note that you can send photos by url and telegram will fetch it for you
    # bot.sendChatAction(chat_id=chat_id, action="upload_photo")
    # bot.sendPhoto(chat_id=chat_id, photo=url, reply_to_message_id=msg_id)
    # except Exception:
    # if things went wrong
    # bot.sendMessage(chat_id=chat_id, text="There was a problem in the name you used, please enter different name", reply_to_message_id=msg_id)

    return 'ok'


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
