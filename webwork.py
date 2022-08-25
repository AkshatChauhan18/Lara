import webbrowser
def open_website(url:str):
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
    webbrowser.get('chrome').open(url)
def search_query(query:str):
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
    webbrowser.get('chrome').open(f"google.com/search?q={query}")
