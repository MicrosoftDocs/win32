---
title: Common Properties of a Cluster Object
description: A common property is an attribute possessed by every instance of a cluster object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5341d390-69dd-4e84-a443-f35a4b6c0bab'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["properties Failover Cluster , common", "properties Failover Cluster ,common,described"]
---

# Common Properties of a Cluster Object

A common [property](cluster-object-properties.md) is an attribute possessed by every instance of a [cluster object](cluster-objects.md). For example, each [node](nodes.md) has a [**NodeName**](nodes-nodename.md) property, thus **NodeName** is a common property for nodes. Each [resource](resources.md) has a [**RestartAction**](resources-restartaction.md) property; thus **RestartAction** is a common property for resources. An object's common properties exist for every instance of that object, regardless of how different the individual instances might be. For example, both a [Physical Disk](physical-disk.md) resource and a [File Share](file-share.md) resource possess a set of resource common properties, even though they are very different kinds of resources.

Common properties are always stored in the [cluster database](cluster-database.md).

Common properties are defined by the [Cluster service](cluster-service.md). End users and developers cannot add to or modify the set of common properties defined by a particular version of the Cluster service.

 

 




