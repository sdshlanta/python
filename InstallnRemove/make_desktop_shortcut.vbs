set WshShell = CreateObject("Wscript.shell")
strDesktop = WshShell.SpecialFolders("Desktop")

Set objShell = CreateObject("WScript.Shell")
userProfilePath = objShell.ExpandEnvironmentStrings("%UserProfile%")

set MyShortcut = WshShell.CreateShortcut(strDesktop & "\Python_Programs.lnk")
MyShortcut.IconLocation = userProfilePath & "\Documents\python\icons\serpent_icon.ico"
MyShortcut.TargetPath = "pythonw.exe"
MyShortcut.Arguments = userProfilePath & "\Documents\python\gui_interface\program_launcher.py"
MyShortCut.Save