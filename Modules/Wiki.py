import wikipediaapi
import wikipedia

def wiki(name):
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
            return Content
        else:
            return 'Not Found On Wiki'
    except:
        return "Wiki Encountered an Error! Try Again"



