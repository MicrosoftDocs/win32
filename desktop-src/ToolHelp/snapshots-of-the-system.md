---
title: Snapshots of the System
description: Snapshots are at the core of the tool help functions. A snapshot is a read-only copy of the current state of one or more of the following lists that reside in system memory processes, threads, modules, and heaps.
ms.assetid: a8122960-f078-4efb-8e01-bf6fb69ee0dd
ms.topic: article
ms.date: 05/31/2018
---

# Snapshots of the System

Snapshots are at the core of the tool help functions. A snapshot is a read-only copy of the current state of one or more of the following lists that reside in system memory: processes, threads, modules, and heaps.

Processes that use tool help functions access these lists from snapshots instead of directly from the operating system. The lists in system memory change when processes are started and ended, threads are created and destroyed, executable modules are loaded and unloaded from system memory, and heaps are created and destroyed. The use of information from a snapshot prevents inconsistencies. Otherwise, changes to a list could possibly cause a thread to incorrectly traverse the list or cause an access violation (a GP fault). For example, if an application traverses the thread list while other threads are created or terminated, information that the application is using to traverse the thread list might become outdated and could cause an error for the application traversing the list.

To take a snapshot of the system memory, use the [**CreateToolhelp32Snapshot**](/windows/desktop/api/TlHelp32/nf-tlhelp32-createtoolhelp32snapshot) function. You can control the content of a snapshot by specifying one or more of the following values when calling this function:

-   **TH32CS\_SNAPHEAPLIST**
-   **TH32CS\_SNAPMODULE**
-   **TH32CS\_SNAPPROCESS**
-   **TH32CS\_SNAPTHREAD**

The **TH32CS\_SNAPHEAPLIST** and **TH32CS\_SNAPMODULE** values are process specific. When these values are specified, the heap and module lists of the specified process are included in the snapshot. If you specify zero as the process identifier, the current process is used. The **TH32CS\_SNAPTHREAD** value always creates a system-wide snapshot even if a process identifier is passed to [**CreateToolhelp32Snapshot**](/windows/desktop/api/TlHelp32/nf-tlhelp32-createtoolhelp32snapshot).

To enumerate the heap or module state for all processes, specify the **TH32CS\_SNAPALL** value and the process identifier of the current process. Then, for each additional process in the snapshot, call [**CreateToolhelp32Snapshot**](/windows/desktop/api/TlHelp32/nf-tlhelp32-createtoolhelp32snapshot) again, specifying its process identifier and the **TH32CS\_SNAPHEAPLIST** or **TH32CS\_SNAPMODULE** value.

You can retrieve an extended error status code for [**CreateToolhelp32Snapshot**](/windows/desktop/api/TlHelp32/nf-tlhelp32-createtoolhelp32snapshot) by using the [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) function.

When your process finishes using a snapshot, destroy it using the [**CloseHandle**](/windows/desktop/api/handleapi/nf-handleapi-closehandle) function. If you do not destroy a snapshot, the process will leak memory until the it exits, at which time the system reclaims the memory.

> [!Note]  
> The snapshot handle acts like a file handle and is subject to the same rules regarding the processes and threads in which it can be used. To specify that the handle is inheritable, create the snapshot using the **TH32CS\_INHERIT** value.

 

## Related topics

<dl> <dt>

[Taking a Snapshot and Viewing Processes](taking-a-snapshot-and-viewing-processes.md)
</dt> </dl>

 

 