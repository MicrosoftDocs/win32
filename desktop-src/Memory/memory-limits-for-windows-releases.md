---
description: Describes the memory limits for supported Windows and Windows Server releases and provides lists of memory limits.
ms.assetid: de09c8af-0ed8-4fd4-b8e8-2c921aafe6f2
title: Memory Limits for Windows and Windows Server Releases
ms.topic: reference
ms.date: 06/11/2025
---

# Memory Limits for Windows and Windows Server Releases

This topic describes the memory limits for supported Windows and Windows Server releases.

Limits on memory and address space vary by platform, operating system, and by whether the **IMAGE\_FILE\_LARGE\_ADDRESS\_AWARE** value of the [**LOADED\_IMAGE**](/windows/win32/api/dbghelp/ns-dbghelp-loaded_image) structure and [4-gigabyte tuning](4-gigabyte-tuning.md) (4GT) are in use. **IMAGE\_FILE\_LARGE\_ADDRESS\_AWARE** is set or cleared by using the [/LARGEADDRESSAWARE](/cpp/build/reference/largeaddressaware-handle-large-addresses) linker option.

4-gigabyte tuning (4GT), also known as application memory tuning, or the /3GB switch, is a technology (only applicable to 32 bit systems) that alters the amount of virtual address space available to user mode applications. Enabling this technology reduces the overall size of the system virtual address space and therefore system resource maximums. For more information, see [What is 4GT]( /previous-versions/windows/it-pro/windows-server-2003/cc786709(v=ws.10)).

Limits on physical memory for 32-bit platforms also depend on the [Physical Address Extension](physical-address-extension.md) (PAE), which allows 32-bit Windows systems to use more than 4 GB of physical memory.

> [!NOTE]
> For information about memory limits in Windows Server 2019 and later, see [Comparison of locks and limits in Windows Server](/windows-server/get-started/locks-limits).

## Memory and Address Space Limits

The following table specifies the limits on memory and address space for supported releases of Windows. Unless otherwise noted, the limits in this table apply to all supported releases.

| Memory type | Limit on X86 | Limit in 64-bit Windows |
|-------------|--------------|-------------------------|
| User-mode virtual address space for each 32-bit process | 2 GB<br/> Up to 3 GB with **IMAGE\_FILE\_LARGE\_ADDRESS\_AWARE** and 4GT | 2 GB with **IMAGE\_FILE\_LARGE\_ADDRESS\_AWARE** cleared (default)<br/> 4 GB with **IMAGE\_FILE\_LARGE\_ADDRESS\_AWARE** set |
| User-mode virtual address space for each 64-bit process | Not applicable | **With IMAGE\_FILE\_LARGE\_ADDRESS\_AWARE** set (default):<br/> **x64: Windows 8.1 and Windows Server 2012 R2 or later:** 128 TB<br/> **x64: Windows 8 and Windows Server 2012 or earlier** 8 TB<br/> **Intel Itanium-based systems:** 7 TB<br/> <br/> 2 GB with **IMAGE\_FILE\_LARGE\_ADDRESS\_AWARE** cleared |
| Kernel-mode virtual address space | 2 GB<br/> From 1 GB to a maximum of 2 GB with 4GT | **Windows 8.1 and Windows Server 2012 R2 or later:** 128 TB<br/> **Windows 8 and Windows Server 2012 or earlier** 8 TB |
| Paged pool | 384 GB or system commit limit, whichever is smaller. **Windows 8.1 and Windows Server 2012 R2:** 15.5 TB or system commit limit, whichever is smaller. <br/> **Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:** Limited by available kernel-mode virtual address space. Starting with Windows Vista with Service Pack 1 (SP1), the paged pool can also be limited by the [PagedPoolLimit](memory-management-registry-keys.md) registry key value.<br/> **Windows Home Server and Windows Server 2003:** 530 MB<br/> **Windows XP:** 490 MB | 384 GB or system commit limit, whichever is smaller **Windows 8.1 and Windows Server 2012 R2:** 15.5 TB or system commit limit, whichever is smaller. <br/> **Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:** 128 GB or system commit limit, whichever is smaller<br/> **Windows Server 2003 and Windows XP:** Up to 128 GB depending on configuration and RAM. |
| Nonpaged pool | 75% of RAM or 2 GB, whichever is smaller. **Windows 8.1 and Windows Server 2012 R2:** RAM or 16 TB, whichever is smaller (address space is limited to 2 x RAM).<br/> **Windows Vista:** Limited only by kernel mode virtual address space and physical memory. Starting with Windows Vista with SP1, the nonpaged pool can also be limited by the [NonPagedPoolLimit](memory-management-registry-keys.md) registry key value.<br/> **Windows Home Server, Windows Server 2003 and Windows XP:** 256 MB, or 128 MB with 4GT | RAM or 128 GB, whichever is smaller (address space is limited to 2 x RAM) **Windows 8.1 and Windows Server 2012 R2:** RAM or 16 TB, whichever is smaller (address space is limited to 2 x RAM).<br/> **Windows Server 2008 R2, Windows 7 and Windows Server 2008:** 75% of RAM up to a maximum of 128 GB<br/> **Windows Vista:** 40% of RAM up to a maximum of 128 GB.<br/> **Windows Server 2003 and Windows XP:** Up to 128 GB depending on configuration and RAM. |
| System cache virtual address space (physical size limited only by physical memory) | Limited by available kernel-mode virtual address space or the [SystemCacheLimit](memory-management-registry-keys.md) registry key value.<br/> **Windows 8.1 and Windows Server 2012 R2:** 16 TB.<br/> **Windows Vista:** Limited only by kernel mode virtual address space. Starting with Windows Vista with SP1, system cache virtual address space can also be limited by the [SystemCacheLimit](memory-management-registry-keys.md) registry key value.<br/> **Windows Home Server, Windows Server 2003 and Windows XP:** 860 MB with [LargeSystemCache](/previous-versions/windows/it-pro/windows-server-2003/cc784562(v=ws.10)) registry key set and without 4GT; up to 448 MB with 4GT. | Always 1 TB regardless of physical RAM **Windows 8.1 and Windows Server 2012 R2:** 16 TB.<br/> **Windows Server 2003 and Windows XP:** Up to 1 TB depending on configuration and RAM. |

## Physical Memory Limits: Windows 11

The following table specifies the limits on physical memory for Windows 11.

| Version                         | Limit on X64 | Limit on ARM64 |
|---------------------------------|--------------|----------------|
| Windows 11 Enterprise           | 6 TB         | 6 TB           |
| Windows 11 Education            | 2 TB         | 2 TB           |
| Windows 11 Pro for Workstations | 6 TB         | 6 TB           |
| Windows 11 Pro                  | 2 TB         | 2 TB           |
| Windows 11 Home                 | 128 GB       | 128 GB         |

## Physical Memory Limits: Windows 10

The following table specifies the limits on physical memory for Windows 10.

| Version                         | Limit on X86 | Limit on X64 |
|---------------------------------|--------------|--------------|
| Windows 10 Enterprise           | 4 GB         | 6 TB         |
| Windows 10 Education            | 4 GB         | 2 TB         |
| Windows 10 Pro for Workstations | 4 GB         | 6 TB         |
| Windows 10 Pro                  | 4 GB         | 2 TB         |
| Windows 10 Home                 | 4 GB         | 128 GB       |

## Physical Memory Limits: Windows Server 2016

The following table specifies the limits on physical memory for Windows Server 2016.

| Version                        | Limit on X64 |
|--------------------------------|--------------|
| Windows Server 2016 Datacenter | 24 TB        |
| Windows Server 2016 Standard   | 24 TB        |

## Physical Memory Limits: Windows 8

The following table specifies the limits on physical memory for Windows 8.

| Version                | Limit on X86 | Limit on X64 |
|------------------------|--------------|--------------|
| Windows 8 Enterprise   | 4 GB         | 512 GB       |
| Windows 8 Professional | 4 GB         | 512 GB       |
| Windows 8              | 4 GB         | 128 GB       |

## Physical Memory Limits: Windows Server 2012

The following table specifies the limits on physical memory for Windows Server 2012. Windows Server 2012 is available only in X64 editions.

| Version                               | Limit on X64 |
|---------------------------------------|--------------|
| Windows Server 2012 Datacenter        | 4 TB         |
| Windows Server 2012 Standard          | 4 TB         |
| Windows Server 2012 Essentials        | 64 GB        |
| Windows Server 2012 Foundation        | 32 GB        |
| Windows Storage Server 2012 Workgroup | 32 GB        |
| Windows Storage Server 2012 Standard  | 4 TB         |
| Hyper-V Server 2012                   | 4 TB         |

## Physical Memory Limits: Windows 7

The following table specifies the limits on physical memory for Windows 7.

| Version                | Limit on X86 | Limit on X64 |
|------------------------|--------------|--------------|
| Windows 7 Ultimate     | 4 GB         | 192 GB       |
| Windows 7 Enterprise   | 4 GB         | 192 GB       |
| Windows 7 Professional | 4 GB         | 192 GB       |
| Windows 7 Home Premium | 4 GB         | 16 GB        |
| Windows 7 Home Basic   | 4 GB         | 8 GB         |
| Windows 7 Starter      | 2 GB         | N/A          |

## Physical Memory Limits: Windows Server 2008 R2

The following table specifies the limits on physical memory for Windows Server 2008 R2. Windows Server 2008 R2 is available only in 64-bit editions.

| Version                                          | Limit on X64 | Limit on IA64 |
|--------------------------------------------------|--------------|---------------|
| Windows Server 2008 R2 Datacenter                | 2 TB         |               |
| Windows Server 2008 R2 Enterprise                | 2 TB         |               |
| Windows Server 2008 R2 for Itanium-Based Systems |              | 2 TB          |
| Windows Server 2008 R2 Foundation                | 8 GB         |               |
| Windows Server 2008 R2 Standard                  | 32 GB        |               |
| Windows HPC Server 2008 R2                       | 128 GB       |               |
| Windows Web Server 2008 R2                       | 32 GB        |               |

## Physical Memory Limits: Windows Server 2008

The following table specifies the limits on physical memory for Windows Server 2008. Limits greater than 4 GB for 32-bit Windows assume that [PAE](physical-address-extension.md) is enabled.

| Version                                       | Limit on X86 | Limit on X64 | Limit on IA64 |
|-----------------------------------------------|--------------|--------------|---------------|
| Windows Server 2008 Datacenter                | 64 GB        | 1 TB         |               |
| Windows Server 2008 Enterprise                | 64 GB        | 1 TB         |               |
| Windows Server 2008 HPC Edition               |              | 128 GB       |               |
| Windows Server 2008 Standard                  | 4 GB         | 32 GB        |               |
| Windows Server 2008 for Itanium-Based Systems |              |              | 2 TB          |
| Windows Small Business Server 2008            | 4 GB         | 32 GB        |               |
| Windows Web Server 2008                       | 4 GB         | 32 GB        |               |

## Physical Memory Limits: Windows Vista

The following table specifies the limits on physical memory for Windows Vista.

| Version                    | Limit on X86 | Limit on X64 |
|----------------------------|--------------|--------------|
| Windows Vista Ultimate     | 4 GB         | 128 GB       |
| Windows Vista Enterprise   | 4 GB         | 128 GB       |
| Windows Vista Business     | 4 GB         | 128 GB       |
| Windows Vista Home Premium | 4 GB         | 16 GB        |
| Windows Vista Home Basic   | 4 GB         | 8 GB         |
| Windows Vista Starter      | 1 GB         |              |

## Physical Memory Limits: Windows Home Server

Windows Home Server is available only in a 32-bit edition. The physical memory limit is 4 GB.

## Physical Memory Limits: Windows Server 2003 R2

The following table specifies the limits on physical memory for Windows Server 2003 R2. Limits over 4 GB for 32-bit Windows assume that [PAE](physical-address-extension.md) is enabled.

| Version                                   | Limit on X86                | Limit on X64 |
|-------------------------------------------|-----------------------------|--------------|
| Windows Server 2003 R2 Datacenter Edition | 64 GB<br/> (16 GB with 4GT) | 1 TB         |
| Windows Server 2003 R2 Enterprise Edition | 64 GB<br/> (16 GB with 4GT) | 1 TB         |
| Windows Server 2003 R2 Standard Edition   | 4 GB                        | 32 GB        |

## Physical Memory Limits: Windows Server 2003 with Service Pack 2 (SP2)

The following table specifies the limits on physical memory for Windows Server 2003 with Service Pack 2 (SP2). Limits over 4 GB for 32-bit Windows assume that [PAE](physical-address-extension.md) is enabled.

| Version                                                           | Limit on X86                | Limit on X64 | Limit on IA64 |
|-------------------------------------------------------------------|-----------------------------|--------------|---------------|
| Windows Server 2003 with Service Pack 2 (SP2), Datacenter Edition | 64 GB<br/> (16 GB with 4GT) | 1 TB         | 2 TB          |
| Windows Server 2003 with Service Pack 2 (SP2), Enterprise Edition | 64 GB<br/> (16 GB with 4GT) | 1 TB         | 2 TB          |
| Windows Server 2003 with Service Pack 2 (SP2), Standard Edition   | 4 GB                        | 32 GB        |               |

## Physical Memory Limits: Windows Server 2003 with Service Pack 1 (SP1)

The following table specifies the limits on physical memory for Windows Server 2003 with Service Pack 1 (SP1). Limits over 4 GB for 32-bit Windows assume that [PAE](physical-address-extension.md) is enabled.

| Version                                                           | Limit on X86                | Limit on X64 | Limit on IA64 |
|-------------------------------------------------------------------|-----------------------------|--------------|---------------|
| Windows Server 2003 with Service Pack 1 (SP1), Datacenter Edition | 64 GB<br/> (16 GB with 4GT) | 1 TB         | 1 TB          |
| Windows Server 2003 with Service Pack 1 (SP1), Enterprise Edition | 64 GB<br/> (16 GB with 4GT) | 1 TB         | 1 TB          |
| Windows Server 2003 with Service Pack 1 (SP1), Standard Edition   | 4 GB                        | 32 GB        |               |

## Physical Memory Limits: Windows Server 2003

The following table specifies the limits on physical memory for Windows Server 2003. Limits over 4 GB for 32-bit Windows assume that [PAE](physical-address-extension.md) is enabled.

| Version                                         | Limit on X86                | Limit on IA64 |
|-------------------------------------------------|-----------------------------|---------------|
| Windows Server 2003, Datacenter Edition         | 64 GB<br/> (16 GB with 4GT) | 512 GB        |
| Windows Server 2003, Enterprise Edition         | 64 GB<br/> (16 GB with 4GT) | 512 GB        |
| Windows Server 2003, Standard Edition           | 4 GB                        |               |
| Windows Server 2003, Web Edition                | 2 GB                        |               |
| Windows Small Business Server 2003              | 4 GB                        |               |
| Windows Compute Cluster Server 2003             |                             | 32 GB         |
| Windows Storage Server 2003, Enterprise Edition | 8 GB                        |               |
| Windows Storage Server 2003                     | 4 GB                        |               |

## Physical Memory Limits: Windows XP

The following table specifies the limits on physical memory for Windows XP.

| Version                    | Limit on X86 | Limit on X64 | Limit on IA64            |
|----------------------------|--------------|--------------|--------------------------|
| Windows XP                 | 4 GB         | 128 GB       | 128 GB (*not supported*) |
| Windows XP Starter Edition | 512 MB       | N/A          | N/A                      |

## Physical Memory Limits: Windows Embedded

The following table specifies the limits on physical memory for Windows Embedded.

| Version                        | Limit on X86 | Limit on X64 |
|--------------------------------|--------------|--------------|
| Windows XP Embedded            | 4 GB         |              |
| Windows Embedded Standard 2009 | 4 GB         |              |
| Windows Embedded Standard 7    | 4 GB         | 192 GB       |

## How graphics cards and other devices affect memory limits

Devices have to map their memory below 4 GB for compatibility with non-PAE-aware Windows releases. Therefore, if the system has 4GB of RAM, some of it is either disabled or is remapped above 4GB by the BIOS. If the memory is remapped, X64 Windows can use this memory. X86 client versions of Windows don’t support physical memory above the 4GB mark, so they can’t access these remapped regions. Any X64 Windows or X86 Server release can.

X86 client versions with PAE enabled do have a usable 37-bit (128 GB) physical address space. The limit that these versions impose is the highest permitted physical RAM address, not the size of the IO space. That means PAE-aware drivers can actually use physical space above 4 GB if they want. For example, drivers could map the "lost" memory regions located above 4 GB and expose this memory as a RAM disk.

## Related content

[4-Gigabyte Tuning](4-gigabyte-tuning.md)

[**IMAGE\_FILE\_LARGE\_ADDRESS\_AWARE**](/windows/win32/api/dbghelp/ns-dbghelp-loaded_image)

[Physical Address Extension](physical-address-extension.md)

[Comparison of locks and limits in Windows Server](/windows-server/get-started/locks-limits)
