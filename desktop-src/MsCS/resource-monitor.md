---
title: Resource Monitor
description: A Resource Monitor provides a communication, monitoring, and processing layer between the Cluster service and one or more resources.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: caebb47f-c2c5-463e-a957-d9eefc7fc33d
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource monitors Failover Cluster
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resource Monitor

A Resource Monitor provides a communication, monitoring, and processing layer between the [Cluster service](cluster-service.md) and one or more [resources](resources.md). Resource Monitors have the following characteristics:

-   A Resource Monitor always runs in a process separate from the Cluster service. If a resource fails, the Resource Monitor isolates the Cluster service from the effects. If the Cluster service fails, the Resource Monitor allows its resources to shut down gracefully.
-   To work with a resource, a Resource Monitor loads the [resource DLL](resource-dlls.md) responsible for that resource type into its process.
-   When the Cluster service requests an operation on a resource, the Resource Monitor routes the request to the appropriate [entry point function](resource-dll-entry-point-functions.md) of the resource DLL responsible for the resource. The Resource Monitor performs default processing for some resource operations.
-   A Resource Monitor stores synchronized state data, allowing the Cluster service and resource DLLs to operate asynchronously, checking and updating resource status as needed.
-   A Resource Monitor periodically checks the operational status of all of its resources. For more information on this process, see [Resource Failure](resource-failure.md).

By default, the Cluster service creates one Resource Monitor per node. This default can be overridden when a resource is created by requesting a separate monitor. Separate monitors are recommended for unstable resources and for debugging new resource types. For information about debugging new resource types, see [Debugging Resource DLLs](debugging-resource-dlls.md).

## Related topics

<dl> <dt>

[Failover Cluster Software Components](server-cluster-software-components.md)
</dt> </dl>

 

 




