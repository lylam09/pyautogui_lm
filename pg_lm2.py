import pyautogui as pg

pg.hotkey('ctrl', 'winleft', 'd')
pg.hotkey('winleft')
pg.typewrite('chrome\n', 0.5)
pg.hotkey('winleft', 'up')
pg.typewrite('instagram.com\n', 0.1)

pg.hotkey('tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab\n')
