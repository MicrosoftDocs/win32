---
title: Tool Help Functions
description: Lists the tool help library functions.
ms.assetid: '83732bd6-f4cf-409d-ad17-86503d408dc3'
ms.topic: article
ms.date: 05/31/2018
---

# Tool Help Functions

The following functions are part of the tool help library.



| Function                                                           | Description                                                                                                      |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [**CreateToolhelp32Snapshot**](/windows/desktop/api/TlHelp32/nf-tlhelp32-createtoolhelp32snapshot)       | Takes a snapshot of the specified processes, as well as the heaps, modules, and threads used by these processes. |
| [**Heap32First**](/windows/desktop/api/TlHelp32/nf-tlhelp32-heap32first)                                 | Retrieves information about the first block of a heap that has been allocated by a process.                      |
| [**Heap32ListFirst**](/windows/desktop/api/TlHelp32/nf-tlhelp32-heap32listfirst)                         | Retrieves information about the first heap that has been allocated by a specified process.                       |
| [**Heap32ListNext**](/windows/desktop/api/TlHelp32/nf-tlhelp32-heap32listnext)                           | Retrieves information about the next heap that has been allocated by a process.                                  |
| [**Heap32Next**](/windows/desktop/api/TlHelp32/nf-tlhelp32-heap32next)                                   | Retrieves information about the next block of a heap that has been allocated by a process.                       |
| [**Module32First**](/windows/desktop/api/TlHelp32/nf-tlhelp32-module32first)                             | Retrieves information about the first module associated with a process.                                          |
| [**Module32Next**](/windows/desktop/api/TlHelp32/nf-tlhelp32-module32next)                               | Retrieves information about the next module associated with a process or thread.                                 |
| [**Process32First**](/windows/desktop/api/TlHelp32/nf-tlhelp32-process32first)                           | Retrieves information about the first process encountered in a system snapshot.                                  |
| [**Process32Next**](/windows/desktop/api/TlHelp32/nf-tlhelp32-process32next)                             | Retrieves information about the next process recorded in a system snapshot.                                      |
| [**Thread32First**](/windows/desktop/api/TlHelp32/nf-tlhelp32-thread32first)                             | Retrieves information about the first thread of any process encountered in a system snapshot.                    |
| [**Thread32Next**](/windows/desktop/api/TlHelp32/nf-tlhelp32-thread32next)                               | Retrieves information about the next thread of any process encountered in the system memory snapshot.            |
| [**Toolhelp32ReadProcessMemory**](/windows/desktop/api/TlHelp32/nf-tlhelp32-toolhelp32readprocessmemory) | Copies memory allocated to another process into an application-supplied buffer.                                  |



 

 

 




