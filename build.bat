@echo off
pip install -r requirements.txt
pyinstaller --onefile --uac-admin --icon NONE --name "ParadiseInjector" injector.py
rmdir /s /q build
del /s /q ParadiseInjector.spec
pause