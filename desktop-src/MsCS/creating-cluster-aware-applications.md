---
title: Creating Cluster-Aware Applications
description: The following sections attempt to reduce the general task of creating a cluster-aware application to smaller tasks that lead to specific API elements, procedures, and examples.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '90b1b234-7d3c-4ffb-8a42-2704e9a3671d'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["cluster-aware applications Failover Cluster ,creating"]
---

# Creating Cluster-Aware Applications

The following sections attempt to reduce the general task of creating a [cluster-aware application](cluster-aware-applications.md) to smaller tasks that lead to specific API elements, procedures, and examples. The goal is to help you identify and implement sets of procedures that create the level of cluster interaction your application requires.



| Task                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Receiving Cluster Events](receiving-cluster-events.md)                     | Tasks related to creating a notification port to receive notifications of cluster events such as property changes or the creation and deletion of objects.                                                                                                                                                                                                                                                |
| [Getting Cluster Information](getting-cluster-information.md)               | "Read-only" tasks related to discovering information about the state and configuration of the [*cluster*](c-gly.md#-wolf-cluster-gly): enumerating objects, retrieving properties, checking object states, and getting object-specific data such as required [dependencies](resource-dependencies.md), available disks, and [*preferred owner*](p-gly.md#-wolf-preferred-owner-gly)[nodes](nodes.md). |
| [Changing the Cluster Configuration](changing-the-cluster-configuration.md) | Tasks concerned with making changes to the cluster such as changing properties, changing object states, creating resources, and configuring groups.                                                                                                                                                                                                                                                       |



 

Many of the tasks presented above depend on familiarity with certain features of the API such as [value lists](value-lists.md), [property lists](property-lists.md), and [property tables](property-tables.md).

## Related topics

<dl> <dt>

[Using the Failover Cluster APIs](using-the-server-cluster-api.md)
</dt> </dl>

 

 




