# Help people learn to dance

import pyautogui as pg
import webbrowser
import time

answer = pg.prompt(
"""
Which style of dance would you learn how to do?

a) Ballet
b) Jazz
c) Hip hop
d) Contemporary
e) Tap


"""
    )

if answer == "a":
    webbrowser.open("https://www.youtube.com/watch?v=b3bawTEPLtA")

elif answer == "b":
    webbrowser.open("https://www.youtube.com/watch?v=wvvP07WefNc")

elif answer == "c":
    webbrowser.open("https://www.youtube.com/watch?v=CQpBfEhF9Uc")

elif answer == "d":
    webbrowser.open("https://www.youtube.com/watch?v=fRxbHcdeKNI")

elif answer == "e":
    webbrowser.open("https://www.youtube.com/watch?v=LH_EyxsupRE")


answer = pg.prompt(
"""
Which style of dance would you buy shoes for?

a) Ballet
b) Jazz
c) Hip hop
d) Contemporary
e) Tap


"""
    )

if answer == "a":
    webbrowser.open("https://www.capezio.com/women/shoes/ballet-slippers/leather-juliet")

elif answer == "b":
    webbrowser.open("https://www.capezio.com/women/shoes/jazz-shoes/split-sole-jazz-ankle-boot")

elif answer == "c":
    webbrowser.open("https://store.nike.com/us/en_us/pd/converse-chuck-taylor-all-star-high-top-unisex-shoe/pid-11214171/pgid-11593146")

elif answer == "d":
    webbrowser.open("https://www.capezio.com/pirouette-ii")

elif answer == "e":
    webbrowser.open("https://www.capezio.com/fluid-tap")


answer = pg.prompt(
"""
Which store would you like to buy dance clothes from?

a) Lulu Lemon
b) Athleta
c) Beam and Barre
d) Nike
e) Adidas


"""
    )

if answer == "a":
    webbrowser.open("https://shop.lululemon.com/?&CID=GOOGLE_Fetch_BRAND_A165_A822_C035098&gclid=EAIaIQobChMIl8G-w4a_2gIVSQeGCh0a-AK4EAAYASAAEgLQBvD_BwE&gclsrc=aw.ds")

elif answer == "b":
    webbrowser.open("https://athleta.gap.com/")

elif answer == "c":
    webbrowser.open("http://www.beamandbarre.com/")

elif answer == "d":
    webbrowser.open("https://www.nike.com/us/en_us/c/women?cp=usns_kw_nike_null_txt!g!c!br!e!nike&k_clickid=38334b77-c942-493b-8b92-7e918330fe6c")

elif answer == "e":
    webbrowser.open("https://www.adidas.com/us?cm_mmc=AdieSEM_Google-_-adidas-Trademark-General-B-Exact-_-Trademark-X-X-General-_-adidas&cm_mmca1=US&cm_mmca2=e&gclid=EAIaIQobChMIptS1lYe_2gIVxGSGCh3bHQ5KEAAYASAAEgK7b_D_BwE&gclsrc=aw.ds&dclid=CO252JaHv9oCFe2_swodc7AERg")


answer = pg.prompt(
"""
What level of dance would you be interested in taking?

a) Beginner
b) Intermediate
c) Advanced 



"""
    )

if answer == "a":
    webbrowser.open("https://www.google.com/search?q=beginner+dance+classes+near+me&rlz=1C1GCEA_enUS752US752&oq=beginner+dance+classes+near+me&aqs=chrome..69i57j0l4.4752j0j7&sourceid=chrome&ie=UTF-8")

elif answer == "b":
    webbrowser.open("https://www.google.com/search?q=intermediate+dance+classes+near+me&rlz=1C1GCEA_enUS752US752&oq=intermediate+dance+classes+&aqs=chrome.1.69i57j0l5.6465j1j7&sourceid=chrome&ie=UTF-8")

elif answer == "c":
    webbrowser.open("https://www.google.com/search?q=advanced+dance+classes+near+me&rlz=1C1GCEA_enUS752US752&oq=advanced+dance+classes+near+me&aqs=chrome..69i57.9367j0j9&sourceid=chrome&ie=UTF-8")

