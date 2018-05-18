---
title: Failover Cluster Implementation
description: A failover cluster consists of two or more independent Microsoft Windows server systems. The computer systems that make up the collection are known as nodes. Nodes have the following characteristics.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '052c0dcc-4157-430e-a42c-6c7ebae70c85'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["failover clusters Failover Cluster ,implementation", "implementation of failover clusters Failover Cluster"]
---

# Failover Cluster Implementation

A [*failover cluster*](f-gly.md#mscs-failover-cluster-gly) consists of two or more independent Microsoft Windows server systems. The computer systems that make up the collection are known as [nodes](nodes.md). Nodes have the following characteristics.

-   Every node has access to all cluster configuration data.
-   Every node communicates with the other nodes in the [*cluster*](c-gly.md#-wolf-cluster-gly) through one or more physically independent [networks](networks.md) (sometimes referred to as interconnects). Network adapters, referred to in failover clusters as [network interfaces](network-interfaces.md), attach nodes to networks.
-   Every node in the cluster is aware when another system joins or leaves the cluster.
-   Every node in the cluster is aware of the resources that are running locally as well as the resources that are running on the other cluster nodes.
-   All nodes in the cluster are grouped under a common name, the cluster name, which is used for accessing and managing the cluster.

When a node starts, it searches for active nodes on the networks designated for internal communication. If it finds an [*active*](a-gly.md#-wolf-active-gly) node, it attempts to join the node's cluster. If it cannot find an existing cluster, it attempts to form a cluster by taking control of the [quorum resource](quorum-resource.md). The quorum resource stores the most current version of the [cluster database](cluster-database.md), which contains cluster configuration and state data. A failover cluster maintains a consistent, updated copy of the cluster database on all active nodes.

A node can host physical or logical units, referred to as [*resources*](r-gly.md#-wolf-resource-gly). Administrators organize these cluster resources into functional units called [groups](groups.md) and assign these groups to individual nodes. If a node fails, the failover cluster transfers the groups that were being hosted by the node to other nodes in the cluster. This transfer process is called [*failover*](f-gly.md#-wolf-failover-gly). The reverse process, [*failback*](f-gly.md#-wolf-failback-gly), occurs when the failed node becomes active again and the groups that were failed over to other nodes are transferred back to the original node.

Nodes, resources, and groups are three kinds of [*cluster objects*](c-gly.md#-wolf-cluster-object-gly). The others are [networks](networks.md), [network interfaces](network-interfaces.md), and [resource types](resource-types.md). All cluster objects are associated with a set of [properties](cluster-object-properties.md), which are data values that describe an object's identity and behavior in the cluster. Administrators manage cluster objects by manipulating their properties, typically through a [*cluster management application*](c-gly.md#-wolf-cluster-management-application-gly) such as [Cluster Administrator](cluster-administrator.md).

Developers use the [Failover Cluster API](the-server-cluster-api.md) to create [*cluster-aware applications*](c-gly.md#-wolf-cluster-aware-application-gly), cluster management applications, and [*custom resource types*](c-gly.md#-wolf-custom-resource-type-gly).

 

 




