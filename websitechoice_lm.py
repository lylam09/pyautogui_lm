import pyautogui as pg
import time

pg.hotkey('winleft', 'crtl', 'd')
pg.hotkey('winleft')
pg.typewrite('chrome\n', 0.5)

website = pg.prompt('What webstite do you want to visit?')

pg.typewrite((
