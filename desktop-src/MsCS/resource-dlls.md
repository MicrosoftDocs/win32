---
title: Resource DLLs
description: Resource DLLs are responsible for carrying out most operations on cluster resources.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e1434102-afaf-4a35-887e-a434c628bd90
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource DLLs Failover Cluster
- resource DLLs Failover Cluster ,described
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resource DLLs

Resource DLLs are responsible for carrying out most operations on cluster resources. A resource DLL is characterized as follows:

-   It contains the resource-specific code necessary to provide [high availability](high-availability.md) for instances of one or more resource types.
-   It exposes this code through a standard interface consisting of a set of [entry point functions](resource-dll-entry-point-functions.md).
-   It is registered with the [Cluster service](cluster-service.md) to associate one or more [resource type](resource-types.md) names with the name of the DLL.
-   It is always loaded into a Resource Monitor's process when in use.

When the Cluster service needs to perform an operation on a [resource](resources.md), it sends the request to the Resource Monitor assigned to the resource. If the Resource Monitor does not have a DLL in its process that can handle that type of resource, it uses the registration information to load the DLL associated with the resource type. It then passes the Cluster service's request to one of the DLL's entry point functions. The resource DLL handles the details of the operation so as to meet the specific needs of the resource.

This architecture separates the Cluster service from the implementation details of specific resource types, allowing the Cluster service to manage [file shares](file-share.md), [physical disks](physical-disk.md), [IP addresses](ip-address.md), and all other types of resources through a standard interface. It also allows for the creation of new resource types.

You can define your own resource types to provide customized support for cluster-unaware applications, enhanced support for cluster-aware applications, or specialized support for new kinds of devices. For more information, see [Creating Resource Types](creating-resource-types.md).

 

 




