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
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# F

[A](a-gly.md) B [C](c-gly.md) [D](d-gly.md) [E](e-gly.md) F [G](g-gly.md) [H](h-gly.md) [I](i-gly.md) J K [L](l-gly.md) [M](m-gly.md) [N](n-gly.md) [O](o-gly.md) [P](p-gly.md) [Q](q-gly.md) [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) U [V](v-gly.md) [W](w-gly.md) X Y Z

<dl> <dt>

<span id="_wolf_failback_gly"></span><span id="_WOLF_FAILBACK_GLY"></span>**failback**
</dt> <dd>

Process of moving a [*group*](https://www.bing.com/search?q=*group*) back to its preferred [*node*](https://www.bing.com/search?q=*node*) when the node becomes [*active*](https://www.bing.com/search?q=*active*) after a failure.

</dd> <dt>

<span id="_wolf_failed_gly"></span><span id="_WOLF_FAILED_GLY"></span>**failed**
</dt> <dd>

Describes a [*node*](https://www.bing.com/search?q=*node*) or [*resource*](https://www.bing.com/search?q=*resource*) that has ceased operating and is unavailable to the [*cluster*](https://www.bing.com/search?q=*cluster*). Node or resource failure can trigger [*failover*](#-wolf-failover-gly).

</dd> <dt>

<span id="_wolf_failover_gly"></span><span id="_WOLF_FAILOVER_GLY"></span>**failover**
</dt> <dd>

Process of moving a [*group*](https://www.bing.com/search?q=*group*) to another [*node*](https://www.bing.com/search?q=*node*) in response to a node or [*resource*](https://www.bing.com/search?q=*resource*) failure.

</dd> <dt>

<span id="mscs.failover_cluster_gly"></span><span id="MSCS.FAILOVER_CLUSTER_GLY"></span>**failover cluster**
</dt> <dd>

The type of [*cluster*](https://www.bing.com/search?q=*cluster*) that the [*Cluster service*](https://www.bing.com/search?q=*Cluster service*) implements. Failover clusters are characterized by high availability. The failover cluster is one of two types of clusters provided by Microsoft [*Windows Clustering*](https://www.bing.com/search?q=*Windows Clustering*). This was previously known as a [*server cluster*](https://www.bing.com/search?q=*server cluster*).

</dd> <dt>

<span id="mscs.failover_cluster_api_gly"></span><span id="MSCS.FAILOVER_CLUSTER_API_GLY"></span>**Failover Cluster API**
</dt> <dd>

Collection of functions that are implemented by the [*Cluster service*](https://www.bing.com/search?q=*Cluster service*) and used by [*cluster-aware applications*](https://www.bing.com/search?q=*cluster-aware applications*), [*cluster management applications*](https://www.bing.com/search?q=*cluster management applications*), and [*resource DLLs*](https://www.bing.com/search?q=*resource DLLs*). The Failover Cluster API includes functions for managing [*cluster objects*](https://www.bing.com/search?q=*cluster objects*) and the [*cluster database*](https://www.bing.com/search?q=*cluster database*). This was previously known as the [*Server Cluster API*](https://www.bing.com/search?q=*Server Cluster API*).

</dd> <dt>

<span id="mscs.failover_cluster_instance_gly"></span><span id="MSCS.FAILOVER_CLUSTER_INSTANCE_GLY"></span>**failover cluster instance**
</dt> <dd>

A [*group*](https://www.bing.com/search?q=*group*) containing an [*IP Address resource*](https://www.bing.com/search?q=*IP Address resource*), an [*IPv6 Address resource*](https://www.bing.com/search?q=*IPv6 Address resource*), and/or an [*IPv6 Tunnel Address resource*](https://www.bing.com/search?q=*IPv6 Tunnel Address resource*) and a [*Network Name resource*](https://www.bing.com/search?q=*Network Name resource*), and additional resources necessary to run one or more applications or services. Clients can use the network name to access the resources in the group, analogous to using a computer name to access the services on a physical server. However, because a failover cluster instance is a group, it can be failed over to another [*node*](https://www.bing.com/search?q=*node*) without affecting the underlying name or address. This was previously known as a [*virtual server*](https://www.bing.com/search?q=*virtual server*).

</dd> <dt>

<span id="_wolf_failover_manager_gly"></span><span id="_WOLF_FAILOVER_MANAGER_GLY"></span>**Failover Manager**
</dt> <dd>

Software component in the [*Cluster service*](https://www.bing.com/search?q=*Cluster service*) that works with the [*Resource Manager*](https://www.bing.com/search?q=*Resource Manager*) to manage [*resources*](https://www.bing.com/search?q=*resources*) and [*groups*](https://www.bing.com/search?q=*groups*) and initiate [*failover*](#-wolf-failover-gly) operations.

</dd> <dt>

<span id="_wolf_failover_policy_gly"></span><span id="_WOLF_FAILOVER_POLICY_GLY"></span>**failover policy**
</dt> <dd>

Parameters that affect [*failover*](#-wolf-failover-gly) operations of a [*group*](https://www.bing.com/search?q=*group*). These parameters include the **FailoverThreshold** and **FailoverPeriod** properties.

</dd> <dt>

<span id="_wolf_failover_time_gly"></span><span id="_WOLF_FAILOVER_TIME_GLY"></span>**failover time**
</dt> <dd>

Amount of time it takes a [*group*](https://www.bing.com/search?q=*group*) to complete the [*failover*](#-wolf-failover-gly) process.

</dd> <dt>

<span id="_wolf_fault_tolerant_gly"></span><span id="_WOLF_FAULT_TOLERANT_GLY"></span>**fault tolerant**
</dt> <dd>

Non-stop, 100% availability of resources. Clients never experience an interruption or loss of service.

See also [*high availability*](https://www.bing.com/search?q=*high availability*).

</dd> <dt>

<span id="_wolf_file_share_resource_gly"></span><span id="_WOLF_FILE_SHARE_RESOURCE_GLY"></span>**File Share resource**
</dt> <dd>

A file share managed as a cluster [*resource*](https://www.bing.com/search?q=*resource*). The Cluster service defines the File Share [*resource type*](https://www.bing.com/search?q=*resource type*) for managing File Share resources.

</dd> </dl>

 

 




