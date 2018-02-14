#!/usr/bin/env python
# -*- coding utf8 -*-

import os
import getpass
import subprocess
import tkinter as tk
from tkinter import *
from PIL import ImageTk

root = tk.Tk()

userprofile = str(os.environ['USERPROFILE'])

def log_use(program_used):# not currently in use
    """Check which programs are being used the most - or even at all"""
    try:
        os.popen("python " + userprofile + "/Documents/python/gui_interface/log_uses.py " + program_used)
    except:
        pass


## These are the defs for menubar tabs ##
def make_shortcut(Var):
    os.system("start " + userprofile +"/Documents/python/InstallnRemove/make_desktop_shortcut.vbs")
    print(Var)

def install_depends(Var):
    os.system("start " + userprofile +"/Documents/python/InstallnRemove/install_depend.bat" )
    print(Var)

def playsnake(Var):
    os.popen("pythonw " + userprofile +"/Documents/python/pygame/snake.py" )
    print(Var)

def microsoftRewards(Var):
    os.system("python " + userprofile +"/Documents/python/extra/microsoft_rewards.py" )
    print(Var)

class Application(tk.Frame):
    """Main Loop for the button creation and commands"""
    def __init__(self, master=None):
        root.title('Welcome back ' + str(getpass.getuser()).capitalize() + '!')
        root.iconbitmap(r''+ userprofile +'/Documents/python/icons/serpent_icon.ico')

        # File Menu Bar Tab
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='Desktop Shortcut', command=lambda: make_shortcut("Making Shortcut"))
        filemenu.add_command(label='Install Dependencies', command=lambda: install_depends("Installing Modules"))
        #filemenu.add_command(label='Update', command=lambda: update_user_code("Updating Code"))
        filemenu.add_command(label="Exit", command=root.destroy)
        menubar.add_cascade(label="File", menu=filemenu)

        # Powershell Menu Bar Tab
        #filemenu2 = Menu(menubar, tearoff=0)
        #menubar.add_cascade(label="Powershell", menu=filemenu2)

        # Extras Menu Bar Tab
        filemenu3 = Menu(menubar, tearoff=0)
        filemenu3.add_command(label='Snake', command=lambda: playsnake("Running Game!"))
        filemenu3.add_command(label='Microsoft Rewards', command=lambda: microsoftRewards("Launching Rewards!"))
        menubar.add_cascade(label="Extras", menu=filemenu3)
        
        root.config(menu=menubar)
        super().__init__(master)
        self.pack()
        self.weather_grab_button()
        self.pinger_button()
        self.tstation_button()
        self.port_scanner_button()


## These create the buttons ##
    def weather_grab_button(self):
        """Weather Grabber launch button"""
        image = ImageTk.PhotoImage(file=userprofile + "/Documents/python/icons/weather.png")
        b = tk.Button(self, text="Current Weather", image=image, compound="top")
        b.config(image=image)
        b.image = image
        b["command"] = self.weather_grab_launch
        b.pack(padx=3, pady=10, side='left')

    def pinger_button(self):
        """Multiple pinger"""
        b = tk.Button(root)
        image = ImageTk.PhotoImage(file=userprofile + "/Documents/python/icons/pinger.png")
        b = tk.Button(self, text="Multiple Pinger", image=image, compound="top")
        b.config(image=image)
        b.image = image
        b["command"] = self.multiplepinger_launch
        b.pack(padx=3, pady=10, side='left')

    def tstation_button(self):
        """Translation Station"""
        b = tk.Button(root)
        image = ImageTk.PhotoImage(file=userprofile + "/Documents/python/icons/tstation_icon.png ")
        b = tk.Button(self, text="Translation Station", image=image, compound="top")
        b.config(image=image)
        b.image = image
        b["command"] = self.tstation_launch
        b.pack(padx=3, pady=10, side='left')

    def port_scanner_button(self):
        """Port Scanner"""
        b = tk.Button(root)
        image = ImageTk.PhotoImage(file=userprofile + "/Documents/python/icons/ninja_scan.png")
        b = tk.Button(self, text="Port Scanner", image=image, compound="top")
        b.config(image=image)
        b.image = image
        b["command"] = self.port_scanner_launch
        b.pack(padx=3, pady=10, side='left')

## These launch the button programs ##
    def weather_grab_launch(self):
        """Weather Grabber Launcher"""
        os.popen("python " + userprofile + "/Documents/python/weather/guiWeather.py")

    def multiplepinger_launch(self):
        """Multiple Pinger Launcher"""
        os.system("start " + userprofile + "/Documents/python/gui_interface/bat_launchers/pinglaunch.bat")
    
    def tstation_launch(self):
        """Translation Station Launcher"""
        os.system("start " + userprofile + "/Documents/python/gui_interface/bat_launchers/launch_tstation.bat")

    def port_scanner_launch(self):
        """Port Scanner Launcher"""
        os.popen("start " + userprofile + "/Documents/python/gui_interface/bat_launchers/portScanner.bat")
##########################################################

app = Application(master=root)
app.mainloop()