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

rmdir installer /S /Q
mkdir installer
cd installer
pyinstaller --noconfirm --onedir --console --icon "" --add-data "C:/Users/H4K0N/Desktop/GitHub/VInstaLock/compiled;." "C:/Users/H4K0N/Desktop/GitHub/VInstaLock/H4Installer.py"
xcopy /E "C:\Users\H4K0N\Desktop\GitHub\VInstaLock\compiled\installer\dist\main\*" "C:\Users\H4K0N\Desktop\GitHub\VInstaLock\compiled\installer\"
rmdir dist /S /Q
rmdir build /S /Q
del main.spec