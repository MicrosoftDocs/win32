---
title: High Availability
description: Failover clusters are designed to keep resources (such as applications, disks, and file shares) highly available.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'daec0128-5ae1-4eea-ad6a-77b633523dd6'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["high availability Failover Cluster"]
---

# High Availability

[*Failover clusters*](f-gly.md#mscs-failover-cluster-gly) are designed to keep resources (such as applications, disks, and file shares) highly available. "Availability" is a measure of the ability of clients to connect with and use a resource at any point in time. If a resource is not available, clients cannot use it.

One way to understand high availability is to contrast it with fault tolerance. These terms describe two different benchmarks measuring availability. Fault tolerance is defined as 100% availability 100% of the time, regardless of the circumstances. A fault tolerant system is designed to guarantee resource availability.

In contrast, a high-availability system is concerned with maximizing resource availability. A highly available resource is available a very high percentage of the time and may even approach 100% availability, but a small percentage of down time is acceptable and expected.

High availability can be defined as follows:

A highly available resource is almost always operational and accessible to clients.

For information on how a failover cluster implements a high-availability environment, see [Failover Cluster Implementation](server-cluster-implementation.md).

For information on how you can create high availability resources, see [Creating Resource Types](creating-resource-types.md).

 

 




