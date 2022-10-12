program = "OverLock"

import PySimpleGUI.PySimpleGUI as GUI
import os
import shutil
import pyshortcuts

GUI.theme("SystemDefaultForReal")   # Add a touch of color

defaultFolder = os.popen("echo %localappdata%\Programs").read().replace("\\", "/")[:-1]


layout = [[GUI.Text()],
        [GUI.Text('Install to'), GUI.In(size=(40,1), key='-FOLDER-', default_text=defaultFolder), GUI.Text('/'), GUI.In(size=(15,1), key='-SUBF-', default_text=program), GUI.FolderBrowse(target=(GUI.ThisRow,1), initial_folder=defaultFolder)],
        [GUI.Button('Install')],
        [GUI.Text()]]



window = GUI.Window(f"H4Installer - {program}", layout, element_justification='c')

while True:
    event, values = window.read()

    if event in (GUI.WIN_CLOSED, 'Exit'):
        break
    if event == 'Install':
        folder = values['-FOLDER-'] + '/' + values['-SUBF-']
        print(folder)

        if os.path.exists(folder) and os.path.isdir(folder):
            shutil.rmtree(folder)
        shutil.copytree(f'{os.path.dirname(__file__)}', folder)
    	
        pyshortcuts.make_shortcut(f"{folder}/main.exe", name=f"{program}", startmenu=True, desktop=False, icon=f"{folder}/Source/{program}.ico")
        window.close()
