---
description: Data Execution Prevention (DEP) is a system-level memory protection feature that is built into the operating system starting with Windows XP and Windows Server 2003.
ms.assetid: 75cd83a5-4b77-4ca9-b595-e32d0dd609d0
title: Data Execution Prevention
ms.topic: article
ms.date: 01/25/2022
ms.custom: seo-windows-dev
---

# Data Execution Prevention

Data Execution Prevention (DEP) is a system-level memory protection feature that is built into the operating system starting with Windows XP and Windows Server 2003. DEP enables the system to mark one or more pages of memory as non-executable. Marking memory regions as non-executable means that code cannot be run from that region of memory, which makes it harder for the exploitation of buffer overruns.

DEP prevents code from being run from data pages such as the default heap, stacks, and memory pools. If an application attempts to run code from a data page that is protected, a memory access violation exception occurs, and if the exception is not handled, the calling process is terminated.

DEP is not intended to be a comprehensive defense against all exploits; it is intended to be another tool that you can use to secure your application.

## How Data Execution Prevention Works

If an application attempts to run code from a protected page, the application receives an exception with the status code **STATUS\_ACCESS\_VIOLATION**. If your application must run code from a memory page, it must allocate and set the proper virtual [memory protection](memory-protection.md) attributes. The allocated memory must be marked **PAGE\_EXECUTE**, **PAGE\_EXECUTE\_READ**, **PAGE\_EXECUTE\_READWRITE**, or **PAGE\_EXECUTE\_WRITECOPY** when allocating memory. Heap allocations made by calling the **malloc** and [**HeapAlloc**](/windows/win32/api/HeapApi/nf-heapapi-heapalloc) functions are non-executable.

Applications cannot run code from the default process heap or the stack.

DEP is configured at system boot according to the no-execute page protection policy setting in the boot configuration data. An application can get the current policy setting by calling the [GetSystemDEPPolicy](/windows/win32/api/WinBase/nf-winbase-getsystemdeppolicy) function. Depending on the policy setting, an application can change the DEP setting for the current process by calling the [SetProcessDEPPolicy](/windows/win32/api/WinBase/nf-winbase-setprocessdeppolicy) function.

## Programming Considerations

An application can use the [VirtualAlloc](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc) function to allocate executable memory with the appropriate memory protection options. It is suggested that an application set, at a minimum, the **PAGE\_EXECUTE** memory protection option. After the executable code is generated, it is recommended that the application set memory protections to disallow write access to the allocated memory. Applications can disallow write access to allocated memory by using the [VirtualProtect](/windows/win32/api/memoryapi/nf-memoryapi-virtualprotect) function. Disallowing write access ensures maximum protection for executable regions of process address space. You should attempt to create applications that use the smallest executable address space possible, which minimizes the amount of memory that is exposed to memory exploitation.

You should also attempt to control the layout of your application's virtual memory and create executable regions. These executable regions should be located in a lower memory space than non-executable regions. By locating executable regions below non-executable regions, you can help prevent a buffer overflow from overflowing into the executable area of memory.

## Application Compatibility

Some application functionality is incompatible with DEP. Applications that perform dynamic code generation (such as Just-In-Time code generation) and do not explicitly mark generated code with execute permission may have compatibility issues on computers that are using DEP. Applications written to the Active Template Library (ATL) version 7.1 and earlier can attempt to execute code on pages marked as non-executable, which triggers an NX fault and terminates the application; for more information, see [SetProcessDEPPolicy](/windows/win32/api/WinBase/nf-winbase-setprocessdeppolicy). Most applications that perform actions incompatible with DEP must be updated to function properly.

A small number of executable files and libraries may contain executable code in the data section of an image file. In some cases, applications may place small segments of code (commonly referred to as thunks) in the data sections. However, DEP marks sections of the image file that is loaded in memory as non-executable unless the section has the executable attribute applied.

Therefore, executable code in data sections should be migrated to a code section, or the data section that contains the executable code should be explicitly marked as executable. The executable attribute, **IMAGE\_SCN\_MEM\_EXECUTE**, should be added to the **Characteristics** field of the corresponding section header for sections that contain executable code. For more information about adding attributes to a section, see the documentation included with your linker.

## Related topics

[Data Execution Prevention](/previous-versions/windows/it-pro/windows-xp/bb457155(v=technet.10)#data-execution-prevention)
