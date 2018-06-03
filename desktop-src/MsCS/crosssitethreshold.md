---
title: CrossSiteThreshold
description: Controls how many Cluster Service heartbeats can be missed across sites before it determines that Cluster Service has stopped responding.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2ED905CF-374A-4D00-9CCB-EA480A73C82A
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CrossSiteThreshold Failover Cluster
topic_type:
- apiref
api_name:
- CrossSiteThreshold
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CrossSiteThreshold

Controls how many Cluster Service heartbeats can be missed across sites before it determines that Cluster Service has stopped responding.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)<br/> |
| Minimum<br/>   | **CROSS\_SITE\_THRESHOLD\_MIN**                      |
| Maximum<br/>   | **CROSS\_SITE\_THRESHOLD\_MAX**                      |
| Default<br/>   | **CROSS\_SITE\_THRESHOLD\_DEFAULT**                  |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_CROSS\_SITE\_THRESHOLD**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





