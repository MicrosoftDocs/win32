---
description: The following functions are used with system shutdown.
ms.assetid: 6a08a769-1acf-49eb-ba95-beaf56a374bf
title: System Shutdown Functions
ms.topic: article
ms.date: 05/31/2018
---

# System Shutdown Functions

The following functions are used with system shutdown.



| Function                                                         | Description                                                                                                                         |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [**AbortSystemShutdown**](/windows/desktop/api/Winreg/nf-winreg-abortsystemshutdowna)               | Stops a system shutdown that has been initiated.                                                                                    |
| [**ExitWindows**](/windows/desktop/api/Winuser/nf-winuser-exitwindows)                               | Logs off the interactive user.                                                                                                      |
| [**ExitWindowsEx**](/windows/desktop/api/Winuser/nf-winuser-exitwindowsex)                           | Logs off the interactive user, shuts down the system, or shuts down and restarts the system.                                        |
| [**InitiateShutdown**](/windows/desktop/api/Winreg/nf-winreg-initiateshutdowna)                     | Initiates a shutdown and restart of the specified computer, and restarts any applications that have been registered for restart.    |
| [**InitiateSystemShutdown**](/windows/desktop/api/Winreg/nf-winreg-initiatesystemshutdowna)         | Initiates a shutdown and optional restart of the specified computer.                                                                |
| [**InitiateSystemShutdownEx**](/windows/desktop/api/Winreg/nf-winreg-initiatesystemshutdownexa)     | Initiates a shutdown and optional restart of the specified computer, and optionally records the reason for the shutdown.            |
| [**LockWorkStation**](/windows/desktop/api/Winuser/nf-winuser-lockworkstation)                       | Locks the workstation's display.                                                                                                    |
| [**ShutdownBlockReasonCreate**](/windows/desktop/api/Winuser/nf-winuser-shutdownblockreasoncreate)   | Indicates that the system cannot be shut down and sets a reason string to be displayed to the user if system shutdown is initiated. |
| [**ShutdownBlockReasonDestroy**](/windows/desktop/api/Winuser/nf-winuser-shutdownblockreasondestroy) | Indicates that the system can be shut down and frees the reason string.                                                             |
| [**ShutdownBlockReasonQuery**](/windows/desktop/api/Winuser/nf-winuser-shutdownblockreasonquery)     | Retrieves the reason string set by the [**ShutdownBlockReasonCreate**](/windows/desktop/api/Winuser/nf-winuser-shutdownblockreasoncreate) function.                     |



 

 

 



