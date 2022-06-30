![iCUE AntiFreeze Logo](https://user-images.githubusercontent.com/32432079/176553169-90b8d5da-aeed-41fb-9aeb-fae405ded87d.png)

This a program made with Python to "fix" a bug with the iCUE monitoring.

## What it does:

- Auto-setup with high priority the service that is responsible for monitoring the temperatures.
- It restart this service every hour and make it run itself at the startup.

## How to use:

- Just download **_'iCUE AntiFreeze.exe'_** and launch it as administrator, that's all.

## AntiVirus detected it as a threat:

**This is really common when the '.exe' files are not signed. You will have to add an exception in your AntiVirus to make it enable to run.**
> _Sorry, but I still learning programming and I prefer to focus on create "things" instead of looking how to sign programs for now._

## I want to get rid of it:

- You have to delete two directories from Windows registry:

   - Press **_'Win + R'_** and type **_'regedit'_** then search for these directories:
   
     - **_HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\iCUE.exe_**
     - **_HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\Corsair.Service.exe_**
   
- Now you have to delete or move **_'iCUE AntiFreeze.exe'_** to another directory. You will find it by doing this:

   - Press **_'Win + R'_** and type **_'%AppData%\Microsoft\Windows\Start Menu\Programs\Startup'_**.
    
