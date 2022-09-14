---
title: Thread Walking
description: A snapshot that includes the thread list contains information about each thread of each currently executing process.
ms.assetid: 2440b781-652d-4d73-b173-87504e7b49b5
keywords:
- enumerating
- enumerating,threads
- threads
- threads,enumerating threads
ms.topic: article
ms.date: 05/31/2018
---

# Thread Walking

A snapshot that includes the thread list contains information about each thread of each currently executing process. You can retrieve information for the first thread in the list by using the [**Thread32First**](/windows/desktop/api/TlHelp32/nf-tlhelp32-thread32first) function. After retrieving the first thread in the list, you can retrieve information for subsequent threads by using the [**Thread32Next**](/windows/desktop/api/TlHelp32/nf-tlhelp32-thread32next) function. **Thread32First** and **Thread32Next** fill a [**THREADENTRY32**](/windows/win32/api/tlhelp32/ns-tlhelp32-threadentry32) structure with information about individual threads in the snapshot.

You can enumerate the threads of a specific process by taking a snapshot that includes the threads and then by traversing the thread list, keeping information about the threads that have the same process identifier as the specified process.

You can retrieve an extended error status code for [**Thread32First**](/windows/desktop/api/TlHelp32/nf-tlhelp32-thread32first) and [**Thread32Next**](/windows/desktop/api/TlHelp32/nf-tlhelp32-thread32next) by using the [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) function.

> [!Note]  
> The contents of the **th32ThreadID** member of [**THREADENTRY32**](/windows/win32/api/tlhelp32/ns-tlhelp32-threadentry32) is a thread identifier and can be used by any functions that require a thread identifier.

 

## Related topics

<dl> <dt>

[Traversing the Thread List](traversing-the-thread-list.md)
</dt> </dl>

 

 