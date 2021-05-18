
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






def intro(chat_id,message_id,bot):
    img="https://raw.githubusercontent.com/AkkuPY/Sara-Bot/main/Assets/Sara_Bot.jpg"
    a='''Heyy I'm Sara, Created By AkkuPY @Akku_Legend  
Type in /notes to know my True Potential!!!'''
    bot.sendChatAction(chat_id=chat_id, action="typing")
    bot.sendPhoto(chat_id=chat_id, photo=img, caption=a,reply_to_message_id = message_id)



def note(chat_id,message_id,bot):
    b='''Here Are The List Of Features Currently I Have.
Type in /<Command> To get the desired result.
                             
->wiki <Name> : Search The Wikipedia About Anything
->yt_music <Name> : YT Mp3 Music Converter

More Are On the way!              
Admin:@Akku_Legend '''
    bot.sendChatAction(chat_id=chat_id, action="typing")
    bot.sendMessage(chat_id=chat_id, text=b, reply_to_message_id=message_id)
