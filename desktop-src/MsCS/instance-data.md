---
title: Instance Data
description: Your resource DLL must maintain a set of data for each instance that identifies and describes the instance and its current configuration, and that associates the instance with handles and other objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0580ec99-2bb7-440b-9a5b-a73430b5b0f1
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource DLLs Failover Cluster ,instance data
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Instance Data

Your [resource DLL](resource-dlls.md) must maintain a set of data for each instance that identifies and describes the instance and its current configuration, and that associates the instance with handles and other objects. At minimum, your resource DLL must maintain the following data items for each instance:

1.  [Resource identifier](resource-identifiers.md).
2.  [Resource](resources.md) name.
3.  The [Resource Monitor's](resource-monitor.md) handle to the instance, which is used to identify the instance in the [**LogEvent**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-plog_event_routine) and [**SetResourceStatus**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pset_resource_status_routine) callback functions.
4.  The cluster database subkey defined for the resource.
5.  The current state of the resource.

A [resource structure](resource-structures.md) should be created to meet these requirements. It is recommended that you maintain a similar set of data for each instance.

For more information on instance management, see [Implementing Instance Management](implementing-instance-management.md).

## Related topics

<dl> <dt>

[Managing Instances](managing-instances.md)
</dt> </dl>

 

 




