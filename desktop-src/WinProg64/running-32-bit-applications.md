---
title: Running 32-bit Applications
description: Run 32-bit Windows-based applications seamlessly on 64-bit Windows with the WOW64 x86 emulator. Also learn about the registry director, file system redirector, application installation on 64-bit systems, and debugging WOW64.
ms.assetid: ac75c5af-86e8-4282-9a8e-8db3c22cbda0
keywords:
- WOW64 64-bit Windows Programming
- WOW64 64-bit Windows Programming , about
- 32-bit applications on 64-bit Windows 64-bit Windows Programming
- 64-bit Windows programming guide 64-bit Windows Programming , WOW64 See WOW64
ms.topic: article
ms.date: 05/31/2018
---

# Running 32-bit Applications

WOW64 is the x86 emulator that allows 32-bit Windows-based applications to run seamlessly on 64-bit Windows. This allows for 32-bit (x86) Windows applications to run seamlessly in 64-bit (x64) Windows, as well as for 32-bit (x86) and 32-bit (ARM) Windows applications to run seamlessly in 64-bit (ARM64) Windows. WOW64 is provided with the operating system and does not have to be explicitly enabled. For more information, see [WOW64 Implementation Details](wow64-implementation-details.md).

The system isolates 32-bit applications from 64-bit applications, which includes preventing file and registry collisions. Console, GUI, and service applications are supported. The system provides interoperability across the 32/64 boundary for scenarios such as cut and paste and COM. However, 32-bit processes cannot load 64-bit DLLs for execution, and 64-bit processes cannot load 32-bit DLLs for execution. This restriction does not apply to DLLs loaded as data files or image resource files; for more information, see [**LoadLibraryEx**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibraryexa).

A 32-bit application can detect whether it is running under WOW64 by calling the [**IsWow64Process**](/windows/desktop/api/wow64apiset/nf-wow64apiset-iswow64process) function (use [**IsWow64Process2**](/windows/desktop/api/wow64apiset/nf-wow64apiset-iswow64process2) if targeting Windows 10). The application can obtain additional information about the processor by using the [**GetNativeSystemInfo**](/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getnativesysteminfo) function.

Note that 64-bit Windows does not support running 16-bit Windows-based applications. The primary reason is that handles have 32 significant bits on 64-bit Windows. Therefore, handles cannot be truncated and passed to 16-bit applications without loss of data. Attempts to launch 16-bit applications fail with the following error: **ERROR\_BAD\_EXE\_FORMAT**.

## In this Section

-   [Performance and Memory Consumption Under WOW64](performance-and-memory-consumption.md)
-   [WOW64 Implementation Details](wow64-implementation-details.md)
-   [Registry Redirector](registry-redirector.md)
-   [File System Redirector](file-system-redirector.md)
-   [Memory Management](memory-management.md)
-   [Processor Affinity](processor-affinity.md)
-   [Interprocess Communication](interprocess-communication.md)
-   [Application Installation](application-installation.md)
-   [Debugging WOW64](debugging-wow64.md)

 

 