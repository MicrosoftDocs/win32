---
Description: There are a variety of functions for obtaining information about processes.
ms.assetid: f9ec6aa5-15ad-47e6-b5f8-8ac4daaf178f
title: Obtaining Additional Process Information
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Obtaining Additional Process Information

There are a variety of functions for obtaining information about processes. Some of these functions can be used only for the calling process, because they do not take a process handle as a parameter. You can use functions that take a process handle to obtain information about other processes.

-   To obtain the command-line string for the current process, use the [**GetCommandLine**](/windows/win32/WinBase/?branch=master) function.
-   To retrieve the [**STARTUPINFO**](/windows/win32/WinBase/ns-processthreadsapi-_startupinfoa?branch=master) structure specified when the current process was created, use the [**GetStartupInfo**](/windows/win32/WinBase/nf-winbase-getstartupinfoa?branch=master) function.
-   To obtain the version information from the executable header, use the [**GetProcessVersion**](/windows/win32/WinBase/nf-processthreadsapi-getprocessversion?branch=master) function.
-   To obtain the full path and file name for the executable file containing the process code, use the [**GetModuleFileName**](base.getmodulefilename) function.
-   To obtain the count of handles to graphical user interface (GUI) objects in use, use the [**GetGuiResources**](/windows/win32/Winuser/nf-winuser-getguiresources?branch=master) function.
-   To determine whether a process is being debugged, use the [**IsDebuggerPresent**](base.isdebuggerpresent) function.
-   To retrieve accounting information for all I/O operations performed by the process, use the [**GetProcessIoCounters**](/windows/win32/WinBase/nf-winbase-getprocessiocounters?branch=master) function.

 

 



