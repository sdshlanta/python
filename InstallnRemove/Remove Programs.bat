@echo off
cd C:\
echo Removing Files


IF EXIST %userprofile%\python GOTO DIREXISTS
echo The Python Programs Folder has been moved from /Documents or changed and cannot be uninstalled.
IF EXIST %userprofile%\desktop\Python_Programs.lnk GOTO SHORTRM
echo The Desktop Shortcut does not exist and therefore could not be deleted.
goto END

:DIREXISTS
echo Attemping to remove the python programs dir.
RD /S /Q "%userprofile%\python"
echo Python_Programs DIR removed!
IF EXIST %userprofile%\desktop\Python_Programs.lnk GOTO SHORTRM
echo The Python Programs shortcut has been moved or changed and cannot be deleted.
goto END

:SHORTRM
echo Attempting to remove the python programs desktop shortcut.
del %userprofile%\desktop\Python_Programs.lnk
echo Desktop Shortcut Removed
echo 
echo Python Programs Successfully Removed!
:END
pause