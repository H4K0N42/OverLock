import subprocess
import requests
import sys
import os

downloads = os.popen("echo %userprofile%\Downloads").read().replace("\\", "/")[:-1]

version = requests.get('https://raw.githubusercontent.com/H4K0N42/OverLock/main/Source/.version').content.decode('utf8')


with open('.version', 'r') as f:
    localversion = f.read()
    f.close()

with open('.program', 'r') as f:
    program = f.read()
    f.close()

if localversion != version:
    print("Downloading Update")

    if os.path.exists(f'{downloads}/H4Installer.exe'):
        os.remove(f'{downloads}/H4Installer.exe')
    
    open(f'{downloads}/H4Installer.exe', 'wb').write(requests.get(f'https://github.com/H4K0N42/{program}/releases/download/{version}/H4Installer.exe', allow_redirects=True).content)

    subprocess.Popen(f'{downloads}/H4Installer.exe', shell=True)


sys.exit()