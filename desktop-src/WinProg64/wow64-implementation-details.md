---
title: WOW64 Implementation Details
description: The WOW64 emulator runs in user mode.
ms.assetid: 93daf9d0-dfdb-42c3-8c3d-397b21991e83
keywords:
- WOW64 64-bit Windows Programming , environment variables
- WOW64 64-bit Windows Programming , implementation
ms.topic: article
ms.date: 05/31/2018
---

# WOW64 Implementation Details

The WOW64 emulator runs in user mode. It provides an interface between the 32-bit version of Ntdll.dll and the kernel of the processor, and it intercepts kernel calls. The WOW64 emulator consists of the following DLLs:

-   Wow64.dll provides the core emulation infrastructure and the thunks for the Ntoskrnl.exe entry-point functions.
-   Wow64Win.dll provides thunks for the Win32k.sys entry-point functions.
-   (x64 only) Wow64Cpu.dll provides support for running x86 programs on x64.
-   (Intel Itanium only) IA32Exec.bin contains the x86 software emulator.
-   (Intel Itanium only) Wowia32x.dll provides the interface between IA32Exec.bin and WOW64.
-   (ARM64 only) xtajit.dll contains the x86 software emulator.
-   (ARM64 only) wowarmw.dll provides support for running ARM32 programs on ARM64.

These DLLs, along with the 64-bit version of Ntdll.dll, are the only 64-bit binaries that can be loaded into a 32-bit process. On Windows 10 on ARM, CHPE (Compiled Hybrid Portable Executable) binaries may also be loaded into an x86 32-bit process.

At startup, Wow64.dll loads the x86 version of Ntdll.dll (or the CHPE version, if enabled) and runs its initialization code, which loads all necessary 32-bit DLLs. Almost all 32-bit DLLs are unmodified copies of 32-bit Windows binaries, though some are loaded as CHPE for performance reasons. Some of these DLLs are written to behave differently on WOW64 than they do on 32-bit Windows, usually because they share memory with 64-bit system components. All user-mode address space above the 32-bit limit is reserved by the system. For more information, see [Performance and Memory Consumption under WOW64](performance-and-memory-consumption.md).

Instead of using the x86 system-service call sequence, 32-bit binaries that make system calls are rebuilt to use a custom calling sequence. This calling sequence is inexpensive for WOW64 to intercept because it remains entirely in user mode. When the custom calling sequence is detected, the WOW64 CPU transitions back to native 64-bit mode and calls into Wow64.dll. Thunking is done in user mode to reduce the impact on the 64-bit kernel and to reduce the risk of a bug in the thunk that might cause a kernel-mode crash, data corruption, or a security hole. The thunks extract arguments from the 32-bit stack, extend them to 64 bits, then make the native system call.

## Environment Variables

When a 32-bit process is created by a 64-bit process, or when a 64-bit process is created by a 32-bit process, WOW64 sets the environment variables for the created process as shown in the following table.



| Process                   | Environment variables                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 64-bit process<br/> | PROCESSOR\_ARCHITECTURE=AMD64 or PROCESSOR\_ARCHITECTURE=IA64 or PROCESSOR\_ARCHITECTURE=ARM64<br/> ProgramFiles=%ProgramFiles%<br/> ProgramW6432=%ProgramFiles%<br/> CommonProgramFiles=%CommonProgramFiles%<br/> CommonProgramW6432=%CommonProgramFiles%<br/> **Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** The ProgramW6432 and CommonProgramW6432 environment variables were added starting with Windows 7 and Windows Server 2008 R2. <br/> |
| 32-bit process<br/> | PROCESSOR\_ARCHITECTURE=x86<br/> PROCESSOR\_ARCHITEW6432=%PROCESSOR\_ARCHITECTURE%<br/> ProgramFiles=%ProgramFiles(x86)%<br/> ProgramW6432=%ProgramFiles%<br/> CommonProgramFiles=%CommonProgramFiles(x86)%<br/> CommonProgramW6432=%CommonProgramFiles%<br/>                                                                                                                                                                                                                  |



 

## Global Hooks

The [**SetWindowsHookEx**](/windows/win32/api/winuser/nf-winuser-setwindowshookexa) function can be used to inject a DLL into another process if the following conditions are met:

-   A 32-bit DLL can be injected only into a 32-bit process, and a 64-bit DLL can be injected only into a 64-bit process. It is not possible to inject a 32-bit DLL into a 64-bit process or vice versa.
-   The 32-bit and 64-bit DLLs must have different names.
-   The architectures of the DLL and the process must match. For instance, you cannot inject a 32-bit x86 DLL into a 32-bit ARM process.

For more information, see [**SetWindowsHookEx**](/windows/win32/api/winuser/nf-winuser-setwindowshookexa).

Be aware that the **WH\_MOUSE**, **WH\_KEYBOARD**, **WH\_JOURNAL\***, **WH\_SHELL**, and low-level hooks can be called on the thread that installed the hook rather than the thread processing the hook. For these hooks, it is possible that both the 32-bit and 64-bit hooks will be called if a 32-bit hook is ahead of a 64-bit hook in the hook chain. For more information, see [Using Hooks](../winmsg/using-hooks.md).

 

