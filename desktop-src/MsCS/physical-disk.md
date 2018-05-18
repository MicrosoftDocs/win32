---
title: Physical Disk
description: The Physical Disk resource type manages a disk on a shared bus connected to two or more cluster nodes. Most groups contain one or more Physical Disk resources as dependencies for other resources in the group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd42e9bca-3717-44f7-a1b9-dfad1dbddd23'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource types Failover Cluster ,Physical Disk", "Physical Disk resource type Failover Cluster", "Physical Disk resource type Failover Cluster ,resources"]
---

# Physical Disk

The Physical Disk [resource type](resource-types.md) manages a disk on a shared bus connected to two or more cluster [nodes](nodes.md). Most [groups](groups.md) contain one or more Physical Disk [resources](resources.md) as [dependencies](resource-dependencies.md) for other resources in the group.

The Physical Disk resource is the only default resource type that can operate as a cluster's [quorum resource](quorum-resource.md).

The following table summarizes the characteristics of the Physical Disk resource type.



| Characteristic                                                   | Description                                                                                                                                                                                                                         |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required [dependencies](resource-dependencies.md)<br/>    | None.<br/>                                                                                                                                                                                                                    |
| Required [private properties](private-properties.md)<br/> | [**Signature**](physical-disks-signature.md)<br/>                                                                                                                                                                            |
| Optional private properties<br/>                           | [**ConditionalMount**](physical-disks-conditionalmount.md), [**DiskInfo**](physical-disks-diskinfo.md), [**MountVolumeInfo**](physical-disks-mountvolumeinfo.md), and [**SkipChkdsk**](physical-disks-skipchkdsk.md)<br/> |



 

 

 





