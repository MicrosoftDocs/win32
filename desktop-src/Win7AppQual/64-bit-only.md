---
description: 64-Bit Only
ms.assetid: 5d0188a5-ef5f-409e-9d2d-7639d99edc1d
title: 64-Bit Only
ms.topic: article
ms.date: 05/31/2018
---

# 64-Bit Only

## Affected Platforms

**Servers** - Windows Server 2008 R2  



## Feature Impact

 **Severity** - Low  
**Frequency** - High  






## Description

Windows Server 2008 R2 ships with a 64-bit SKU only; no 32-bit SKU is available for the server version of the operating system. However, a 32-bit SKU continues to be available for the Windows 7 client.

## Manifestation of Impact

This will impact three areas:

-   32-bit drivers
-   32-bit plug-ins
-   16-bit executables

## Solution for 32-bit Drivers

Recompile 32-bit drivers as signed 64-bit drivers.

## Solution for 32-bit Plug-ins

WoW64, an x86 emulator, allows 32-bit Windows-based applications to run seamlessly on 64-bit Windows. WoW64 is now an optional feature that you must install if it is necessary to run 32-bit code.

The system isolates 32-bit applications from 64-bit applications, which includes preventing file and registry collisions. Console, GUI, and service applications are supported. The system provides interoperability across the 32/64 boundary for scenarios such as cut and paste and COM. However, 32-bit processes cannot load 64-bit DLLs, and 64-bit processes cannot load 32-bit DLLs. We commonly see this in shell plug-ins written for Windows Explorer.

A 32-bit application can detect whether it is running under WOW64 by calling the IsWow64Process function. The application can obtain additional information about the processor by using the GetNativeSystemInfo function

Note that 64-bit Windows does not support running 16-bit Windows-based applications. The primary reason is that handles have 32 significant bits on 64-bit Windows. Therefore, handles cannot be truncated and passed to 16-bit applications without loss of data. Attempts to launch 16-bit applications fail with the following error: ERROR\_BAD\_EXE\_FORMAT.

## Solution for 16-bit Executables

64-bit Windows recognizes a limited number of specific 16-bit installer programs and substitutes a ported 32-bit version. The list of substitutions is stored in the registry under the following key: HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\NtVdm64 There is built-in support for several installer engines, including InstallShield 5.x installers. Note that the 64-bit Windows Installer can seamlessly install 32-bit MSI-based applications on 64-bit Windows.

## Links to Other Resources

-   [Running 32-bit Applications](/windows/desktop/WinProg64/running-32-bit-applications)
-   [Performance and Memory Consumption](/windows/desktop/WinProg64/performance-and-memory-consumption)
-   [WOW64 Implementation Details](/windows/desktop/WinProg64/wow64-implementation-details)
-   [Registry Redirector](/windows/desktop/WinProg64/registry-redirector)
-   [File System Redirector](/windows/desktop/WinProg64/file-system-redirector)
-   [Memory Management](/windows/desktop/WinProg64/memory-management)
-   [Processor Affinity](/windows/desktop/WinProg64/processor-affinity)
-   [Interprocess Communication](/windows/desktop/WinProg64/interprocess-communication)
-   [Application Installation on 64-bit Systems](/windows/desktop/WinProg64/application-installation)
-   [Debugging WOW64](/windows/desktop/WinProg64/debugging-wow64)
-   [**IsWow64Process Function**](/windows/desktop/api/wow64apiset/nf-wow64apiset-iswow64process)
-   [**GetNativeSystemInfo Function**](/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getnativesysteminfo)

 

 
