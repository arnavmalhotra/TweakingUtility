
import tkinter as tk
from tkinter.constants import DISABLED
from typing import Text
import os
import subprocess
import requests
import webbrowser
import time
from zipfile import ZipFile
homedir = os.path.expanduser("~")
hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
r = requests.get("https://pastebin.com/raw/yourrawlinkhere")


def extractFile(exactFileName):
    file_name=cwd+"\\zipfiles.zip"
    with ZipFile(file_name, 'r') as zip:
        zip.extract(exactFileName,pwd=bytes("datacamp","utf-8"))
    

def showFrame(frame):
    frame.tkraise()

def executeFile(fileName):
    extractFile(fileName)
    os.startfile(fileName)
    os.remove(fileName)




cwd = os.getcwd()
window = tk.Tk()
window.state('zoomed')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
sidebar = tk.Frame(height=390,width=200)




ApplicationsFrame = tk.Frame(window)
ApplicationsFrame_title = tk.Label(ApplicationsFrame, text="This is the Applications Frame").pack()
CleanupFrame = tk.Frame(window)
CleanupFrameLabel = tk.Label(CleanupFrame, text="This is the cleanup frame").pack()
ImportantFrame = tk.Frame(window)
ImportantFrameLabel = tk.Label(ImportantFrame,text="This is the important frame").pack()
FPSFrame = tk.Frame(window)
FPSFrameLabel = tk.Label(FPSFrame,text = "This is the FPS Frame").pack()
ServicesFrame = tk.Frame(window)
ServicesFrameLabel = tk.Label(ServicesFrame,text="This is the services frame").pack()
PingFrame = tk.Frame(window)
PingFrameLabel = tk.Label(PingFrame,text="This is the ping frame").pack()
LatencyFrame = tk.Frame(window)
LatencyFrameLabel = tk.Label(LatencyFrame,text=" This is the latency frame").pack()
PerformanceFrame = tk.Frame(window)
PerformanceFrameLabel = tk.Label(PerformanceFrame,text="This is the performance frame").pack()
AMDFrame = tk.Frame(window)
AMDFrameLabel = tk.Label(AMDFrame,text="This is the AMD Frame").pack()
NVIDIAFrame = tk.Frame(window)
NVIDIAFrameLabel = tk.Label(NVIDIAFrame,text="This is the NVIDIA Frame").pack()
PresetFrame = tk.Frame(window)
PresetFrameLabel = tk.Label(PresetFrame,text="This is the Preset Frame").pack()
MouseFrame = tk.Frame(window)
MouseFrameLabel = tk.Label(MouseFrame, text = "This is the mouse frame").pack()
SoundFrame = tk.Frame(window)
SoundFrameLabel = tk.Label(SoundFrame,text="This is the sound frame").pack()
PowerPlanFrame = tk.Frame(window)
PowerPlanFrameLabel = tk.Label(PowerPlanFrame,text ="This is the power plan frame").pack()
InputDelayFrame = tk.Frame(window)
InputDelayFrameLabel = tk.Label(InputDelayFrame, text = "This is the input delay frame").pack()
Unregistered = tk.Frame(window)
UnregisteredLabel = tk.Label(Unregistered,text="You are not register for the program, but at ww.exe or contact Centxe")



for frame in(ApplicationsFrame,CleanupFrame,ImportantFrame,FPSFrame,ServicesFrame,PingFrame,LatencyFrame,PerformanceFrame,AMDFrame,NVIDIAFrame,PresetFrame,MouseFrame,SoundFrame,PowerPlanFrame,InputDelayFrame):
    frame.grid(row=0,column=0,sticky="nsew")
showFrame(ApplicationsFrame)



#==============================================================================Sidebar===========================================================#
sidebar.grid(row=0,column=1)
sidebar_applications = tk.Button(sidebar,text="Application Tweaks", command = lambda:showFrame(ApplicationsFrame),width=25).pack()
sidebar_cleanupFrame = tk.Button(sidebar,text="Cleanup Tweaks", command = lambda:showFrame(CleanupFrame),width=25).pack()
sidebar_importantFrame = tk.Button(sidebar,text="Important Tweaks", command = lambda:showFrame(ImportantFrame),width=25).pack()
sidebar_fpsIncreaseFrame = tk.Button(sidebar,text="Increase FPS", command = lambda:showFrame(FPSFrame),width=25).pack()
sidebar_disableServicesFrame = tk.Button(sidebar,text="Disable Unnecesary Services", command = lambda:showFrame(ServicesFrame),width=25).pack()
sidebar_lowerPingFrame = tk.Button(sidebar,text="Lower ping", command = lambda:showFrame(PingFrame),width=25).pack()
sidebar_lowLatencyFrame = tk.Button(sidebar,text="Lower Latency Tweaks", command = lambda:showFrame(LatencyFrame),width=25).pack()
sidebar_highPerformance = tk.Button(sidebar,text="High Performance Tweaks", command = lambda:showFrame(PerformanceFrame),width=25).pack()
sidebar_AmdGpuFrame = tk.Button(sidebar,text="AMD GPU Tweaks", command = lambda:showFrame(AMDFrame),width=25).pack()
sidebar_NvidiaGpuFrame = tk.Button(sidebar,text="NVIDIA GPU Tweaks", command = lambda:showFrame(NVIDIAFrame),width=25).pack()
sidebar_gamingPresetFrame = tk.Button(sidebar,text="Gaming Preset", command = lambda:showFrame(PresetFrame),width=25).pack()
sidebar_mouseTweaksFrame = tk.Button(sidebar,text="Mouse Tweaks", command = lambda:showFrame(MouseFrame),width=25).pack()
sidebar_soundTweaksFrame = tk.Button(sidebar,text="Sound Tweaks", command = lambda:showFrame(SoundFrame),width=25).pack()
sidebar_gamingPowerPlanFrame = tk.Button(sidebar,text="Gaming Power Plan", command = lambda:showFrame(PowerPlanFrame),width=25).pack()
sidebar_inputDelayFrame = tk.Button(sidebar,text="Input Delay Tweaks", command = lambda:showFrame(InputDelayFrame),width=25).pack()

def restorePoint():
    executeFile("restorepoint.lnk")
def adwcleaner():
    os.startfile("bin/Adwcleaner.exe")
def cctrialsetup():
    os.startfile("bin/cctrialsetup.exe")
def cleanmgr():
    os.startfile("bin/Cleanmgr+.exe")
def MBsetup():
    os.startfile("bin/MBSetup.exe")
def memreduct():
    os.startfile("bin/memreduct.exe")
def MSIutil():
    os.startfile("bin/MSI_util_v3.exe")
def nvidiaProfileInspector():
    os.startfile("bin/nvidiaProfileInspector.exe")
def parkcontrolsetup():
    os.startfile("bin/parkcontrolsetup64.exe")
def timerresolution():
    os.startfile("bin/TimerResolution.exe")
def updateDirectx():
    os.startfile("bin/Update DirectX.exe")


applicationsBTN1 = tk.Button(ApplicationsFrame,text="Create Restore Point",command=restorePoint).pack()
applicationsBTN2 = tk.Button(ApplicationsFrame,text="Adwcleaner",command=adwcleaner).pack()
applicationsBTN3 = tk.Button(ApplicationsFrame,text="CCtrialSetup",command=cctrialsetup).pack()
applicationsBTN4 = tk.Button(ApplicationsFrame,text="CleanMGR+",command=cleanmgr).pack()
applicationsBTN5 = tk.Button(ApplicationsFrame,text="MBSetup",command=MBsetup).pack()
applicationsBTN6 = tk.Button(ApplicationsFrame,text="Memreduct",command=memreduct).pack()
applicationsBTN7 = tk.Button(ApplicationsFrame,text="MSI Util",command=MSIutil).pack()
applicationsBTN8 = tk.Button(ApplicationsFrame,text="Nvidia Profile Inspector",command=nvidiaProfileInspector).pack()
applicationsBTN9 = tk.Button(ApplicationsFrame,text="Park Control",command=parkcontrolsetup).pack()
applicationsBTN10 = tk.Button(ApplicationsFrame,text="Timer Resolution",command=timerresolution).pack()
applicationsBTN11 = tk.Button(ApplicationsFrame,text="Update DirectX",command=updateDirectx).pack()


def prefetchFiles():
    executeFile("3 Delete Prefetch Files.lnk")
def cacheCleaner():
    executeFile("Cache Cleaner.bat")
def DeleteFortniteConfig():
    executeFile("Delete Fortnite Config Files In Appdata.bat")
def deleteLogFiles():
    executeFile("Delete Log Files.bat")
def deleteTempFiles():
    executeFile("Delete Temporary Files.bat")
def deleteWUCachedfiles():
    executeFile("Delete WU Cached Files.bat")
def disableHPET():
    executeFile("Disable HPET, ST & DT.bat")
def tempcleaner():
    executeFile("TempCleaner.bat")
def diskcleanup():
    executeFile("Disk Cleanup.exe.lnk")


cleanupBTN1 = tk.Button(CleanupFrame,text="Disable Prefetch Files",command=prefetchFiles).pack()
cleanupBTN2 = tk.Button(CleanupFrame,text="Cache Cleaner",command=cacheCleaner).pack()
cleanupBTN3 = tk.Button(CleanupFrame,text="Delete Fortnite Config",command=DeleteFortniteConfig).pack()
cleanupBTN4 = tk.Button(CleanupFrame,text="Delete Log Files",command=deleteLogFiles).pack()
cleanupBTN5 = tk.Button(CleanupFrame,text="Delete Temporary Files",command=deleteTempFiles).pack()
cleanupBTN6 = tk.Button(CleanupFrame,text="Delete WU Cached Files",command=deleteWUCachedfiles).pack()
cleanupBTN7 = tk.Button(CleanupFrame,text="Disable HPET, ST and DT",command=disableHPET).pack()
cleanupBTN8 = tk.Button(CleanupFrame,text="Disk Cleanup",command=diskcleanup).pack()
cleanupBTN9 = tk.Button(CleanupFrame,text="Temp Cleaner",command=tempcleaner).pack()

def restorepointfirstthing():
    executeFile("restorepoint.lnk")
def disableStartupApps():
    executeFile("Disable Startup Apps you dont use.lnk")
def uninstallApps():
    executeFile("Uninstall Apps You Don't Need.lnk")

importantBTN1 = tk.Button(ImportantFrame, text="Create Restore Point",command=restorepointfirstthing).pack()
importantBTN3 = tk.Button(ImportantFrame, text="Disable unnecessary startup apps",command=disableStartupApps).pack()
importantBTN4 = tk.Button(ImportantFrame, text="Uninstall unnecessary apps",command=uninstallApps).pack()


def disablePowerThrottling():
    executeFile("Disable Power Throttling.reg")
def DPPOPT():
    executeFile("DPP OPT.reg")
def gameProfileOptim():
    executeFile("Game Profile Optimization.reg")
def lowerLatency():
    executeFile("Lower Latency.reg")
def normalFnPriority():
    executeFile("Normal Fortnite Priority.reg")
def OptimizeCould():
    executeFile("Optimize Could Content.reg")
def TCPIP():
    executeFile("TCPIP Network Priority.reg")


fpsincreaseBTN1 = tk.Button(FPSFrame,text="Disable Power Throttling",command=disablePowerThrottling).pack()
fpsincreaseBTN2 = tk.Button(FPSFrame,text="DPP OPT",command=DPPOPT).pack()
fpsincreaseBTN3 = tk.Button(FPSFrame,text="Game Profile Optimization",command=gameProfileOptim).pack()
fpsincreaseBTN4 = tk.Button(FPSFrame,text="Lower Latency",command=lowerLatency).pack()
fpsincreaseBTN5 = tk.Button(FPSFrame,text="Normal Fortnite Priority",command=normalFnPriority).pack()
fpsincreaseBTN6 = tk.Button(FPSFrame,text="Optimize could content",command=OptimizeCould).pack()
fpsincreaseBTN7 = tk.Button(FPSFrame,text="TCP IP Network Priority",command=TCPIP).pack()

def disableUAC():
    executeFile("5 Disable UAC.reg")
def disableUpdate():
    executeFile("6 Disable Windows Updates.bat")
def disableDiagnosticsTelemtry():
    executeFile("Disable Diagnostics & Telemetry Services.reg")
def disableExtraServices():
    executeFile("Disable Extra Unnecessary Services.reg")
def disableBluetooth():
    executeFile("OPTIONAL Disable Bluetooth Services.reg")
def disableDownloadMaps():
    executeFile("Optional Disable Download Maps Manager.reg")
def disablePrinterServices():
    executeFile("OPTIONAL Disable Printer Services.reg")
def disableXboxServices():
    executeFile("OPTIONAL Disable Xbox Services.reg")

servicesBTN1 = tk.Button(ServicesFrame,text="Disable UAC",command=disableUAC).pack()
servicesBTN2 = tk.Button(ServicesFrame,text="Disable Updates",command=disableUpdate).pack()
servicesBTN3 = tk.Button(ServicesFrame,text="Disable Diagnostics and Telemetry",command=disableDiagnosticsTelemtry).pack()
servicesBTN4 = tk.Button(ServicesFrame,text="Disable Extra Uneeccesary Services",command=disableExtraServices).pack()
servicesBTN5 = tk.Button(ServicesFrame,text="Disable Bluetooth Service",command=disableBluetooth).pack()
servicesBTN6 = tk.Button(ServicesFrame,text="Disable Download Maps",command=disableDownloadMaps).pack()
servicesBTN7 = tk.Button(ServicesFrame,text="Disable Printer Service",command=disablePrinterServices).pack()
servicesBTN8 = tk.Button(ServicesFrame,text="Disable Xbox Services",command=disableXboxServices).pack()

def deliveryOpt():
    executeFile("Disable Delivery Optimization.reg")
def networkThrottle():
    executeFile("Disable Network Throttling Index.reg")
def OnedriveSync():
    executeFile("Disable OneDrive Sync.reg")
def networkPriorities():
    executeFile("Reinforce Network Priorities.reg")


pingBTN1 = tk.Button(PingFrame,text="Disable Delivery Optimization",command=deliveryOpt).pack()
pingBTN2 = tk.Button(PingFrame,text="Disable Network Throttling Index",command=networkThrottle).pack()
pingBTN3 = tk.Button(PingFrame,text="Disable Onedrive Sync",command=OnedriveSync).pack()
pingBTN4 = tk.Button(PingFrame,text="Reinforce Network Priorities",command=networkPriorities).pack()

def lowestInputLatency():
    executeFile("28 Hex - Lowest Input Latency.reg")

latencyBTN1 = tk.Button(LatencyFrame,text="Lowest Input Latency",command=lowestInputLatency).pack()


def highPerformance():
    executeFile("Default - 26 Hex (Priority To Programs).reg")

performanceBTN1 = tk.Button(PerformanceFrame,text="Highest Performanece",command=highPerformance).pack()

def AMDPriority():
    executeFile("AMD Thread Priority.reg")
AMDBTN1 = tk.Button(AMDFrame,text="AMD thread priority",command=AMDPriority).pack()

def nvidiaButton():
    executeFile("NVIDIA Thread Priority.reg")

NVIDIABTN1 = tk.Button(NVIDIAFrame,text="NVIDIA Thread Priority",command=nvidiaButton).pack()

PresetBTN1 = tk.Button(PresetFrame,text="Button1").pack()
PresetBTN2 = tk.Button(PresetFrame,text="Button2").pack()
PresetBTN3 = tk.Button(PresetFrame,text="Button3").pack()

mouseBTN1 = tk.Button(MouseFrame,text="Button 1").pack()
mouseBTN2 = tk.Button(MouseFrame,text="Button 2").pack()
mouseBTN3 = tk.Button(MouseFrame,text="Button 3").pack()

soundBTN = tk.Button(SoundFrame,text="Button 1").pack()

powerPlanBTN1 = tk.Button(PowerPlanFrame,text="Button 1").pack()

inputDelayBTN = tk.Button(InputDelayFrame,text="Button 1").pack()





























window.minsize(1000,390)
window.maxsize(1000,390)

window.mainloop()

