---
title: Cluster Database
description: The cluster database is a set of keys, sometimes referred to as the cluster hive, under HKEY\_LOCAL\_MACHINE in the registry.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d2c1a9c0-7e87-4a3c-9a1a-7f1756f97804
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- cluster database Failover Cluster
- cluster database Failover Cluster ,described
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Cluster Database

The cluster database is a set of keys, sometimes referred to as the cluster hive, under **HKEY\_LOCAL\_MACHINE** in the registry. It contains information about all physical and logical elements in a cluster, including a listing of [cluster objects](cluster-objects.md), their [properties](cluster-object-properties.md), and configuration data.

Each node stores a continuously updated copy of the cluster database. The [Cluster services](cluster-service.md) on each [node](nodes.md) cooperate to maintain a consistent, updated image by participating in global updates and periodic consistency checks. The [quorum resource](quorum-resource.md) also maintains an updated copy of the cluster database.

Many typical programming tasks involve direct or indirect changes to the cluster database. The [Failover Cluster API](the-server-cluster-api.md) provides many different ways to interact with the cluster database, but there is a definite order of preference governing which APIs should be used in which circumstances. For more information, see [Standard Order of Preference](standard-order-of-preference.md). Never use the registry functions to access or change the cluster database. The registry functions will corrupt the cluster database and render the cluster unusable.

 

 




