---
description: System virtual address (VA) space on 32-bit systems can become exhausted due to fragmentation. Several registry keys can be used to configure memory limits on 32-bit systems that experience this issue.
ms.assetid: ec2a8c6b-cd8e-4085-b337-02f78a210bb5
title: Memory Management Registry Keys
ms.topic: article
ms.date: 05/31/2018
---

# Memory Management Registry Keys

System virtual address (VA) space on 32-bit systems can become exhausted due to fragmentation. Several registry keys can be used to configure memory limits on 32-bit systems that experience this issue. System VA space on 64-bit systems is not subject to exhaustion by fragmentation; therefore, these keys have no effect on 64-bit systems.

For 32-bit systems, these memory management registry keys must be explicitly created under the following registry key:

**HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**Current Control Set**\\**Control**\\**Session Manager**\\**Memory Management**

**Windows Server 2008 and Windows Vista:** These registry keys are available on 32-bit systems starting with Windows Server 2008 and Windows Vista with Service Pack 1 (SP1).

For default memory and address space limits on both 32-bit and 64-bit systems, see [Memory Limits for Windows Releases](memory-limits-for-windows-releases.md).

The following table describes the memory management registry keys that can be used to configure memory limits on 32-bit systems. All of these keys have a REG\_DWORD type and possible values that range from 0 through 2,048 MB. The default is 0, which means no limit is enforced. Values are automatically rounded up to the next system VA allocation boundary, which is 2 MB on 32-bit systems that have [Physical Address Extension](physical-address-extension.md) (PAE) enabled and 4 MB on 32-bit systems that do not have PAE enabled.



| Key                   | Description                                                                                                                                                    |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **NonPagedPoolLimit** | Specifies the maximum amount of system VA space that can be used by the nonpaged pool. Under certain conditions, this limit may be exceeded by a small amount. |
| **PagedPoolLimit**    | Specifies the maximum amount of system VA space that can be used by the paged pool.                                                                            |
| **SessionSpaceLimit** | Specifies the maximum amount of system VA space that can be used by session space allocations.                                                                 |
| **SystemCacheLimit**  | Specifies the maximum amount of system VA space that can be used by the system cache. Under certain conditions, this limit may be exceeded by a small amount.  |
| **SystemPtesLimit**   | Specifies the maximum amount of system VA space that can be used by I/O mappings and other resources that consume system page table entries (PTEs).            |



 

Determining whether system VA space is being exhausted requires the use of a kernel debugger. For more information, see [Debugging Tools for Windows](https://msdn.microsoft.com/library/cc267445.aspx).

 

 



