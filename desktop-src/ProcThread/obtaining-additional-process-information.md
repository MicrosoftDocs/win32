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

-   To obtain the command-line string for the current process, use the [**GetCommandLine**](/windows/desktop/api/WinBase/) function.
-   To retrieve the [**STARTUPINFO**](/windows/desktop/api/WinBase/ns-processthreadsapi-_startupinfoa) structure specified when the current process was created, use the [**GetStartupInfo**](/windows/desktop/api/WinBase/nf-winbase-getstartupinfoa) function.
-   To obtain the version information from the executable header, use the [**GetProcessVersion**](/windows/desktop/api/WinBase/nf-processthreadsapi-getprocessversion) function.
-   To obtain the full path and file name for the executable file containing the process code, use the [**GetModuleFileName**](https://msdn.microsoft.com/windows/desktop/f124c99f-8be1-4a9c-a84c-b1b323921f1a) function.
-   To obtain the count of handles to graphical user interface (GUI) objects in use, use the [**GetGuiResources**](/windows/desktop/api/Winuser/nf-winuser-getguiresources) function.
-   To determine whether a process is being debugged, use the [**IsDebuggerPresent**](https://msdn.microsoft.com/windows/desktop/7bc4bcb7-3f85-4349-a1da-c4ebee2d3e3f) function.
-   To retrieve accounting information for all I/O operations performed by the process, use the [**GetProcessIoCounters**](/windows/desktop/api/WinBase/nf-winbase-getprocessiocounters) function.

 

 



