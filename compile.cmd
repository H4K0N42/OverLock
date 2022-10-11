@echo off

rmdir compiled /S /Q
mkdir compiled
cd compiled
pyinstaller --noconfirm --onedir --console --paths="C:/Users/H4K0N/AppData/Roaming/Python/Python310/site-packages/cv2" --icon "" --add-data "C:/Users/H4K0N/Desktop/GitHub/VInstaLock/Source;." "C:/Users/H4K0N/Desktop/GitHub/VInstaLock/Source/main.py"
xcopy /E "C:\Users\H4K0N\Desktop\GitHub\VInstaLock\compiled\dist\main\*" "C:\Users\H4K0N\Desktop\GitHub\VInstaLock\compiled\"
rmdir dist /S /Q
rmdir build /S /Q
del main.spec
cd ..