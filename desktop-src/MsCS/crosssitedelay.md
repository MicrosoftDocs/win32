---
title: CrossSiteDelay
description: Controls the time interval, in milliseconds, that the cluster network driver waits between sending Cluster Service heartbeats across sites.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 81ED4EBC-2BEA-4BFD-8EF5-A163D5BA9521
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CrossSiteDelay Failover Cluster
topic_type:
- apiref
api_name:
- CrossSiteDelay
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CrossSiteDelay

Controls the time interval, in milliseconds, that the cluster network driver waits between sending Cluster Service heartbeats across sites.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)<br/> |
| Minimum<br/>   | **CROSS\_SITE\_DELAY\_MIN**                          |
| Maximum<br/>   | **CROSS\_SITE\_DELAY\_MAX**                          |
| Default<br/>   | **CROSS\_SITE\_DELAY\_DEFAULT**                      |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_CROSS\_SITE\_DELAY**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





