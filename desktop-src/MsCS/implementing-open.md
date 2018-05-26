---
title: Implementing Open
description: The Cluster service calls the Open entry point function (through a Resource Monitor) to create a new instance of a resource type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ba8733dc-ec22-4e21-ab21-a7cbf89273e4
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- entry point functions Failover Cluster ,implementing Open
- Open Failover Cluster ,implementing
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Implementing Open

The [Cluster service](cluster-service.md) calls the [**Open**](/windows/previous-versions/ResApi/nc-resapi-popen_routine?branch=master) entry point function (through a [Resource Monitor](resource-monitor.md)) to create a new instance of a [resource type](resource-types.md). Your [resource DLL](resource-dlls.md) should initialize an actual instance of the physical or logical entity to be supported as the [resource](resources.md) and associate it with a set of instance data. **Open** can also lay groundwork for the [**Online**](/windows/previous-versions/ResApi/nc-resapi-ponline_routine?branch=master) entry point.

**To implement Open**

1.  Optional: Enforce limits on the number of concurrent instances allowed. It is recommended that you use a synchronization object such as a semaphore to synchronize instance counts.
2.  Required: Generate and save the required [instance data](instance-data.md) for the new instance. See [Implementing Instance Management](implementing-instance-management.md).
3.  Required: Create or initialize an actual instance of the physical or logical entity to be supported as a resource. Make sure it is in an offline state.
4.  Optional: Perform configuration tasks such as establishing registry and crypto key checkpoints. See [Checkpointing](checkpointing.md).
5.  Recommended: For optimal performance, return a value within 300 milliseconds.

## Example

See [Resource DLL Examples](https://msdn.microsoft.com/library/aa370474).

 

 




