---
title: Cluster Service
description: The Cluster service is a system component used to control failover clusters activities on a single node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 90717d6e-f2a4-49a0-86b6-17de1c4bcfe4
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Cluster service Failover Cluster
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Cluster Service

The Cluster service is a system component used to control [*failover clusters*](https://www.bing.com/search?q=*failover clusters*) activities on a single [node](nodes.md). It is fundamental to the operation of the [*cluster*](https://www.bing.com/search?q=*cluster*). There is one instance of the Cluster service running on every node in a cluster. The Cluster service instances work together to perform the following failover cluster operations:

-   Monitor and control [cluster objects](cluster-objects.md) and [cluster properties](cluster-object-properties.md).
-   Handle event notification.
-   Facilitate communication among other software components.
-   Perform [*failover*](https://www.bing.com/search?q=*failover*) and failback operations.
-   Maintain a consistent image of the cluster across all nodes.

The Cluster service is so fundamental to a node's participation in a failover cluster that the term is often used to describe the activities of the cluster as a whole—for example, "The Cluster service performs failover." Such terminology is not necessarily wrong but it can be misleading. Keep in mind that a single instance of the Cluster service is specific to a single node and therefore cluster-wide operations depend on all instances of the Cluster service communicating and working together.

 

 




