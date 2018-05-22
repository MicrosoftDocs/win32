---
Description: 'An interlocked singly linked list (SList) eases the task of insertion and deletion from a linked list.'
ms.assetid: '35463ace-33ab-4eb9-9901-2504a92456e2'
title: Interlocked Singly Linked Lists
---

# Interlocked Singly Linked Lists

An *interlocked singly linked list* (SList) eases the task of insertion and deletion from a linked list. SLists are implemented using a nonblocking algorithm to provide atomic synchronization, increase system performance, and avoid problems such as priority inversion and lock convoys.

SLists are straightforward to implement and use in 32-bit code. However, it is challenging to implement them in 64-bit code because the amount of data exchangeable by the native interlocked exchange primitives is not double the address size, as it is in 32-bit code. Therefore, SLists enable porting high-end scalable algorithms to Windows.

**Windows 8:** Starting in Windows 8 the appropriate native interlocked exchange primitives are available for 64-bit code, for example [**InterlockedCompare64Exchange128**](interlockedcompare64exchange128.md).

Applications can use SLists by calling the [**InitializeSListHead**](initializeslisthead.md) function to initialize the head of the list. To insert items into the list, use the [**InterlockedPushEntrySList**](interlockedpushentryslist.md) function. To delete items from the list, use the [**InterlockedPopEntrySList**](interlockedpopentryslist.md) function.

All list items must be aligned on a **MEMORY\_ALLOCATION\_ALIGNMENT** boundary. Unaligned items can cause unpredictable results. See **\_aligned\_malloc**.

For an example, see [Using Singly Linked Lists](using-singly-linked-lists.md).

The following table lists the SList functions.



| Function                                                         | Description                                                                                                                                               |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**InitializeSListHead**](initializeslisthead.md)               | Initializes the head of a singly linked list.                                                                                                             |
| [**InterlockedFlushSList**](interlockedflushslist.md)           | Flushes the entire list of items in a singly linked list.                                                                                                 |
| [**InterlockedPopEntrySList**](interlockedpopentryslist.md)     | Removes an item from the front of a singly linked list.                                                                                                   |
| [**InterlockedPushEntrySList**](interlockedpushentryslist.md)   | Inserts an item at the front of a singly linked list.                                                                                                     |
| [**InterlockedPushListSList**](interlockedpushlistslist.md)     | Inserts a singly-linked list at the front of another singly linked list.                                                                                  |
| [**InterlockedPushListSListEx**](interlockedpushlistslistex.md) | Inserts a singly-linked list at the front of another singly linked list. This version of the method does not use the **\_\_fastcall** calling convention. |
| [**RtlFirstEntrySList**](rtlfirstentryslist.md)                 | Retrieves the first entry in a singly linked list.                                                                                                        |
| [**QueryDepthSList**](querydepthslist.md)                       | Retrieves the number of entries in the specified singly linked list.                                                                                      |



 

 

 



