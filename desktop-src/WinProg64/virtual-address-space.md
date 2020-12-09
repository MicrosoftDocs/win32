---
title: Virtual Address Space (Programming Guide for 64-bit Windows)
description: By default, 64-bit Microsoft Windows-based applications have a user-mode address space of several terabytes.
ms.assetid: c5c4af39-727e-46e1-821e-8342c555bf4c
keywords:
- 64-bit Windows programming guide 64-bit Windows Programming , virtual address space
- virtual address space 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# Virtual Address Space (Programming Guide for 64-bit Windows)

By default, 64-bit Microsoft Windows-based applications have a user-mode address space of several terabytes. For precise values, see [Memory Limits for Windows and Windows Server Releases](/windows/desktop/Memory/memory-limits-for-windows-releases). However, applications can specify that the system should allocate all memory for the application below 2 gigabytes. This feature is beneficial for 64-bit applications if the following conditions are true:

-   A 2 GB address space is sufficient.
-   The code has many pointer truncation warnings.
-   Pointers and integers are freely mixed.
-   The code has polymorphism using 32-bit data types.

All pointers are still 64-bit pointers, but the system ensures that every memory allocation occurs below the 2 GB limit, so that if the application truncates a pointer, no significant data is lost. Pointers can be truncated to 32-bit values, then extended to 64-bit values by either sign extension or zero extension.

To specify this memory limitation, use the **/LARGEADDRESSAWARE:NO** linker option. Note that **/LARGEADDRESSAWARE:NO** is ignored for an ARM64 binary. However, be aware that problems can occur when using this option. If you build a DLL that uses this option and the DLL is called by an application that does not use this option, the DLL could truncate a 64-bit pointer whose upper 32 bits are significant. This can cause application failure without any warning.

 

 
