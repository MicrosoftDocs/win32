---
title: AdminAccessPoint
description: Management point type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 908F2D00-1ACE-4564-A373-871A5B7C38E0
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- AdminAccessPoint Failover Cluster
topic_type:
- apiref
api_name:
- AdminAccessPoint
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AdminAccessPoint

Management point type.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | **CLUSTER\_MGMT\_POINT\_TYPE\_NONE**      |
| Maximum   | **CLUSTER\_MGMT\_POINT\_TYPE\_CNO\_ONLY** |
| Default   | **CLUSTER\_MGMT\_POINT\_TYPE\_CNO**       |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_MGMT\_POINT\_TYPE**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





