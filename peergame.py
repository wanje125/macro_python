import pyautogui as pag
import pandas as pd


print('시작합니다')
#Size(width=1920, height=1080)

pag.PAUSE = 2
pag.moveTo(1000, 100) 
pag.click()
pag.hotkey('ctrl','home')
pag.moveTo(120,290)
pag.click()

#iteration
for i in range(10):
    pag.hotkey('ctrl', 'c')
    pag.hotkey('ctrl', 'tab')
    pag.moveTo(1100,480)
    pag.click()
    pag.moveTo(710,670)
    pag.doubleClick()
    pag.hotkey('ctrl', 'v')
    pag.hotkey('ctrl', 'shift','tab')
    pag.hotkey('right')
    pag.hotkey('ctrl', 'c')
    pag.hotkey('ctrl', 'tab')
    pag.moveTo(710,870)
    pag.click()
    pag.hotkey('ctrl', 'v')
    pag.scroll(-150)  
    pag.confirm(text='보냈습니까?', title='보냈습니까?', buttons=['OK', 'Cancel'])
    pag.moveTo(1707,244)
    pag.click()
    pag.hotkey('ctrl', 'shift','tab')
    pag.hotkey('left')
    pag.hotkey('down')
