---
title: Thread Walking
description: A snapshot that includes the thread list contains information about each thread of each currently executing process.
ms.assetid: '2440b781-652d-4d73-b173-87504e7b49b5'
keywords: ["enumerating", "enumerating,threads", "threads", "threads,enumerating threads"]
---

# Thread Walking

A snapshot that includes the thread list contains information about each thread of each currently executing process. You can retrieve information for the first thread in the list by using the [**Thread32First**](thread32first.md) function. After retrieving the first thread in the list, you can retrieve information for subsequent threads by using the [**Thread32Next**](thread32next.md) function. **Thread32First** and **Thread32Next** fill a [**THREADENTRY32**](threadentry32-str.md) structure with information about individual threads in the snapshot.

You can enumerate the threads of a specific process by taking a snapshot that includes the threads and then by traversing the thread list, keeping information about the threads that have the same process identifier as the specified process.

You can retrieve an extended error status code for [**Thread32First**](thread32first.md) and [**Thread32Next**](thread32next.md) by using the [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) function.

> [!Note]  
> The contents of the **th32ThreadID** member of [**THREADENTRY32**](threadentry32-str.md) is a thread identifier and can be used by any functions that require a thread identifier.

 

## Related topics

<dl> <dt>

[Traversing the Thread List](traversing-the-thread-list.md)
</dt> </dl>

 

 




