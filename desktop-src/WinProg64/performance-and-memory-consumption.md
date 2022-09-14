---
title: Performance and Memory Consumption Under WOW64
description: Performance and memory consumption under WOW64 are determined by the following factors.
ms.assetid: 77759840-7b1a-4956-a038-d6374b6ec354
keywords:
- performance under WOW64 64-bit Windows Programming
- memory consumption under WOW64 64-bit Windows Programming
- WOW64 64-bit Windows Programming , performance
- WOW64 64-bit Windows Programming , memory consumption
ms.topic: article
ms.date: 05/31/2018
---

# Performance and Memory Consumption Under WOW64

Performance and memory consumption under WOW64 are determined by the following factors:

-   Processor hardware. Instruction emulation is performed on the chip. On the x64 processor, x86 instructions are executed natively by the processor. Therefore, execution speed under WOW64 on x64 is similar to its speed under 32-bit Windows. On the Intel Itanium processor and any ARM64 processors, more software is involved in the emulation, and performance suffers as a result.
-   API thunk overhead. This overhead is small compared to system calls to the NT kernel. NT kernel functions are intended to be called infrequently.
-   Virtual memory size. On the Intel Itanium processor, WOW64 adds significant overhead if two or more instances of the same 32-bit application are running concurrently. This is due to the native 8 KB pages on the Intel Itanium, which complicates the emulation of the native 4 KB pages on the x86 architecture (more pages are marked as writable; all writable pages are private to the process). This can adversely affect the scalability of Terminal Services on certain processors. This is not the case for the x64 processor.
-   Working set. WOW64 increases the size of the application's working set.

WOW64 enables 32-bit applications to take advantage of the 64-bit kernel. Therefore, 32-bit applications can use a larger number of kernel handles and window handles. However, 32-bit applications may not be able to create as many threads under WOW64 as they can when running natively on x86-based systems because WOW64 allocates an additional 64-bit stack (usually 512 KB) for each thread. In addition, some amount of address space is reserved for WOW64 itself and the data structures it uses. The amount reserved depends on the processor; more is reserved on the Intel Itanium than on the x64 or ARM64 processors.

If the application has the [**IMAGE\_FILE\_LARGE\_ADDRESS\_AWARE**](/windows/desktop/api/dbghelp/ns-dbghelp-loaded_image) flag set in the image header, each 32-bit application receives 4 GB of virtual address space in the WOW64 environment. If the **IMAGE\_FILE\_LARGE\_ADDRESS\_AWARE** flag is not set, each 32-bit application receives 2 GB of virtual address space in the WOW64 environment.

 

 