---
title: Failover Cluster Functions
description: This section contains the functions of the Failover Cluster API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 28D8979D-4719-4730-8F94-F980D28C5FE4
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Failover Cluster Functions

This section contains the functions of the Failover Cluster API.

## In this section

<dl> <dt>

[Control Code Functions](control-code-functions.md)
</dt> <dd>

Control code functions use [control codes](control-codes.md) as parameters in order to perform cluster operations.

</dd> <dt>

[Resource DLL Functions](resource-dll-functions.md)
</dt> <dd>

The Resource DLL functions allow the [Cluster service](cluster-service.md) to manage [resources](resources.md) indirectly through a [Resource Monitor](resource-monitor.md) and a [resource DLL](resource-dlls.md). These function are only used by resource DLLs, except for the cluster database access functions, which should be avoided by [cluster-aware](cluster-aware-applications.md) application whenever possible.

</dd> <dt>

[Failover Cluster Object Management Functions](cluster-object-management-functions.md)
</dt> <dd>

The failover cluster object management functions manage failover cluster objects through the [Cluster service](cluster-service.md). These functions are primarily used by [cluster-aware](cluster-aware-applications.md) applications, and should be avoided by resource DLLs whenever possible.

</dd> <dt>

[Failover Cluster Utility Functions](cluster-utility-functions.md)
</dt> <dd>

The failover cluster utility functions support a wide range of functionality, from general purpose helper functions to thread and service management functions. Both [cluster-aware applications](https://www.bing.com/search?q=cluster-aware applications) and [resource DLLs](resource-dlls.md) can use the failover cluster utility functions. However, some utility functions are intended only for use by resource DLLs. Cluster-aware applications should follow the topic [standard order of preference](standard-order-of-preference.md) before using utility functions intended for resource DLLs.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Reference](failover-cluster-reference.md)
</dt> </dl>

 

 




