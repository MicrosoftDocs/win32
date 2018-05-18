---
title: Heap Lists and Heap Walking
description: A snapshot that includes the heap list for a specified process contains identification information for each heap associated with the specified process and detailed information about each heap.
ms.assetid: '631096fd-cb2c-4b19-aa71-d47060e2715c'
---

# Heap Lists and Heap Walking

A snapshot that includes the heap list for a specified process contains identification information for each heap associated with the specified process and detailed information about each heap. You can retrieve an identifier for the first heap of the heap list by using the [**Heap32ListFirst**](heap32listfirst.md) function. After retrieving the first heap in the list, you can traverse the heap list for subsequent heaps associated with the process by using the [**Heap32ListNext**](heap32listnext.md) function. **Heap32ListFirst** and **Heap32ListNext** fill a [**HEAPLIST32**](heaplist32-str.md) structure with the process identifier, the heap identifier, and flags describing the heap.

You can retrieve information about the first block of a heap by using the [**Heap32First**](heap32first.md) function. After retrieving the first block of a heap, you can retrieve information about subsequent blocks of the same heap by using the [**Heap32Next**](heap32next.md) function. **Heap32First** and **Heap32Next** fill a [**HEAPENTRY32**](heapentry32-str.md) structure with information for the appropriate block of a heap.

You can retrieve an extended error status code for [**Heap32ListFirst**](heap32listfirst.md), [**Heap32ListNext**](heap32listnext.md), [**Heap32First**](heap32first.md), and [**Heap32Next**](heap32next.md) by using the [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) function.

> [!Note]  
> The heap identifier, which is specified in the **th32HeapID** member of the [**HEAPENTRY32**](heapentry32-str.md) structure, has meaning only to the tool help functions. It is not a handle, nor is it usable by other functions.

 

 

 




