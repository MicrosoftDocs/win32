---
title: Cluster Objects
description: Cluster objects are the physical and logical units managed by failover clusters.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 609cc002-2db9-4ec6-a802-8f7bdbb11b90
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- cluster objects Failover Cluster
- objects in failover clusters Failover Cluster
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Cluster Objects

Cluster objects are the physical and logical units managed by [*failover clusters*](https://www.bing.com/search?q=*failover clusters*). Each object is associated with:

-   One or more [properties](cluster-object-properties.md), or attributes, that define the object and its behavior within the [*cluster*](https://www.bing.com/search?q=*cluster*).
-   A set of [control codes](control-codes.md) used to manipulate the object's properties.
-   A set of [object management functions](cluster-object-management-functions.md) used to manage the object through the [Cluster service](cluster-service.md).

The following table summarizes the cluster objects.



| Cluster object                              | Description                                                                                                                   |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [Group](groups.md)                         | A collection of resources that run together on a node and are [*failed over*](https://www.bing.com/search?q=*failed over*) as a single unit. |
| [Network](networks.md)                     | A network across which a cluster node can communicate.                                                                        |
| [Network Interface](network-interfaces.md) | A network adapter that is installed in a cluster node.                                                                        |
| [Node](nodes.md)                           | A computer system that is a member of a cluster.                                                                              |
| [Resource](resources.md)                   | An entity that is hosted by a node, managed by the Cluster service, and can be started, stopped, and moved to another node.   |
| [Resource Type](resource-types.md)         | A category of resources, such as [Physical Disks](physical-disk.md).                                                         |



 

 

 




