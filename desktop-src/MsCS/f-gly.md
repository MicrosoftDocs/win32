---
title: F
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Robots: noindex, nofollow
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9cca18f0-cf81-4e4d-9b87-da1484ddd9d8
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# F

[A](a-gly.md) B [C](c-gly.md) [D](d-gly.md) [E](e-gly.md) F [G](g-gly.md) [H](h-gly.md) [I](i-gly.md) J K [L](l-gly.md) [M](m-gly.md) [N](n-gly.md) [O](o-gly.md) [P](p-gly.md) [Q](q-gly.md) [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) U [V](v-gly.md) [W](w-gly.md) X Y Z

<dl> <dt>

<span id="_wolf_failback_gly"></span><span id="_WOLF_FAILBACK_GLY"></span>**failback**
</dt> <dd>

Process of moving a [*group*](g-gly.md#-wolf-group-gly) back to its preferred [*node*](n-gly.md#-wolf-node-gly) when the node becomes [*active*](a-gly.md#-wolf-active-gly) after a failure.

</dd> <dt>

<span id="_wolf_failed_gly"></span><span id="_WOLF_FAILED_GLY"></span>**failed**
</dt> <dd>

Describes a [*node*](n-gly.md#-wolf-node-gly) or [*resource*](r-gly.md#-wolf-resource-gly) that has ceased operating and is unavailable to the [*cluster*](c-gly.md#-wolf-cluster-gly). Node or resource failure can trigger [*failover*](#-wolf-failover-gly).

</dd> <dt>

<span id="_wolf_failover_gly"></span><span id="_WOLF_FAILOVER_GLY"></span>**failover**
</dt> <dd>

Process of moving a [*group*](g-gly.md#-wolf-group-gly) to another [*node*](n-gly.md#-wolf-node-gly) in response to a node or [*resource*](r-gly.md#-wolf-resource-gly) failure.

</dd> <dt>

<span id="mscs.failover_cluster_gly"></span><span id="MSCS.FAILOVER_CLUSTER_GLY"></span>**failover cluster**
</dt> <dd>

The type of [*cluster*](c-gly.md#-wolf-cluster-gly) that the [*Cluster service*](c-gly.md#-wolf-cluster-service-gly) implements. Failover clusters are characterized by high availability. The failover cluster is one of two types of clusters provided by Microsoft [*Windows Clustering*](w-gly.md#-wolf-windows-clustering-gly). This was previously known as a [*server cluster*](s-gly.md#-wolf-server-cluster-gly).

</dd> <dt>

<span id="mscs.failover_cluster_api_gly"></span><span id="MSCS.FAILOVER_CLUSTER_API_GLY"></span>**Failover Cluster API**
</dt> <dd>

Collection of functions that are implemented by the [*Cluster service*](c-gly.md#-wolf-cluster-service-gly) and used by [*cluster-aware applications*](c-gly.md#-wolf-cluster-aware-application-gly), [*cluster management applications*](c-gly.md#-wolf-cluster-management-application-gly), and [*resource DLLs*](r-gly.md#-wolf-resource-dll-gly). The Failover Cluster API includes functions for managing [*cluster objects*](c-gly.md#-wolf-cluster-object-gly) and the [*cluster database*](c-gly.md#-wolf-cluster-database-gly). This was previously known as the [*Server Cluster API*](s-gly.md#-wolf-server-cluster-api-gly).

</dd> <dt>

<span id="mscs.failover_cluster_instance_gly"></span><span id="MSCS.FAILOVER_CLUSTER_INSTANCE_GLY"></span>**failover cluster instance**
</dt> <dd>

A [*group*](g-gly.md#-wolf-group-gly) containing an [*IP Address resource*](i-gly.md#-wolf-ip-address-resource-gly), an [*IPv6 Address resource*](i-gly.md#mscs-ipv6-address-resource-gly), and/or an [*IPv6 Tunnel Address resource*](i-gly.md#mscs-ipv6-tunnel-address-resource-gly) and a [*Network Name resource*](n-gly.md#-wolf-network-name-resource-gly), and additional resources necessary to run one or more applications or services. Clients can use the network name to access the resources in the group, analogous to using a computer name to access the services on a physical server. However, because a failover cluster instance is a group, it can be failed over to another [*node*](n-gly.md#-wolf-node-gly) without affecting the underlying name or address. This was previously known as a [*virtual server*](v-gly.md#-wolf-virtual-server-gly).

</dd> <dt>

<span id="_wolf_failover_manager_gly"></span><span id="_WOLF_FAILOVER_MANAGER_GLY"></span>**Failover Manager**
</dt> <dd>

Software component in the [*Cluster service*](c-gly.md#-wolf-cluster-service-gly) that works with the [*Resource Manager*](r-gly.md#-wolf-resource-manager-gly) to manage [*resources*](r-gly.md#-wolf-resource-gly) and [*groups*](g-gly.md#-wolf-group-gly) and initiate [*failover*](#-wolf-failover-gly) operations.

</dd> <dt>

<span id="_wolf_failover_policy_gly"></span><span id="_WOLF_FAILOVER_POLICY_GLY"></span>**failover policy**
</dt> <dd>

Parameters that affect [*failover*](#-wolf-failover-gly) operations of a [*group*](g-gly.md#-wolf-group-gly). These parameters include the **FailoverThreshold** and **FailoverPeriod** properties.

</dd> <dt>

<span id="_wolf_failover_time_gly"></span><span id="_WOLF_FAILOVER_TIME_GLY"></span>**failover time**
</dt> <dd>

Amount of time it takes a [*group*](g-gly.md#-wolf-group-gly) to complete the [*failover*](#-wolf-failover-gly) process.

</dd> <dt>

<span id="_wolf_fault_tolerant_gly"></span><span id="_WOLF_FAULT_TOLERANT_GLY"></span>**fault tolerant**
</dt> <dd>

Non-stop, 100% availability of resources. Clients never experience an interruption or loss of service.

See also [*high availability*](h-gly.md#-wolf-high-availability-gly).

</dd> <dt>

<span id="_wolf_file_share_resource_gly"></span><span id="_WOLF_FILE_SHARE_RESOURCE_GLY"></span>**File Share resource**
</dt> <dd>

A file share managed as a cluster [*resource*](r-gly.md#-wolf-resource-gly). The Cluster service defines the File Share [*resource type*](r-gly.md#-wolf-resource-type-gly) for managing File Share resources.

</dd> </dl>

 

 




