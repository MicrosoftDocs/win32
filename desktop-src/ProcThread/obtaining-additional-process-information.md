---
Description: There are a variety of functions for obtaining information about processes.
ms.assetid: f9ec6aa5-15ad-47e6-b5f8-8ac4daaf178f
title: Obtaining Additional Process Information
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining Additional Process Information

There are a variety of functions for obtaining information about processes. Some of these functions can be used only for the calling process, because they do not take a process handle as a parameter. You can use functions that take a process handle to obtain information about other processes.

-   To obtain the command-line string for the current process, use the [**GetCommandLine**](https://msdn.microsoft.com/en-us/library/ms683156(v=VS.85).aspx) function.
-   To retrieve the [**STARTUPINFO**](/windows/desktop/api) structure specified when the current process was created, use the [**GetStartupInfo**](/windows/desktop/api/WinBase/nf-winbase-getstartupinfoa) function.
-   To obtain the version information from the executable header, use the [**GetProcessVersion**](/windows/desktop/api) function.
-   To obtain the full path and file name for the executable file containing the process code, use the [**GetModuleFileName**](https://msdn.microsoft.com/en-us/library/ms683197(v=VS.85).aspx) function.
-   To obtain the count of handles to graphical user interface (GUI) objects in use, use the [**GetGuiResources**](/windows/desktop/api/Winuser/nf-winuser-getguiresources) function.
-   To determine whether a process is being debugged, use the [**IsDebuggerPresent**](https://msdn.microsoft.com/en-us/library/ms680345(v=VS.85).aspx) function.
-   To retrieve accounting information for all I/O operations performed by the process, use the [**GetProcessIoCounters**](/windows/desktop/api/WinBase/nf-winbase-getprocessiocounters) function.

 

 



