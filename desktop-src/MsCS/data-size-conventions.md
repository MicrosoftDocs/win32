---
title: Data Size Conventions
description: Failover Cluster API data size conventions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 283dc560-d547-4b42-b45c-435045080639
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- data Failover Cluster ,size conventions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Data Size Conventions

The [Failover Cluster API](the-server-cluster-api.md) uses the following conventions when returning and receiving data sizes.

-   Function parameters that contain the prefix *cb* express sizes as a count of bytes. For strings, this size includes the terminating **NULL**.
-   Function parameters that contain the prefix *cch* express sizes as a count of characters. For strings, this size may or may not include the terminating **NULL**. The function description will indicate when to include the **NULL** in the count.

Note that the Failover Cluster API uses Unicode (multi-byte) strings. Therefore the byte count of a string buffer will not be the same as the count of characters in the string.

 

 




