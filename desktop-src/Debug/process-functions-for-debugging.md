---
Description: The CreateProcess function enables a debugger to start a process and debug it.
ms.assetid: 7056e181-9bc5-4530-a7b8-d5ff1e345eef
title: Process Functions for Debugging
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Process Functions for Debugging

The [**CreateProcess**](https://msdn.microsoft.com/windows/desktop/3ef0a5b2-4d71-4c17-8188-76a4025287fc) function enables a debugger to start a process and debug it. The *fdwCreate* parameter of **CreateProcess** is used to specify the type of debugging operation. If the DEBUG\_PROCESS flag is specified for the parameter, a debugger debugs the new process and all of the process's descendants, provided that the descendants are created without the DEBUG\_PROCESS flag.

If the DEBUG\_PROCESS and DEBUG\_ONLY\_THIS\_PROCESS flags are specified for *fdwCreate*, a debugger debugs the new process but none of its descendants.

One debugger can debug another by creating a process with the DEBUG\_PROCESS flag. The new process (the debugger being debugged) must then create a process with the DEBUG\_PROCESS flag.

The [**OpenProcess**](https://msdn.microsoft.com/windows/desktop/8f695c38-19c4-49e4-97de-8b64ea536cb1) function enables a debugger to obtain the identifier of an existing process. (The [**DebugActiveProcess**](/windows/desktop/api/WinBase/) function uses this identifier to attach the debugger to the process.) Typically, debuggers open a process with the PROCESS\_VM\_READ and PROCESS\_VM\_WRITE flags. Using these flags enables the debugger to read from and write to the virtual memory of the process by using the [**ReadProcessMemory**](https://www.bing.com/search?q=**ReadProcessMemory**) and [**WriteProcessMemory**](https://www.bing.com/search?q=**WriteProcessMemory**) functions. For more information, see [**Processes and Threads**](https://msdn.microsoft.com/windows/desktop/6bff848c-0c55-41e7-aff1-84c6b21a1b8d).

 

 



