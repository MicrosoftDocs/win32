---
title: Alignment Faults
description: Alignment Faults
ms.assetid: 16e69aec-3aec-4684-bf37-b3e5db6e4f87
keywords:
- alignment faults 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# Alignment Faults

The system alignment-fault handler is turned off by default on Itanium-based systems. Therefore, any unaligned data access generates an exception that will not automatically be fixed by the system unless the application catches the exception in a [frame-based exception handler](/windows/desktop/Debug/frame-based-exception-handling). To enable the system alignment-fault hander, call the [**SetErrorMode**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-seterrormode) function with **SEM\_NOALIGNMENTFAULTEXCEPT**. However, note that processes may experience severe performance degradation if the system alignment-fault handler is enabled and the process generates alignment faults.

If the WinDbg debugger has been installed as the system debugger, WinDbg will automatically be launched if any process on the system generates an unhandled exception. If you do not have a debugger installed as your system debugger, the system displays a dialog box stating that your application has encountered an error and providing the opportunity to report the problem to Microsoft.

On x64 and ARM64 systems, any alignment faults are handled by a combination of hardware and software. For best performance, all access to memory should be properly aligned. In addition, unaligned [interlocked variable access](/windows/desktop/Sync/interlocked-variable-access) should be avoided on ARM64, as these operations are not atomic-safe.

 

 