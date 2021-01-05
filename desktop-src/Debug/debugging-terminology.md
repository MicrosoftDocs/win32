---
description: The following terms are used when describing debugging.
ms.assetid: 580f2787-d944-4350-a2c2-c00816b3f515
title: Debugging Terminology
ms.topic: article
ms.date: 05/31/2018
---

# Debugging Terminology

The following terms are used when describing debugging.

<dl> <dt>

<span id="Blue_screen"></span><span id="blue_screen"></span><span id="BLUE_SCREEN"></span>Blue screen
</dt> <dd>

When the system encounters a hardware problem, data inconsistency, or similar error, it may display a blue screen containing information that can be used to determine the cause of the error. This information includes the STOP code and whether a crash dump file was created. It may also include a list of loaded drivers and a stack trace.

</dd> <dt>

<span id="Crash_dump_file"></span><span id="crash_dump_file"></span><span id="CRASH_DUMP_FILE"></span>Crash dump file
</dt> <dd>

You can configure the system to write information to a crash dump file on your hard disk whenever a STOP code is generated. The file contains information the debugger can use to analyze the error. This file can be as big as the physical memory contained in the computer.

</dd> <dt>

<span id="Debugger"></span><span id="debugger"></span><span id="DEBUGGER"></span>Debugger
</dt> <dd>

A program designed to help detect, locate, and correct errors in another program. It allows the developer to step through the execution of the process and its threads, monitoring memory, variables, and other elements of process and thread context.

</dd> <dt>

<span id="Kernel_mode"></span><span id="kernel_mode"></span><span id="KERNEL_MODE"></span>Kernel mode
</dt> <dd>

The processor mode in which system services and device drivers run. All interfaces and CPU instructions are available, and all memory is accessible.

</dd> <dt>

<span id="Minidump_file"></span><span id="minidump_file"></span><span id="MINIDUMP_FILE"></span>Minidump file
</dt> <dd>

Applications can produce user-mode minidump files, which contain a useful subset of the information contained in a crash dump file. For more information, see [Minidump Files](minidump-files.md).

</dd> <dt>

<span id="STOP_code"></span><span id="stop_code"></span><span id="STOP_CODE"></span>STOP code
</dt> <dd>

The error code that identifies the error that stopped the system kernel from continuing to run.

</dd> <dt>

<span id="Symbol_files"></span><span id="symbol_files"></span><span id="SYMBOL_FILES"></span>Symbol files
</dt> <dd>

All system applications, drivers, and DLLs are built such that their debugging information resides in separate files known as symbol files. Therefore, the system is smaller and faster, yet it can still be debugged if the symbol files are installed. For more information, see [Symbol Files](symbol-files.md).

</dd> <dt>

<span id="User_mode"></span><span id="user_mode"></span><span id="USER_MODE"></span>User mode
</dt> <dd>

The processor mode in which applications run. A limited set of interfaces are available in this mode, and access to system data is limited.

</dd> </dl>

## Related topics

<dl> <dt>

[Configuring Automatic Debugging](configuring-automatic-debugging.md)
</dt> </dl>

 

 



