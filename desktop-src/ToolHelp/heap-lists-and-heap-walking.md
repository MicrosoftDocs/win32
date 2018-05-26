---
title: Heap Lists and Heap Walking
description: A snapshot that includes the heap list for a specified process contains identification information for each heap associated with the specified process and detailed information about each heap.
ms.assetid: 631096fd-cb2c-4b19-aa71-d47060e2715c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Heap Lists and Heap Walking

A snapshot that includes the heap list for a specified process contains identification information for each heap associated with the specified process and detailed information about each heap. You can retrieve an identifier for the first heap of the heap list by using the [**Heap32ListFirst**](/windows/win32/TlHelp32/nf-tlhelp32-heap32listfirst?branch=master) function. After retrieving the first heap in the list, you can traverse the heap list for subsequent heaps associated with the process by using the [**Heap32ListNext**](/windows/win32/TlHelp32/nf-tlhelp32-heap32listnext?branch=master) function. **Heap32ListFirst** and **Heap32ListNext** fill a [**HEAPLIST32**](/windows/win32/TlHelp32/ns-tlhelp32-tagheaplist32?branch=master) structure with the process identifier, the heap identifier, and flags describing the heap.

You can retrieve information about the first block of a heap by using the [**Heap32First**](/windows/win32/TlHelp32/nf-tlhelp32-heap32first?branch=master) function. After retrieving the first block of a heap, you can retrieve information about subsequent blocks of the same heap by using the [**Heap32Next**](/windows/win32/TlHelp32/nf-tlhelp32-heap32next?branch=master) function. **Heap32First** and **Heap32Next** fill a [**HEAPENTRY32**](/windows/win32/TlHelp32/ns-tlhelp32-tagheapentry32?branch=master) structure with information for the appropriate block of a heap.

You can retrieve an extended error status code for [**Heap32ListFirst**](/windows/win32/TlHelp32/nf-tlhelp32-heap32listfirst?branch=master), [**Heap32ListNext**](/windows/win32/TlHelp32/nf-tlhelp32-heap32listnext?branch=master), [**Heap32First**](/windows/win32/TlHelp32/nf-tlhelp32-heap32first?branch=master), and [**Heap32Next**](/windows/win32/TlHelp32/nf-tlhelp32-heap32next?branch=master) by using the [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) function.

> [!Note]  
> The heap identifier, which is specified in the **th32HeapID** member of the [**HEAPENTRY32**](/windows/win32/TlHelp32/ns-tlhelp32-tagheapentry32?branch=master) structure, has meaning only to the tool help functions. It is not a handle, nor is it usable by other functions.

 

 

 




