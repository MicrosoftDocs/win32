---
title: Read-only Properties
description: Read-only properties cannot be changed through the normal property manipulation API elements.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7df0981b-7253-40c1-9a5d-44cfc4cdf13b'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["properties Failover Cluster ,access,read-only"]
---

# Read-only Properties

Read-only [properties](cluster-object-properties.md) cannot be changed through the normal property manipulation API elements. For some read-only properties, there are specialized API elements that change the property indirectly. For example, the [**Name**](networks-name.md) property for [networks](networks.md) is read-only, but the [cluster object management function](cluster-object-management-functions.md) [**SetClusterNetworkName**](setclusternetworkname.md) has the effect of changing the property.

Do not try to force a change to a read-only property by direct manipulation of the [cluster database](cluster-database.md). The result is likely to be an unusable [*cluster*](c-gly.md#-wolf-cluster-gly).

 

 




