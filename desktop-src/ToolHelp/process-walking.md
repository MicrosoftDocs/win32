---
title: Process Walking
description: A snapshot that includes the process list contains information about each currently executing process.
ms.assetid: 4fb55763-2206-48ad-8b1f-ed2c33b6f56b
keywords:
- enumerating
- enumerating,processes
- processes
- processes,enumerating processes
ms.topic: article
ms.date: 05/31/2018
---

# Process Walking

A snapshot that includes the process list contains information about each currently executing process. You can retrieve information for the first process in the list by using the [**Process32First**](/windows/desktop/api/TlHelp32/nf-tlhelp32-process32first) function. After retrieving the first process in the list, you can traverse the process list for subsequent entries by using the [**Process32Next**](/windows/desktop/api/TlHelp32/nf-tlhelp32-process32next) function. **Process32First** and **Process32Next** fill a [**PROCESSENTRY32**](/windows/desktop/api/TlHelp32/ns-tlhelp32-tagprocessentry32) structure with information about a process in the snapshot. For an example, see [Taking a Snapshot and Viewing Processes](taking-a-snapshot-and-viewing-processes.md).

You can retrieve an extended error status code for [**Process32First**](/windows/desktop/api/TlHelp32/nf-tlhelp32-process32first) and [**Process32Next**](/windows/desktop/api/TlHelp32/nf-tlhelp32-process32next) by using the [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) function.

You can read the memory in a specific process into a buffer by using the [**Toolhelp32ReadProcessMemory**](/windows/desktop/api/TlHelp32/nf-tlhelp32-toolhelp32readprocessmemory) function (or the [**VirtualQueryEx**](https://msdn.microsoft.com/library/windows/desktop/aa366907) function).

> [!Note]  
> The contents of the **th32ProcessID** and **th32ParentProcessID** members of [**PROCESSENTRY32**](/windows/desktop/api/TlHelp32/ns-tlhelp32-tagprocessentry32) are process identifiers and can be used by any functions that require a process identifier.

 

 

 




