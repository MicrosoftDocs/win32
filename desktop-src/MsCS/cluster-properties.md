---
title: Failover Cluster Properties
description: Each failover cluster object has a set of properties that define its identity and behavior in the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a5607384-57c6-4f63-b53b-693f7053765b
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- properties Failover Cluster ,grouped by scope
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Failover Cluster Properties

Each [failover cluster object](cluster-objects.md) has a set of [properties](cluster-object-properties.md) that define its identity and behavior in the [*cluster*](c-gly.md#-wolf-cluster-gly). Applications and [resource DLLs](resource-dlls.md) manipulate the properties of failover cluster objects to maintain awareness of the failover cluster and to change the failover cluster to suit their needs.

Reference information on failover cluster properties is divided into the following sections based on [*property scope*](p-gly.md#-wolf-property-scope-gly).

-   [Common Properties](common-properties-ref.md) are attributes possessed by all instances of a failover cluster object.
-   [Private Properties](private-properties-ref.md) are only possessed by individual object instances.

 

 




