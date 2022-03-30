---
description: This topic explains how to debug Shell and namespace extension DLLs.
title: Debugging with the Shell
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 2fcaf633-9a6d-4fda-a690-28445b10a6d6
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Debugging with the Shell

This topic explains how to debug Shell and namespace extension DLLs.

- [Running the Shell Under a Debugger](#running-the-shell-under-a-debugger)
- [Running and Testing Shell Extensions](#running-and-testing-shell-extensions)
- [Unloading the DLL](#unloading-the-dll)

## Running the Shell Under a Debugger

To debug your extension, you need to run the Shell from the debugger. Follow these steps:

1.  Load the extension's project into the debugger, but do not run it.
2.  Shut down the Shell.

    - For Windows Vista and later:
        1.  Display the **Start** menu.
        2.  Press CTRL+SHIFT and right-click on the background of the right half of the **Start** menu.
        3.  From the menu that appears, choose **Exit Explorer**.
    - For Windows XP:
        1.  From the **Start** menu, choose **Shut down**.
        2.  Press CTRL+ALT+SHIFT, and click **No** in the **Shut Down Windows** dialog box.

    The Shell is now shut down, but all other applications are still running, including the debugger.

3.  Set the debugger to run the extension DLL with Explorer.exe from the **Windows** directory.
4.  Run the project from the debugger. The Shell will launch as usual, but the debugger will be attached to the Shell's process.

## Running and Testing Shell Extensions

You can run and test your extensions in a separate Windows Explorer process to avoid stopping and restarting the desktop and taskbar. Your desktop and taskbar can still be used while you run and test the extensions.

To enable this feature, add the following REG\_DWORD entry to the registry.

```
HKEY_CURRENT_USER
   Software
      Microsoft
         Windows
            CurrentVersion
               Explorer
                  DesktopProcess = 1
```

For this entry to take effect, you must log off and log on again. This setting causes the desktop and taskbar windows to be created in one Explorer.exe process and all other Explorer and folder windows to be opened in a different Explorer.exe process.

In addition to making the running and testing of your extensions more convenient, this setting also makes the desktop more robust as it relates to Shell extensions. Many such extensions (shortcut menu extensions, for example) will be loaded into the nondesktop Explorer.exe process. If this process terminates, the desktop and taskbar will be unaffected, and the next Explorer or folder window will re-create the terminated process.

## Unloading the DLL

The Shell automatically unloads any DLL when its usage count is zero, but only after the DLL has not been used for a period of time. This inactive period might be unacceptably long at times, especially when a Shell extension DLL is being debugged. You can shorten the inactive period by adding the following information to the registry.

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Windows
            CurrentVersion
               Explorer
                  AlwaysUnloadDll
```

 

 



