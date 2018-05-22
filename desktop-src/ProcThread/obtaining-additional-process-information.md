---
Description: 'There are a variety of functions for obtaining information about processes.'
ms.assetid: 'f9ec6aa5-15ad-47e6-b5f8-8ac4daaf178f'
title: Obtaining Additional Process Information
---

# Obtaining Additional Process Information

There are a variety of functions for obtaining information about processes. Some of these functions can be used only for the calling process, because they do not take a process handle as a parameter. You can use functions that take a process handle to obtain information about other processes.

-   To obtain the command-line string for the current process, use the [**GetCommandLine**](getcommandline.md) function.
-   To retrieve the [**STARTUPINFO**](startupinfo-str.md) structure specified when the current process was created, use the [**GetStartupInfo**](getstartupinfo.md) function.
-   To obtain the version information from the executable header, use the [**GetProcessVersion**](getprocessversion.md) function.
-   To obtain the full path and file name for the executable file containing the process code, use the [**GetModuleFileName**](base.getmodulefilename) function.
-   To obtain the count of handles to graphical user interface (GUI) objects in use, use the [**GetGuiResources**](getguiresources.md) function.
-   To determine whether a process is being debugged, use the [**IsDebuggerPresent**](base.isdebuggerpresent) function.
-   To retrieve accounting information for all I/O operations performed by the process, use the [**GetProcessIoCounters**](getprocessiocounters.md) function.

 

 



