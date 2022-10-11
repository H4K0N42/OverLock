import pyautogui
from win32api import GetSystemMetrics

from GUI import hero
print(f"Selected Hero: {hero}")
print("Locking ...")

location = None
while location == None:
    location = pyautogui.locateOnScreen("button.png", grayscale=True, confidence=0.8)

if 'hero' in locals():
    x, y = GetSystemMetrics(0), GetSystemMetrics(1)

    #Tanks
    if hero == 'D.VA':          x, y = x*0.20, y*0.77
    if hero == 'DOOMFIST':      x, y = x*0.23, y*0.77
    if hero == 'JUNKER QUEEN':  x, y = x*0.26, y*0.77
    if hero == 'ORISA':         x, y = x*0.30, y*0.77
    if hero == 'REINHARDT':     x, y = x*0.33, y*0.77
    if hero == 'ROADHOG':       x, y = x*0.20, y*0.83
    if hero == 'SIGMA':         x, y = x*0.23, y*0.83
    if hero == 'WINSTON':       x, y = x*0.26, y*0.83
    if hero == 'WRECKING BALL': x, y = x*0.30, y*0.83
    if hero == 'ZARYA':         x, y = x*0.33, y*0.83
    #DMGS
    if hero == 'ASHE':          x, y = x*0.42, y*0.77
    if hero == 'CASSIDY':       x, y = x*0.45, y*0.77
    if hero == 'ECHO':          x, y = x*0.48, y*0.77
    if hero == 'GENJI':         x, y = x*0.52, y*0.77
    if hero == 'HANZO':         x, y = x*0.55, y*0.77
    if hero == 'JUNKRAT':       x, y = x*0.58, y*0.77
    if hero == 'MEI':           x, y = x*0.62, y*0.77
    if hero == 'PHARAH':        x, y = x*0.65, y*0.77
    if hero == 'REAPER':        x, y = x*0.42, y*0.83
    if hero == 'SOJOURN':       x, y = x*0.45, y*0.83
    if hero == 'SOLDIER: 76':   x, y = x*0.48, y*0.83
    if hero == 'SOMBRA':        x, y = x*0.52, y*0.83
    if hero == 'SYMMETRA':      x, y = x*0.55, y*0.83
    if hero == 'TORBJÖRN':      x, y = x*0.58, y*0.83
    if hero == 'TRACER':        x, y = x*0.62, y*0.83
    if hero == 'WIDOWMAKER':    x, y = x*0.65, y*0.83
    #Healers
    if hero == 'ANA':           x, y = x*0.74, y*0.77
    if hero == 'BAPTISTE':      x, y = x*0.77, y*0.77
    if hero == 'BRIGITTE':      x, y = x*0.80, y*0.77
    if hero == 'KIRIKO':        x, y = x*0.83, y*0.77
    if hero == 'LÚCIO':         x, y = x*0.74, y*0.83
    if hero == 'MERCY':         x, y = x*0.77, y*0.83
    if hero == 'MOIRA':         x, y = x*0.80, y*0.83
    if hero == 'ZENYATTA':      x, y = x*0.83, y*0.83
    
    pyautogui.click(x, y, 2, 0.1)