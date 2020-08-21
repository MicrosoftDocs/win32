---
title: Debugging WOW64
description: Applications running under WOW64 can be debugged with either an x86-hosted debugger or a native debugger.
ms.assetid: e0945bdd-998d-4531-869f-21c505cb2135
keywords:
- WOW64 64-bit Windows Programming , debugging
- debugging WOW64 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# Debugging WOW64

Applications running under WOW64 can be debugged two ways:

-   Use an x86-hosted debugger such as NTSD, WinDbg, or Visual Studio. The 32-bit NTSD is installed to %systemroot%\\syswow64 on retail installations. Note that x86 debuggers can be used to debug x86 code, but cannot be used to disassemble or set breakpoints within the WOW64 thunk layer because it is 64-bit native code.
-   Use a native debugger such as CDB, NTSD, or WinDbg and the WOW64 debugger extension, Wow64exts.dll. If the native debugger breaks while the processor is in x86 mode, the debugger presents the process as an x86 process. If the processor is in native mode, the debugger presents the process as native.

CDB, NTSD, and WinDbg are included in Debugging Tools for Windows. For more information, see the [Debugging Tools for Windows](/windows-hardware/drivers/debugger/) documentation.

The Wow64exts debugger extension is installed with WinDbg. Use the !load wow64exts command to load the debugger extension. The following table lists the !wow64exts debugger extension commands.



| Command                | Description                                                                                                                              |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| !wow64exts.sw          | Switches between x86 and native mode.                                                                                                    |
| !wow64exts.k *count*   | Dumps a combined 32-bit/64-bit stack trace. If *count* is specified, the command dumps the first *count* addresses in each stack trace.  |
| !wow64exts.info        | Dumps basic information about the PEB of the process, the TEB of the current thread, and thread local storage (TLS) slots used by WOW64. |
| !wow64exts.r *address* | Dumps context for the specified address. If *address* is not specified, the command dumps context for the processor.                     |



 

 

 