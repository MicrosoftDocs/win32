---
title: Quorum Resource
description: In every failover cluster, a single resource is designated as the quorum resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4c2ee30e-4de2-44ba-93ba-d2d89196545e
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- quorum resource Failover Cluster
- resources Failover Cluster ,quorum
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Quorum Resource

In every [*failover cluster*](https://www.bing.com/search?q=*failover cluster*), a single [resource](resources.md) is designated as the [*quorum resource*](https://www.bing.com/search?q=*quorum resource*). The [Cluster service](cluster-service.md) uses the quorum resource to perform two fundamental tasks:

-   The quorum resource allows the cluster to maintain its state and configuration independently of individual node failures. The quorum resource stores a constantly-updated version of the cluster database and is accessible to all cluster nodes. When a node forms a cluster, it compares its local copy of the cluster database with the data stored on the quorum resource and updates its copy if necessary.
-   The quorum resource enforces cluster unity, preventing "split-brain syndrome" in cases where communication failures result in two or more sets of nodes that can communicate within each set but not across sets. In such cases, only the node that controls the quorum resource, and nodes that can communicate with that node, are allowed to form a cluster.

A cluster uses one of two types of quorum resources, and depending on which type it uses, the cluster is either a *quorum-device cluster* or *a majority-of-nodes cluster*. The type of quorum resource, and therefore the type of the cluster, can be changed after the cluster is set up.

A quorum-device cluster requires a storage-class resource on a shared SCSI or FibreChannel bus. By default, failover clusters allow only physical disk resources to operate as quorum devices. However, third-party developers can create their own resource types to support other kinds of storage devices as quorum devices. For more information, see [Creating Resource Types](creating-resource-types.md).

A majority-of-nodes cluster uses a set of local disks called quorum disk set as its storage media. Each cluster node contributes one local disk to the quorum disk set. Thus, while the majority-of-nodes resource behaves like any other cluster resource and allows only one owner at a time, the owner of the resource must coordinate reads and writes with the other cluster nodes. In order to establish quorum and form a cluster, a majority of the nodes (M) must be available. In other words, a majority-of-nodes cluster can form and continue to run as long as there are M &gt;= (N + 1) / 2 active nodes (where N is the total number of nodes configured as members of the cluster). Note that there are ways to force quorum in cases where the number of active nodes is less than M.

There are advantages and disadvantages to both types of clusters. Majority-of-nodes clusters allow the creation of "geoclusters," or clusters of nodes separated by great distances, but their failure semantics are much more restrictive than quorum device clusters. For example, without forcing quorum, a single-node majority-of-nodes cluster is not possible. Quorum-device clusters can tolerate more node failures but are geographically restricted to the length of the shared SCSI or FibreChannel bus.

For more information on setting up and administering the different quorum types, see Windows Help.

For information on specific API elements related to quorum resources, see the following topics:

-   [**ClusResource.BecomeQuorumResource**](clusresource-becomequorumresource.md)
-   [**Cluster.QuorumLogSize**](cluster-quorumlogsize.md)
-   [**Cluster.QuorumPath**](cluster-quorumpath.md)
-   [**Cluster.QuorumResource**](cluster-quorumresource.md)
-   [**GetClusterNodeState**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_node_state)
-   [**GetClusterQuorumResource**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_quorum_resource)
-   [**QuorumResourceLost**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pquorum_resource_lost)
-   [**SetClusterQuorumResource**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_quorum_resource)

 

 




