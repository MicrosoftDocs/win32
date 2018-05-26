---
title: Checkpointing
description: Many applications and other resources store data in registry keys outside of the cluster database.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6031fe2b-d5cb-477e-9d0f-c8c4a14ce02b
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- checkpointing Failover Cluster
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Checkpointing

Many applications and other [resources](resources.md) store data in registry keys outside of the [cluster database](cluster-database.md). Checkpointing is the process of associating a resource with one or more registry keys so that when the resource is moved to a new [node](nodes.md) (during [failover](failover.md), for example), the required keys are propagated to the local registry on the new node.

The [Failover Cluster API](the-server-cluster-api.md) allows cryptographic key containers to be checkpointed as well as normal registry keys. The following rules apply to checkpoints:

-   Whenever anything changes on the checkpointed registry tree and the resource is online, the [Cluster service](cluster-service.md) stores a copy of the tree on the [quorum resource](quorum-resource.md).
-   A change made to a checkpointed key while the resource is offline will be overwritten with the checkpointed data when the application comes online.
-   If the resource moves to another node, the Cluster service restores the registry tree from the quorum resource log file to the registry on the new node before the resource is brought online.
-   If the resource is deleted, the checkpoint is deleted.
-   Checkpoints are included in backups created by the [**BackupClusterDatabase**](/windows/previous-versions/ClusAPI/nf-clusapi-backupclusterdatabase?branch=master) function.
-   Multiple resource instances on different nodes must be handled carefully. Consider the situation where Resource A\[0\] stores data\[0\] in checkpoint A on node 0. Resource A\[1\] stores data\[1\] in checkpoint A on node 1. If Resource A\[1\] fails over to node 0, the Cluster service will replace data\[0\] with data\[1\] in checkpoint A. If Resource A\[0\] depends on data\[0\], it is likely to fail. One solution to this problem is to give the checkpointed keys different names on different nodes.

Applications and [resource DLLs](resource-dlls.md) manage checkpoints by using [control codes](about-control-codes.md). Note that the Cluster service does not pass any of the control codes involved with checkpointing to resource DLLs, which means that resource DLLs can use the checkpointing control codes freely without risking deadlocks. The following control codes work with checkpoints:

-   [CLUSCTL\_RESOURCE\_ADD\_CRYPTO\_CHECKPOINT](clusctl-resource-add-crypto-checkpoint.md)
-   [CLUSCTL\_RESOURCE\_ADD\_REGISTRY\_CHECKPOINT](clusctl-resource-add-registry-checkpoint.md)
-   [CLUSCTL\_RESOURCE\_ADD\_REGISTRY\_CHECKPOINT\_32BIT](clusctl-resource-add-registry-checkpoint-32bit.md)
-   [CLUSCTL\_RESOURCE\_ADD\_REGISTRY\_CHECKPOINT\_64BIT](clusctl-resource-add-registry-checkpoint-64bit.md)
-   [CLUSCTL\_RESOURCE\_DELETE\_CRYPTO\_CHECKPOINT](clusctl-resource-delete-crypto-checkpoint.md)
-   [CLUSCTL\_RESOURCE\_DELETE\_REGISTRY\_CHECKPOINT](clusctl-resource-delete-registry-checkpoint.md)
-   [CLUSCTL\_RESOURCE\_GET\_CRYPTO\_CHECKPOINTS](clusctl-resource-get-crypto-checkpoints.md)
-   [CLUSCTL\_RESOURCE\_GET\_REGISTRY\_CHECKPOINTS](clusctl-resource-get-registry-checkpoints.md)
-   [CLUSCTL\_RESOURCE\_TYPE\_GET\_CRYPTO\_CHECKPOINTS](clusctl-resource-type-get-crypto-checkpoints.md)
-   [CLUSCTL\_RESOURCE\_TYPE\_GET\_REGISTRY\_CHECKPOINTS](clusctl-resource-type-get-registry-checkpoints.md)

 

 




