import pyautogui as pg
import time 

pg.hotkey('winleft', 'ctrl', 'd')
pg.hotkey('winleft')
pg.typewrite('idle\n', .5)
pg.hotkey('ctrl', 'n')

pg.typewrite('Hello.\n', .5)

pg.hotkey('ctrl', 'shift', 's')
pg.hotkey('up','up','up\n')

pg.typewrite('hello_lm\n', .5)

pg.hotkey('shift', 'tab')
pg.hotkey('enter')


