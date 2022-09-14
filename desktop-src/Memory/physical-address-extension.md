---
description: Physical Address Extension (PAE) is a processor feature that enables x86 processors to access more than 4 GB of physical memory on capable versions of Windows.
ms.assetid: 1aec2414-cc93-4a86-955d-2433360c9125
title: Physical Address Extension
ms.topic: article
ms.date: 05/31/2018
---

# Physical Address Extension

Physical Address Extension (PAE) is a processor feature that enables x86 processors to access more than 4 GB of physical memory on capable versions of Windows. Certain 32-bit versions of Windows Server running on x86-based systems can use PAE to access up to 64 GB or 128 GB of physical memory, depending on the physical address size of the processor. For details, see [Memory Limits for Windows Releases](memory-limits-for-windows-releases.md).

The Intel Itanium and x64 processor architectures can access more than 4 GB of physical memory natively and therefore do not provide the equivalent of PAE. PAE is used only by 32-bit versions of Windows running on x86-based systems.

With PAE, the operating system moves from two-level linear address translation to three-level address translation. Instead of a linear address being split into three separate fields for indexing into memory tables, it is split into four separate fields: a 2-bit bitfield, two 9-bit bitfields, and a 12-bit bitfield that corresponds to the page size implemented by Intel architecture (4 KB). The size of page table entries (PTEs) and page directory entries (PDEs) in PAE mode is increased from 32 to 64 bits. The additional bits allow an operating system PTE or PDE to reference physical memory above 4 GB.

In 32-bit Windows running on x64-based systems, PAE also enables several advanced system and processor features, including hardware-enabled [Data Execution Prevention](data-execution-prevention.md) (DEP), [non-uniform memory access (NUMA)](../procthread/numa-support.md), and the ability to add memory to a system while it is running (hot-add memory).

PAE does not change the amount of virtual address space available to a process. Each process running in 32-bit Windows is still limited to a 4 GB virtual address space.

## System Support for PAE

PAE is supported only on the following 32-bit versions of Windows running on x86-based systems:

-   Windows 7 (32 bit only)
-   Windows Server 2008 (32-bit only)
-   Windows Vista (32-bit only)
-   Windows Server 2003 (32-bit only)
-   Windows XP (32-bit only)

## Enabling PAE

Windows automatically enables PAE if DEP is enabled on a computer that supports hardware-enabled DEP, or if the computer is configured for hot-add memory devices in memory ranges beyond 4 GB. If the computer does not support hardware-enabled DEP or is not configured for hot-add memory devices in memory ranges beyond 4 GB, PAE must be explicitly enabled.

To explicitly enable PAE, use the following [**BCDEdit /set**](/windows-hardware/drivers/devtest/bcdedit--set) command to set the **pae** boot entry option:

 **bcdedit /set \[{ID}\] pae ForceEnable**  


IF DEP is enabled, PAE cannot be disabled. Use the following [**BCDEdit /set**](/windows-hardware/drivers/devtest/bcdedit--set) commands to disable both DEP and PAE:

 **bcdedit /set \[{ID}\] nx AlwaysOff**  
**bcdedit /set \[{ID}\] pae ForceDisable**  


**Windows Server 2003 and Windows XP:** To enable PAE, use the **/PAE** switch in the [boot.ini](/windows-hardware/drivers/devtest/overview-of-the-boot-ini-file) file. To disable PAE, use the **/NOPAE** switch. To disable DEP, use the **/EXECUTE** switch.

## Comparing PAE and other Large Memory Support

PAE, [4-gigabyte tuning](4-gigabyte-tuning.md) (4GT), and [Address Windowing Extensions](address-windowing-extensions.md) (AWE) serve different purposes and can be used independently of each other:

-   PAE allows the operating system to access and use more than 4 GB of physical memory.
-   4GT increases the portion of the virtual address space that is available to a process from 2 GB to up to 3 GB.
-   AWE is a set of APIs that allows a process to allocate nonpaged physical memory and then dynamically map portions of this memory into the virtual address space of the process.

When neither 4GT nor AWE are being used, the amount of physical memory that a single 32-bit process can use is limited by the size of its address space (2 GB). In this case, a PAE-enabled system can still make use of more than 4 GB of RAM to run multiple processes at the same time or to cache file data in memory.

4GT can be used with or without PAE. However, some versions of Windows limit the maximum amount of physical memory that can be supported when 4GT is used. On such systems, booting with 4GT enabled causes the operating system to ignore any memory in excess of the limit.

AWE does not require PAE or 4GT but is often used together with PAE to allocate more than 4 GB of physical memory from a single 32-bit process.

## Related topics



[**IsProcessorFeaturePresent**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-isprocessorfeaturepresent)
</dt> <dt>

[PAE X86 Technical Reference](/previous-versions/windows/it-pro/windows-server-2003/cc728455(v=ws.10))
</dt> </dl>

 

 
