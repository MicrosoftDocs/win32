---
description: '4-Gigabyte Tuning: BCDEdit and Boot.ini'
ms.assetid: 991eb86f-9e6f-4084-8b6f-f979e42104b5
title: '4-Gigabyte Tuning: BCDEdit and Boot.ini'
ms.topic: article
ms.date: 05/31/2018
---

# 4-Gigabyte Tuning: BCDEdit and Boot.ini

On 32-bit editions of Windows, applications have 4 gigabyte (GB) of virtual address space available. The virtual address space is divided so that 2 GB is available to the application and the other 2 GB is available only to the system. The 4-gigabyte tuning (4GT or 4GT RAM Tuning) feature, enabled with the *BCDEdit /set increaseuserva* command, increases the virtual address space that is available to the application up to 3 GB, and reduces the amount available to the system to between 1 and 2 GB.

For applications that are memory-intensive, such as database management systems (DBMS), the use of a larger virtual address space can provide considerable performance and scalability benefits. However, the file cache, paged pool, and nonpaged pool are smaller, which can adversely affect applications with heavy networking or I/O. Therefore, you might want to test your application under load, and examine the performance counters to determine whether your application benefits from the larger address space.

To enable 4GT, use the [BCDEdit /set](/windows-hardware/drivers/devtest/bcdedit--set) command to set the **increaseuserva** boot entry option to a value between 2048 (2 GB) and 3072 (3 GB).

**Windows Server 2003 and earlier:** To enable 4GT, add the **/3GB** switch to the Boot.ini file. The **/3GB** switch is supported on the following systems:

-   Windows Server 2003
-   Windows XP Professional

The **/3GB** switch makes a full 3 GB of virtual address space available to applications and reduces the amount available to the system to 1 GB. On Windows Server 2003, the amount of address space available to applications can be adjusted by setting the **/USERVA** switch in Boot.ini to a value between 2048 and 3072, which increases the amount of address space available to the system. This can help maintain overall system performance when the application requires more than 2 GB but less than 3 GB of address space.

To enable an application to use the larger address space, set the [**IMAGE\_FILE\_LARGE\_ADDRESS\_AWARE**](/windows/desktop/api/dbghelp/ns-dbghelp-loaded_image) flag in the image header. The linker included with Microsoft Visual C++ supports the **/LARGEADDRESSAWARE** switch to set this flag. Setting this flag and then running the application on a system that does not have 4GT support should not affect the application.

On 64-bit editions of Windows, 32-bit applications marked with the [**IMAGE\_FILE\_LARGE\_ADDRESS\_AWARE**](/windows/desktop/api/dbghelp/ns-dbghelp-loaded_image) flag have 4 GB of address space available.

**Itanium editions of Windows Server 2003:** Prior to SP1, 32-bit processes have only 2 GB of address space available.

Use the following guidelines to support 4GT in applications:

-   Addresses near the 2-GB boundary are typically used by various system DLLs. Therefore, a 32-bit process cannot allocate more than 2 GB of contiguous memory, even if the entire 4-GB address space is available.
-   To retrieve the amount of total user virtual space, use the [**GlobalMemoryStatusEx**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-globalmemorystatusex) function. To retrieve the highest possible user address, use the [**GetSystemInfo**](/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getsysteminfo) function. Always detect the real value at runtime, and avoid using hard-wired constant definitions such as: `#define HIGHEST_USER_ADDRESS 0xC0000000`.
-   Avoid signed comparisons with pointers, because they might cause applications to crash on a 4GT-enabled system. A condition such as the following is false for a pointer that is above 2 GB: `if (pointer > 40000000)`.
-   Code that uses the highest bit of a pointer for an application-defined purpose will fail when 4GT is enabled. For example, a 32-bit word might be considered a user-mode address if it is below 0x80000000, and an error code if above. This is not true with 4GT.

[**VirtualAlloc**](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc) usually returns low addresses before high addresses. Therefore, your process may not use very high addresses unless it allocates a lot of memory or has a fragmented virtual address space. To force allocations to allocate from higher addresses before lower addresses for testing purposes, specify **MEM\_TOP\_DOWN** when calling **VirtualAlloc** or set the following registry value to 0x100000:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Control**\\**Session Manager**\\**Memory Management**\\**AllocationPreference**

## Related topics

<dl> <dt>

[Memory Limits for Windows Releases](memory-limits-for-windows-releases.md)
</dt> <dt>

[Physical Address Extension](physical-address-extension.md)
</dt> <dt>

[4GT Technical Reference](/previous-versions/windows/it-pro/windows-server-2003/cc778496(v=ws.10))
</dt> </dl>

 

 
