import webbrowser
import pyautogui as pg

websites1 = ["https://senorsalazarspanishclass.wordpress.com/hw/", "https://senorsalazarspanishclass.wordpress.com/2016/02/18/vocabulario/"]

websites2 = ["https://senorsalazarspanishclass.wordpress.com/2016/02/18/gramatica/", "https://senorsalazarspanishclass.wordpress.com/2016/02/16/cultura/"]

answer = pg.prompt  (
"""
What would you like to do?
a) Do homework and learn vocabulary
b) Learn grammar and read the culture

"""
    )
if answer == "a":
    for i in websites1:
        webbrowser.open(i)

elif answer == "b":
    for i in websites2:
        webbrowser.open(i)
