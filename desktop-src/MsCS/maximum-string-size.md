---
title: Maximum Property Size
description: For all string properties, the cluster imposes no restrictions on the size of the string that you use.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a8d8be10-a9f3-410e-b400-08e45880eba7
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- maximum string size Failover Cluster
- properties Failover Cluster ,maximum string size
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Maximum Property Size

For all string [properties](cluster-object-properties.md), the [*cluster*](c-gly.md#-wolf-cluster-gly) imposes no restrictions on the size of the string that you use. It is possible to store megabyte-sized strings as cluster property values. However, the registry API recommends that data over 2048 KB in size (2 MB) should be stored in an external file. Other factors may also limit string size:

-   Available memory.
-   System limits such as **MAX\_PATH** (260).
-   The ability of monitors and user interfaces to display the data properly.
-   Throughput and performance impact.

In general, megabyte-size strings stored as properties will adversely impact performance and usability. [*Physical Disk resources*](p-gly.md#-wolf-physical-disk-resource-gly) should be used for large-scale data storage.

 

 




