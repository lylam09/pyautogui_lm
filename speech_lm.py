import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What's your favorite color?")


answer = pg.prompt("Enter your favorite color below.")


if answer == "blue":
    speak.Speak("Wow, my favorite color is blue too!")

elif answer == "purple":
    speak.Speak("I kinda like purple I guess")

else:
    speak.Speak("Your favorite color is " + answer)

speak.Speak("What's your favorite animal?")

animal = pg.prompt("Enter your favorite animal below.")

speak.Speak("Aight, let's look for funny " + animal + " videos.")

wb.open("https://www.youtube.com/results?search_query=funny " + animal)
