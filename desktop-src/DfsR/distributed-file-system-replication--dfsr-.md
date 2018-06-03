---
title: Distributed File System Replication
description: Supports replication scheduling and bandwidth throttling.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fd9a3d78-7103-425c-a314-694dd1d8da40
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Distributed File System Replication Distributed File System Replication
- Distributed File System Replication Distributed File System Replication , home page
- DFSR Files See Distributed File System Replication
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Distributed File System Replication

The Distributed File System Replication (DFSR) service is a state-based, multimaster replication engine that supports replication scheduling and bandwidth throttling. DFSR uses a compression algorithm known as remote differential compression (RDC). RDC is a "diff-over-the wire" client/server protocol that can be used to efficiently update files over a limited-bandwidth network. RDC detects insertions, removals, and rearrangements of data in files, enabling DFSR to replicate only the changed file blocks when files are updated. For more information about DFSR, see [Introduction to DFS Replication](http://go.microsoft.com/fwlink/p/?linkid=104129).

You can use the DFSR WMI provider to create tools for configuring and monitoring the DFSR service.

For more information, see the following topics:

-   [About DFSR](about-dfsr.md)
-   [Using DFSR](using-the-dfsr-wmi-provider.md)
-   [DFSR WMI Classes](dfsr-wmi-classes.md)
-   [DFSR Glossary](dfsr-glossary.md)

## Run-Time Requirements

DFSR is supported on Windows server operating systems. It is supported on Windows Vista, but it is not supported on any other Windows client operating systems.

For information about run-time requirements for a particular programming element, see the Requirements section of the documentation for that element.

## Related topics

<dl> <dt>

[DFS Technical Reference](Http://go.microsoft.com/fwlink/p/?linkid=84117)
</dt> <dt>

[FRS Technical Reference](Http://go.microsoft.com/fwlink/p/?linkid=84118)
</dt> </dl>

 

 




