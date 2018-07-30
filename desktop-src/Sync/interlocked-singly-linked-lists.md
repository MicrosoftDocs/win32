---
Description: An interlocked singly linked list (SList) eases the task of insertion and deletion from a linked list.
ms.assetid: 35463ace-33ab-4eb9-9901-2504a92456e2
title: Interlocked Singly Linked Lists
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Interlocked Singly Linked Lists

An *interlocked singly linked list* (SList) eases the task of insertion and deletion from a linked list. SLists are implemented using a nonblocking algorithm to provide atomic synchronization, increase system performance, and avoid problems such as priority inversion and lock convoys.

SLists are straightforward to implement and use in 32-bit code. However, it is challenging to implement them in 64-bit code because the amount of data exchangeable by the native interlocked exchange primitives is not double the address size, as it is in 32-bit code. Therefore, SLists enable porting high-end scalable algorithms to Windows.

**Windows 8:** Starting in Windows 8 the appropriate native interlocked exchange primitives are available for 64-bit code, for example [**InterlockedCompare64Exchange128**](https://msdn.microsoft.com/en-us/library/ms683553(v=VS.85).aspx).

Applications can use SLists by calling the [**InitializeSListHead**](https://msdn.microsoft.com/en-us/library/ms683482(v=VS.85).aspx) function to initialize the head of the list. To insert items into the list, use the [**InterlockedPushEntrySList**](https://msdn.microsoft.com/en-us/library/ms684020(v=VS.85).aspx) function. To delete items from the list, use the [**InterlockedPopEntrySList**](https://msdn.microsoft.com/en-us/library/ms683648(v=VS.85).aspx) function.

All list items must be aligned on a **MEMORY\_ALLOCATION\_ALIGNMENT** boundary. Unaligned items can cause unpredictable results. See **\_aligned\_malloc**.

For an example, see [Using Singly Linked Lists](using-singly-linked-lists.md).

The following table lists the SList functions.



| Function                                                         | Description                                                                                                                                               |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**InitializeSListHead**](https://msdn.microsoft.com/en-us/library/ms683482(v=VS.85).aspx)               | Initializes the head of a singly linked list.                                                                                                             |
| [**InterlockedFlushSList**](https://msdn.microsoft.com/en-us/library/ms683612(v=VS.85).aspx)           | Flushes the entire list of items in a singly linked list.                                                                                                 |
| [**InterlockedPopEntrySList**](https://msdn.microsoft.com/en-us/library/ms683648(v=VS.85).aspx)     | Removes an item from the front of a singly linked list.                                                                                                   |
| [**InterlockedPushEntrySList**](https://msdn.microsoft.com/en-us/library/ms684020(v=VS.85).aspx)   | Inserts an item at the front of a singly linked list.                                                                                                     |
| [**InterlockedPushListSList**](https://msdn.microsoft.com/en-us/library/Hh448545(v=VS.85).aspx)     | Inserts a singly-linked list at the front of another singly linked list.                                                                                  |
| [**InterlockedPushListSListEx**](/windows/desktop/api/interlockedapi/nf-interlockedapi-interlockedpushlistslistex) | Inserts a singly-linked list at the front of another singly linked list. This version of the method does not use the **\_\_fastcall** calling convention. |
| [**RtlFirstEntrySList**](/windows/desktop/api/WinNT/nf-winnt-rtlfirstentryslist)                 | Retrieves the first entry in a singly linked list.                                                                                                        |
| [**QueryDepthSList**](https://msdn.microsoft.com/en-us/library/ms684916(v=VS.85).aspx)                       | Retrieves the number of entries in the specified singly linked list.                                                                                      |



 

 

 



