---
title: Resources
description: List of characteristics of a Failover Cluster resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 090d1c20-fab3-43dd-bfe2-a2c3f9ba8f89
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- cluster objects Failover Cluster ,resources
- resources Failover Cluster
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resources

A [*cluster*](https://www.bing.com/search?q=*cluster*) resource is any physical or logical component that has the following characteristics.

-   It can be brought [*online*](https://www.bing.com/search?q=*online*) and taken [*offline*](https://www.bing.com/search?q=*offline*).
-   It can be managed in a cluster.
-   It can be hosted (owned) by only one [node](nodes.md) at a time.

To manage resources, the [Cluster service](cluster-service.md) communicates to a [resource DLL](resource-dlls.md) through a [Resource Monitor](resource-monitor.md). In response to a Cluster service request, the Resource Monitor calls the appropriate [entry-point function](resource-dll-entry-point-functions.md) in the resource DLL to check and control the resource's state.

A resource can specify one or more resources on which it is dependent. A dependent resource is one that requires another resource to operate. For example, a network name won't work by itself; it must be associated with an IP address. Because of this requirement, a [Network Name](network-name.md) resource is dependent on an [IP Address](ip-address.md) resource. Dependent resources are taken offline before the resources upon which they depend are taken offline, and they are brought online after these resources are brought online.

A resource can also specify a list of [nodes](nodes.md) on which it is able to run. Preferred nodes and dependencies are important considerations when administrators organize resources into [groups](groups.md).

> \[!Important\]  
> In Windows Server 2012, a resource can be placed in locked mode, which is maintained in the volatile cluster state.

 

The following topics describe important concepts related to resources:



| Resource concepts                                  | Description                                                                                                                                           |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Quorum Resource](quorum-resource.md)             | Describes the fundamental role it plays in defining the cluster.                                                                                      |
| [Resource Failure](resource-failure.md)           | Describes how the Cluster service determines when a resource has failed, as well as ways for developers and administrators to adjust that process.    |
| [Resource Dependencies](resource-dependencies.md) | Provides information on the effects of dependency relationships between resources, and lists the required dependencies of the default resource types. |



 

For more information on working with resources, see the following topics.

-   [Resource Common Properties](resource-common-properties.md)
-   [Resource Control Codes](resource-control-codes.md)
-   [Resource Management Functions](resource-management-functions.md)
-   [Resource DLL Entry Point Functions](resource-dll-entry-point-functions.md)
-   [Resource DLL Callback Functions](resource-dll-callback-functions.md)

 

 




