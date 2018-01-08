import pyautogui as pg
import time 

pg.hotkey('ctrl', 'n')
time.sleep(3) 
pg.typewrite('Hello.\n', .5)

pg.hotkey('ctrl', 'shift', 's')
pg.hotkey('up','up','up\n')

pg.typewrite('hello_lm\n', .5)

pg.hotkey('shift', 'tab')
pg.hotkey('enter')


