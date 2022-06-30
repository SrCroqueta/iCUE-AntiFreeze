import os, time, ctypes, shutil

def noWindow(): # No black screen when running.
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def regKeyForHighPriority(): # Creates two directories with their registry keys to setting up high priority processes for Corsair's services.
#    https://answers.microsoft.com/en-us/windows/forum/all/how-to-permanently-set-priority-processes-using/df82bd40-ce52-4b84-af34-4d93da17d079
    try:
        os.system('cmd /c "reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\iCUE.exe"')
        os.system('cmd /c "reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\iCUE.exe\PerfOptions" /v "CpuPriorityClass" /t REG_DWORD /d 00000003"')
        os.system('cmd /c "reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\Corsair.Service.exe"')
        os.system('cmd /c "reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\Corsair.Service.exe\PerfOptions" /v "CpuPriorityClass" /t REG_DWORD /d 00000003"')
    except:
        pass

def copyToStartup(): # Copies the '.exe' file to the Windows' Startup programs directory.
    src_file = 'iCUE AntiFreeze.exe'
    to_directory = os.getenv('APPDATA')+r'\Microsoft\Windows\Start Menu\Programs\Startup\iCUE AntiFreeze.exe'

    try:
        shutil.copyfile(src_file, to_directory)
    except:
        pass

def msgBox(): # Advices that the file it can be deleted from where it has been launched.
    ctypes.windll.user32.MessageBoxW(0, "You can now delete the file where it has been launched from. It has been copied to the Windows' startup programs directory.\n\nYou can check it if you go to:\n\n%AppData%\Microsoft\Windows\Start Menu\Programs\Startup\n\nThere should be the same file. Don't delete this one.", 'Info', 0)

def reloadService(): # Restarts 'CorsairService' every hour.
    while True:
        os.system('powershell.exe Restart-Service CorsairService -Force')
        time.sleep(3600)

def main():
    noWindow()
    if not isAdmin():
        ctypes.windll.user32.MessageBoxW(0, "You must run 'iCUE AntiFreeze.exe' as Administrator.", 'Error: Administrator privileges.', 0)
    else:
        regKeyForHighPriority()
        copyToStartup()
        msgBox()
        reloadService()

if __name__ == '__main__':
    main()
