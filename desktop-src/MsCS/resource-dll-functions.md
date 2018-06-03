---
title: Resource DLL Functions
description: The Resource DLL functions allow the Cluster service to manage resources indirectly through a Resource Monitor and a resource DLL.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7644a51b-a19f-4ea1-af68-baf3937b60e0
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource DLL functions Failover Cluster
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resource DLL Functions

The Resource DLL functions allow the [Cluster service](cluster-service.md) to manage [resources](resources.md) indirectly through a [Resource Monitor](resource-monitor.md) and a [resource DLL](resource-dlls.md). These function are only used by resource DLLs, except for the cluster database access functions, which should be avoided by [cluster-aware](cluster-aware-applications.md) application whenever possible.

For more information about how to create resource DLLs, see [Creating Resource Types](creating-resource-types.md).

## In this section

<dl> <dt>

[Resource DLL Entry-Point Functions](resource-dll-entry-point-functions.md)
</dt> <dd>

The resource DLL entry point functions are used by the [Cluster service](cluster-service.md) to indirectly initiate operations on cluster [resources](resources.md). These functions are implemented in resource DLLs.

</dd> <dt>

[Resource DLL Callback Functions](resource-dll-callback-functions.md)
</dt> <dd>

The resource DLL callback functions allow a [resource DLL](resource-dlls.md) to report status and event information to a [Resource Monitor](resource-monitor.md), which then provides the information to the [Cluster service](cluster-service.md).

</dd> <dt>

[Cluster Database Access Functions](cluster-database-access-functions.md)
</dt> <dd>

The [cluster database](cluster-database.md) access functions are called by [Resource DLLs](resource-dlls.md) to create and initialize private properties and perform other configuration tasks.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Functions](failover-cluster-functions.md)
</dt> <dt>

[Failover Cluster Utility Functions](cluster-utility-functions.md)
</dt> <dt>

[Creating Resource Types](creating-resource-types.md)
</dt> </dl>

 

 




