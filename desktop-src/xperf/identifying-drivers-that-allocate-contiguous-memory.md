---
title: Identifying Drivers That Allocate Contiguous Memory
description: Identifying Drivers That Allocate Contiguous Memory
ms.assetid: e5abed86-db9c-45a2-8ac8-3906868087d1
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Identifying Drivers That Allocate Contiguous Memory

### Target Platforms

X86 Windows Server 2003 Service Pack 2

X64 Windows Server 2003 Service Pack 2

X64 Windows Server 2008 Service Pack 1

X64 Windows Server 2008 Service Pack 2

X64 Windows Server 2008 R2

When monitoring the working set size of a process, you may find that the working set size of the process decreases. This information may indicate that the memory manager is trimming all processes on the computer to satisfy a large memory allocation request. Working set trimming is the action Windows memory manager takes to satisfy physical memory demand under low resource conditions. Working set trimming can have severe performance consequences under Windows 2003 and the consumers of physical memory responsible are variable and often difficult to identify. For a more thorough discussion of this behavior please see [Knowledge Base article 956341](http://go.microsoft.com/fwlink/p/?linkid=3100&amp;ID=956341).

In releases greater than or equal to Vista SP1 and Windows Server 2008 SP1contiguous memory logic is changed such that working set trimming is much more rare than in previous releases. Also, in these newer releases, if the memory manager trims working sets, the working sets will not be emptied; only shared pages will be trimmed. For processes whose working sets comprise mostly of private pages, the overall WS size may not dramatically change as it would before.

This document explains how to identify Working Set Trimming events. In this example, a driver allocating too much contiguous memory causes a Working Set Trimming event.

> [!Note]  
> The ETW event will only be logged by the memory manager when the working sets are going to be emptied, not when a process allocates contiguous memory.

 

This section includes the following topics:

<dl>

[Preparing the Environment](preparing-the-environment.md)  
[Collecting Contiguous Memory Allocation Data](collecting-contiguous-memory-allocation-data.md)  
[Evaluating Contiguous Memory Allocation Data](evaluating-contiguous-memory-allocation-data.md)  
</dl>

 

 




