import wikipediaapi
import wikipedia

def wiki(name,chat_id,msg_id,bot):
    try:
        global Sub
        Sub = name

        # Wiki Language
        wiki_wiki = wikipediaapi.Wikipedia('en')

        # Wiki Search
        page_py = wiki_wiki.page(Sub)

        # Check if page is there
        Exist = page_py.exists()
        if Exist is True:
            # Page Title
            Title = page_py.title
            # Content
            Content = Title + '\n' + wikipedia.summary(Sub, sentences=5) + '\n' + page_py.fullurl
            bot.sendChatAction(chat_id=chat_id, action="typing")
            bot.sendMessage(chat_id=chat_id, text=Content, reply_to_message_id=msg_id)
        else:
            bot.sendChatAction(chat_id=chat_id, action="typing")
            bot.sendMessage(chat_id=chat_id, text="Not Found On Wiki", reply_to_message_id=msg_id)
    except:
        bot.sendChatAction(chat_id=chat_id, action="typing")
        bot.sendMessage(chat_id=chat_id, text="Wiki Encountered an Error! Try Again", reply_to_message_id=msg_id)



