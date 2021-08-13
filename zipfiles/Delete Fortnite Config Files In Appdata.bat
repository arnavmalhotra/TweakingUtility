@echo off
echo Batch File By Centxe (youtube.com/Centxe)
@echo
del /s /f /q "%localappdata%\FortniteGame"\*.*
@echo
rd /s /q "%localappdata%\FortniteGame"
echo Deleted Folder Successfully, Open Fortnite To Regenerate Files..
pause