---
title: Process Walking
description: A snapshot that includes the process list contains information about each currently executing process.
ms.assetid: '4fb55763-2206-48ad-8b1f-ed2c33b6f56b'
keywords: ["enumerating", "enumerating,processes", "processes", "processes,enumerating processes"]
---

# Process Walking

A snapshot that includes the process list contains information about each currently executing process. You can retrieve information for the first process in the list by using the [**Process32First**](process32first.md) function. After retrieving the first process in the list, you can traverse the process list for subsequent entries by using the [**Process32Next**](process32next.md) function. **Process32First** and **Process32Next** fill a [**PROCESSENTRY32**](processentry32-str.md) structure with information about a process in the snapshot. For an example, see [Taking a Snapshot and Viewing Processes](taking-a-snapshot-and-viewing-processes.md).

You can retrieve an extended error status code for [**Process32First**](process32first.md) and [**Process32Next**](process32next.md) by using the [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) function.

You can read the memory in a specific process into a buffer by using the [**Toolhelp32ReadProcessMemory**](toolhelp32readprocessmemory.md) function (or the [**VirtualQueryEx**](https://msdn.microsoft.com/library/windows/desktop/aa366907) function).

> [!Note]  
> The contents of the **th32ProcessID** and **th32ParentProcessID** members of [**PROCESSENTRY32**](processentry32-str.md) are process identifiers and can be used by any functions that require a process identifier.

 

 

 




