import os
import sys
import PySimpleGUI as GUI

selflocation = os.path.dirname(os.path.realpath(__file__))

GUI.LOOK_AND_FEEL_TABLE['H4Theme'] = {'BACKGROUND': '#292929',
                                        'TEXT': '#FFFFFF',
                                        'INPUT': '#494949',
                                        'TEXT_INPUT': '#FFFFFF',
                                        'SCROLL': '#191919',
                                        'BUTTON': ('#191919', '#494949'),
                                        'PROGRESS': ('#191919', '#494949'),
                                        'BORDER': 2, 'SLIDER_DEPTH': 0, 
                                        'PROGRESS_DEPTH': 0}
#GUI.theme("SystemDefaultForReal")
GUI.theme("H4Theme")

heros = [
    "--TANKS--", '',
            'D.VA', 'DOOMFIST', 'JUNKER QUEEN', 'ORISA', 'REINHARDT',
            'ROADHOG', 'SIGMA', 'WINSTON', 'WRECKING BALL', 'ZARYA', '',
    "--DMGS--", '',
            'ASHE', 'CASSIDY', 'ECHO', 'GENJI', 'HANZO', 'JUNKRAT', 'MEI', 'PHARAH',
            'REAPER','SOLDIER: 76','SOMBRA','SYMMETRA','TORBJÖRN','TRACER','WIDOWMAKER', '',
    "--HEALERS--", '',
            'ANA', 'BAPTISTE', 'BRIGITTE', 'KIRIKO',
            'LÚCIO', 'MERCY', 'MOIRA', 'ZENYATTA']

lasthero = ""
if os.path.exists(f'{selflocation}/.lasthero'):
    with open(f'{selflocation}/.lasthero', 'r') as f:
        lasthero = f.read()


layout = [[GUI.Text()],
        [GUI.Text('Instalock Hero')],
        [GUI.DropDown(heros, lasthero, key='-HERO-')],
        [GUI.Button('Lock Hero (One Round)')],
        [GUI.Text()]]

window = GUI.Window(title=f"VInstaLock", layout=layout, element_justification='c', size=(300, 150))


while True:
    event, values = window.read()

    if event in (GUI.WIN_CLOSED, 'Exit'):
        sys.exit()
        
    hero = values['-HERO-']
    hero = hero.upper()
    if hero not in heros: continue   
    if hero == "": continue 
    if hero == "--TANKS--": continue
    if hero == "--DMGS--": continue
    if hero == "--HEALERS--": continue


    if event == 'Lock Hero (One Round)':
        break

window.close()

with open(f'{selflocation}/.lasthero', 'w') as f:
    f.write(hero)
