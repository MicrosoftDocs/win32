---
description: The virtual memory functions manipulate pages of memory. The functions use the size of a page on the current computer to round off specified sizes and addresses.
ms.assetid: 509cd529-ff79-4b07-9e09-3c5ae65f6cba
title: Allocating Virtual Memory
ms.topic: article
ms.date: 05/31/2018
---

# Allocating Virtual Memory

The virtual memory functions manipulate pages of memory. The functions use the size of a page on the current computer to round off specified sizes and addresses.

The [**VirtualAlloc**](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc) function performs one of the following operations:

-   Reserves one or more free pages.
-   Commits one or more reserved pages.
-   Reserves and commits one or more free pages.

You can specify the starting address of the pages to be reserved or committed, or you can allow the system to determine the address. The function rounds the specified address to the appropriate page boundary. Reserved pages are not accessible, but committed pages can be allocated with **PAGE\_READWRITE**, **PAGE\_READONLY**, or **PAGE\_NOACCESS** access. When pages are committed, memory charges are allocated from the overall size of RAM and paging files on disk, but each page is initialized and loaded into physical memory only at the first attempt to read from or write to that page. You can use normal pointer references to access memory committed by the [**VirtualAlloc**](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc) function.

 

 
