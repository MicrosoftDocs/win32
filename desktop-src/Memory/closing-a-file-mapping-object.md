---
description: When a process has finished with the file mapping object, it should destroy all file views in its address space by using the UnmapViewOfFile function for each file view.
ms.assetid: d62d068c-9b1d-4dbf-8b21-31a636a41456
title: Closing a File Mapping Object
ms.topic: article
ms.date: 05/31/2018
---

# Closing a File Mapping Object

When a process has finished with the file mapping object, it should destroy all file views in its address space by using the [**UnmapViewOfFile**](/windows/win32/api/memoryapi/nf-memoryapi-unmapviewoffile) function for each file view.

Unmapping a mapped view of a file invalidates the range occupied by the view in the address space of the process and makes the range available for other allocations. It removes the working set entry for each unmapped virtual page that was part of the working set of the process and reduces the working set size of the process. It also decrements the share count of the corresponding physical page.

Modified pages in the unmapped view are not written to disk until their share count reaches zero, or in other words, until they are unmapped or trimmed from the working sets of all processes that share the pages. Even then, the modified pages are written "lazily" to disk; that is, modifications may be cached in memory and written to disk at a later time. To minimize the risk of data loss in the event of a power failure or a system crash, applications should explicitly flush modified pages using the [**FlushViewOfFile**](/windows/win32/api/memoryapi/nf-memoryapi-flushviewoffile) function.

When each process finishes using the file mapping object and has unmapped all views, it must close the file mapping object's handle and the file on disk by calling [**CloseHandle**](/windows/win32/api/handleapi/nf-handleapi-closehandle). These calls to **CloseHandle** succeed even when there are file views that are still open. However, leaving file views mapped causes memory leaks.

 

 
