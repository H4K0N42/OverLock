@echo off

rmdir compiled /S /Q
mkdir compiled
cd compiled
pyinstaller --noconfirm --onedir --console --icon "C:\Users\H4K0N\Desktop\GitHub\OverLock\Source\OverLock.ico" --add-data "C:/Users/H4K0N/Desktop/GitHub/OverLock/Source;." "C:/Users/H4K0N/Desktop/GitHub/OverLock/Source/main.py"
xcopy /E "C:\Users\H4K0N\Desktop\GitHub\OverLock\compiled\dist\main\*" "C:\Users\H4K0N\Desktop\GitHub\OverLock\compiled\"
rmdir dist /S /Q
rmdir build /S /Q
del main.spec
cd ..