import subprocess
import requests
import os
from zipfile import ZipFile
hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
r = requests.get("https://gist.github.com/arnavmalhotra/28f0b021931c064dcd0718d8da71af3b")

def extractFile(exactFileName):
    file_name="pswd_file.zip"
    with ZipFile(file_name, 'r') as zip:
        zip.extract(exactFileName,pwd=bytes("datacamp","utf-8"))
def executeFile(fileName):
    extractFile(fileName)
    os.startfile(fileName)
    os.remove(fileName)


if hwid in r.text:
    os.startfile("TweakingUtility.exe")
else:
    os.startfile("Unregistered.exe")



