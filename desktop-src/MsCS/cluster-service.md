---
title: Cluster Service
description: The Cluster service is a system component used to control failover clusters activities on a single node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '90717d6e-f2a4-49a0-86b6-17de1c4bcfe4'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Cluster service Failover Cluster"]
---

# Cluster Service

The Cluster service is a system component used to control [*failover clusters*](f-gly.md#mscs-failover-cluster-gly) activities on a single [node](nodes.md). It is fundamental to the operation of the [*cluster*](c-gly.md#-wolf-cluster-gly). There is one instance of the Cluster service running on every node in a cluster. The Cluster service instances work together to perform the following failover cluster operations:

-   Monitor and control [cluster objects](cluster-objects.md) and [cluster properties](cluster-object-properties.md).
-   Handle event notification.
-   Facilitate communication among other software components.
-   Perform [*failover*](f-gly.md#-wolf-failover-gly) and failback operations.
-   Maintain a consistent image of the cluster across all nodes.

The Cluster service is so fundamental to a node's participation in a failover cluster that the term is often used to describe the activities of the cluster as a whole—for example, "The Cluster service performs failover." Such terminology is not necessarily wrong but it can be misleading. Keep in mind that a single instance of the Cluster service is specific to a single node and therefore cluster-wide operations depend on all instances of the Cluster service communicating and working together.

 

 




