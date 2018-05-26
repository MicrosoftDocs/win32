---
Description: An interlocked singly linked list (SList) eases the task of insertion and deletion from a linked list.
ms.assetid: 35463ace-33ab-4eb9-9901-2504a92456e2
title: Interlocked Singly Linked Lists
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Interlocked Singly Linked Lists

An *interlocked singly linked list* (SList) eases the task of insertion and deletion from a linked list. SLists are implemented using a nonblocking algorithm to provide atomic synchronization, increase system performance, and avoid problems such as priority inversion and lock convoys.

SLists are straightforward to implement and use in 32-bit code. However, it is challenging to implement them in 64-bit code because the amount of data exchangeable by the native interlocked exchange primitives is not double the address size, as it is in 32-bit code. Therefore, SLists enable porting high-end scalable algorithms to Windows.

**Windows 8:** Starting in Windows 8 the appropriate native interlocked exchange primitives are available for 64-bit code, for example [**InterlockedCompare64Exchange128**](/windows/win32/WinBase/?branch=master).

Applications can use SLists by calling the [**InitializeSListHead**](/windows/win32/WinBase/nf-interlockedapi-initializeslisthead?branch=master) function to initialize the head of the list. To insert items into the list, use the [**InterlockedPushEntrySList**](/windows/win32/WinBase/nf-interlockedapi-interlockedpushentryslist?branch=master) function. To delete items from the list, use the [**InterlockedPopEntrySList**](/windows/win32/WinBase/nf-interlockedapi-interlockedpopentryslist?branch=master) function.

All list items must be aligned on a **MEMORY\_ALLOCATION\_ALIGNMENT** boundary. Unaligned items can cause unpredictable results. See **\_aligned\_malloc**.

For an example, see [Using Singly Linked Lists](using-singly-linked-lists.md).

The following table lists the SList functions.



| Function                                                         | Description                                                                                                                                               |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**InitializeSListHead**](/windows/win32/WinBase/nf-interlockedapi-initializeslisthead?branch=master)               | Initializes the head of a singly linked list.                                                                                                             |
| [**InterlockedFlushSList**](/windows/win32/WinBase/nf-interlockedapi-interlockedflushslist?branch=master)           | Flushes the entire list of items in a singly linked list.                                                                                                 |
| [**InterlockedPopEntrySList**](/windows/win32/WinBase/nf-interlockedapi-interlockedpopentryslist?branch=master)     | Removes an item from the front of a singly linked list.                                                                                                   |
| [**InterlockedPushEntrySList**](/windows/win32/WinBase/nf-interlockedapi-interlockedpushentryslist?branch=master)   | Inserts an item at the front of a singly linked list.                                                                                                     |
| [**InterlockedPushListSList**](/windows/win32/WinBase/?branch=master)     | Inserts a singly-linked list at the front of another singly linked list.                                                                                  |
| [**InterlockedPushListSListEx**](/windows/win32/interlockedapi/nf-interlockedapi-interlockedpushlistslistex?branch=master) | Inserts a singly-linked list at the front of another singly linked list. This version of the method does not use the **\_\_fastcall** calling convention. |
| [**RtlFirstEntrySList**](/windows/win32/WinNT/nf-winnt-rtlfirstentryslist?branch=master)                 | Retrieves the first entry in a singly linked list.                                                                                                        |
| [**QueryDepthSList**](/windows/win32/WinBase/nf-interlockedapi-querydepthslist?branch=master)                       | Retrieves the number of entries in the specified singly linked list.                                                                                      |



 

 

 



