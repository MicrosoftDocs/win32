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

The [**CreateProcess**](https://msdn.microsoft.com/en-us/library/ms682425(v=VS.85).aspx) function enables a debugger to start a process and debug it. The *fdwCreate* parameter of **CreateProcess** is used to specify the type of debugging operation. If the DEBUG\_PROCESS flag is specified for the parameter, a debugger debugs the new process and all of the process's descendants, provided that the descendants are created without the DEBUG\_PROCESS flag.

If the DEBUG\_PROCESS and DEBUG\_ONLY\_THIS\_PROCESS flags are specified for *fdwCreate*, a debugger debugs the new process but none of its descendants.

One debugger can debug another by creating a process with the DEBUG\_PROCESS flag. The new process (the debugger being debugged) must then create a process with the DEBUG\_PROCESS flag.

The [**OpenProcess**](https://msdn.microsoft.com/en-us/library/ms684320(v=VS.85).aspx) function enables a debugger to obtain the identifier of an existing process. (The [**DebugActiveProcess**](https://msdn.microsoft.com/en-us/library/ms679295(v=VS.85).aspx) function uses this identifier to attach the debugger to the process.) Typically, debuggers open a process with the PROCESS\_VM\_READ and PROCESS\_VM\_WRITE flags. Using these flags enables the debugger to read from and write to the virtual memory of the process by using the [**ReadProcessMemory**](https://msdn.microsoft.com/en-us/library/ms680553(v=VS.85).aspx) and [**WriteProcessMemory**](https://msdn.microsoft.com/en-us/library/ms681674(v=VS.85).aspx) functions. For more information, see [**Processes and Threads**](https://msdn.microsoft.com/en-us/library/ms684841(v=VS.85).aspx).

 

 



