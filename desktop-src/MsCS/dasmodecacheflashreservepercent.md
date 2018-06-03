---
title: S2DCacheFlashReservePercent
description: The percent of disk space, to reserve for the cache of a flash drive when using Storage Spaces Direct (2SD).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5D6DB59E-5375-49A6-84E0-241C3B157E3E
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- S2DCacheFlashReservePercent Failover Cluster
topic_type:
- apiref
api_name:
- S2DCacheFlashReservePercent
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# S2DCacheFlashReservePercent

The percent of disk space, to reserve for the cache of a flash drive when using Storage Spaces Direct (2SD).



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)<br/> |
| Minimum<br/>   | 0<br/>                                         |
| Maximum<br/>   | 100<br/>                                       |
| Default<br/>   | 0<br/>                                         |



 

## Remarks

The constant for this property is **CLUSTER\_S2D\_CACHE\_FLASH\_RESERVE\_PERCENT**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> <dt>

[CLUSCTL\_CLUSTER\_SET\_CLUSTER\_S2D\_ENABLED](clusctl-cluster-set-cluster-das-mode-enabled.md)
</dt> </dl>

 

 





