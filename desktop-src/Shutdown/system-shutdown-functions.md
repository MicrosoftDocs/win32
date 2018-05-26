---
Description: The following functions are used with system shutdown.
ms.assetid: 6a08a769-1acf-49eb-ba95-beaf56a374bf
title: System Shutdown Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System Shutdown Functions

The following functions are used with system shutdown.



| Function                                                         | Description                                                                                                                         |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [**AbortSystemShutdown**](/windows/win32/Winreg/nf-winreg-abortsystemshutdowna?branch=master)               | Stops a system shutdown that has been initiated.                                                                                    |
| [**ExitWindows**](/windows/win32/Winuser/nf-winuser-exitwindows?branch=master)                               | Logs off the interactive user.                                                                                                      |
| [**ExitWindowsEx**](/windows/win32/Winuser/nf-winuser-exitwindowsex?branch=master)                           | Logs off the interactive user, shuts down the system, or shuts down and restarts the system.                                        |
| [**InitiateShutdown**](/windows/win32/Winreg/nf-winreg-initiateshutdowna?branch=master)                     | Initiates a shutdown and restart of the specified computer, and restarts any applications that have been registered for restart.    |
| [**InitiateSystemShutdown**](/windows/win32/Winreg/nf-winreg-initiatesystemshutdowna?branch=master)         | Initiates a shutdown and optional restart of the specified computer.                                                                |
| [**InitiateSystemShutdownEx**](/windows/win32/Winreg/nf-winreg-initiatesystemshutdownexa?branch=master)     | Initiates a shutdown and optional restart of the specified computer, and optionally records the reason for the shutdown.            |
| [**LockWorkStation**](/windows/win32/Winuser/nf-winuser-lockworkstation?branch=master)                       | Locks the workstation's display.                                                                                                    |
| [**ShutdownBlockReasonCreate**](/windows/win32/Winuser/nf-winuser-shutdownblockreasoncreate?branch=master)   | Indicates that the system cannot be shut down and sets a reason string to be displayed to the user if system shutdown is initiated. |
| [**ShutdownBlockReasonDestroy**](/windows/win32/Winuser/nf-winuser-shutdownblockreasondestroy?branch=master) | Indicates that the system can be shut down and frees the reason string.                                                             |
| [**ShutdownBlockReasonQuery**](/windows/win32/Winuser/nf-winuser-shutdownblockreasonquery?branch=master)     | Retrieves the reason string set by the [**ShutdownBlockReasonCreate**](/windows/win32/Winuser/nf-winuser-shutdownblockreasoncreate?branch=master) function.                     |



 

 

 



