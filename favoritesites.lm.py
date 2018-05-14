import webbrowser
import pyautogui as pg

videos = ["https://www.youtube.com/watch?v=Zi2pKmW9vzI", "https://www.youtube.com/watch?v=Nk6XEsqp03c"]

tvshows = ["https://www.youtube.com/watch?v=hPKvFVYEOKg", "https://www.youtube.com/watch?v=bvEnlf9g4co"]

answer = pg.prompt  (
"""
What would you like to do?
a) watch videos
b) watch tv shows

"""
    )
if answer == "a":
    for i in videos:
        webbrowser.open(i)

elif answer == "b":
    for i in tvshows:
        webbrowser.open(i)
