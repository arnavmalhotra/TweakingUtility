import subprocess
import requests
import os
from zipfile import ZipFile
hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
r = requests.get("https://pastebin.com/raw/yourrawlinkhere")

def extractFile(exactFileName):
    file_name="pswd_file.zip"
    with ZipFile(file_name, 'r') as zip:
        zip.extract(exactFileName,pwd=bytes("datacamp","utf-8"))
def executeFile(fileName):
    extractFile(fileName)
    os.startfile(fileName)
    os.remove(fileName)


if hwid in r.text:
    executeFile("TweakingUtility.exe")
else:
    executeFile("Unregistered.exe")



