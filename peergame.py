import pyautogui as pag
import pandas as pd


print('시작합니다')
#Size(width=2560, height=1600)

pag.PAUSE = 2
pag.moveTo(1700, 195) 
pag.click()
pag.hotkey('ctrl','home')
pag.moveTo(172,468)
pag.click()

#iteration
for i in range(10):
    pag.hotkey('ctrl', 'c')
    pag.hotkey('ctrl', 'tab')
    pag.moveTo(1500,750)
    pag.click()
    pag.moveTo(600,1050)
    pag.doubleClick()
    pag.hotkey('ctrl', 'v')
    pag.hotkey('ctrl', 'shift','tab')
    pag.hotkey('right')
    pag.hotkey('ctrl', 'c')
    pag.hotkey('ctrl', 'tab')
    pag.moveTo(630,1400)
    pag.click()
    pag.click()
    pag.hotkey('ctrl', 'v')
    pag.scroll(-150)  
    pag.confirm(text='보냈습니까?', title='보냈습니까?', buttons=['OK', 'Cancel'])
    pag.size()
    pag.moveTo(2215,375)
    pag.moveTo(2215,375)
    pag.click()
    pag.hotkey('ctrl', 'shift','tab')
    pag.hotkey('left')
    pag.hotkey('down')
