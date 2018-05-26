---
title: Tool Help Functions
description: Lists the tool help library functions.
ms.assetid: b92f68e9-c702-4133-857b-b3f44d0fb918
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Tool Help Functions

The following functions are part of the tool help library.



| Function                                                           | Description                                                                                                      |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [**CreateToolhelp32Snapshot**](/windows/win32/TlHelp32/nf-tlhelp32-createtoolhelp32snapshot?branch=master)       | Takes a snapshot of the specified processes, as well as the heaps, modules, and threads used by these processes. |
| [**Heap32First**](/windows/win32/TlHelp32/nf-tlhelp32-heap32first?branch=master)                                 | Retrieves information about the first block of a heap that has been allocated by a process.                      |
| [**Heap32ListFirst**](/windows/win32/TlHelp32/nf-tlhelp32-heap32listfirst?branch=master)                         | Retrieves information about the first heap that has been allocated by a specified process.                       |
| [**Heap32ListNext**](/windows/win32/TlHelp32/nf-tlhelp32-heap32listnext?branch=master)                           | Retrieves information about the next heap that has been allocated by a process.                                  |
| [**Heap32Next**](/windows/win32/TlHelp32/nf-tlhelp32-heap32next?branch=master)                                   | Retrieves information about the next block of a heap that has been allocated by a process.                       |
| [**Module32First**](/windows/win32/TlHelp32/nf-tlhelp32-module32first?branch=master)                             | Retrieves information about the first module associated with a process.                                          |
| [**Module32Next**](/windows/win32/TlHelp32/nf-tlhelp32-module32next?branch=master)                               | Retrieves information about the next module associated with a process or thread.                                 |
| [**Process32First**](/windows/win32/TlHelp32/nf-tlhelp32-process32first?branch=master)                           | Retrieves information about the first process encountered in a system snapshot.                                  |
| [**Process32Next**](/windows/win32/TlHelp32/nf-tlhelp32-process32next?branch=master)                             | Retrieves information about the next process recorded in a system snapshot.                                      |
| [**Thread32First**](/windows/win32/TlHelp32/nf-tlhelp32-thread32first?branch=master)                             | Retrieves information about the first thread of any process encountered in a system snapshot.                    |
| [**Thread32Next**](/windows/win32/TlHelp32/nf-tlhelp32-thread32next?branch=master)                               | Retrieves information about the next thread of any process encountered in the system memory snapshot.            |
| [**Toolhelp32ReadProcessMemory**](/windows/win32/TlHelp32/nf-tlhelp32-toolhelp32readprocessmemory?branch=master) | Copies memory allocated to another process into an application-supplied buffer.                                  |



 

 

 




