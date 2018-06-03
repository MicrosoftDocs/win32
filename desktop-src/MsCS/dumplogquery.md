---
title: DumpLogQuery
description: Specifies a query that can be used to export logs for resource types.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7313AFC8-B27D-426F-87CB-8DEB17145A40
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DumpLogQuery Failover Cluster
topic_type:
- apiref
api_name:
- DumpLogQuery
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DumpLogQuery

Specifies a query that can be used to export logs for resource types.



| Attribute            | Value                                                            |
|----------------------|------------------------------------------------------------------|
| Data type<br/> | An array of null-terminated Unicode strings.<br/>          |
| Access<br/>    | [Read/write](read-write-properties.md)                          |
| Structure<br/> | [**CLUSPROP\_MULTI\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_sz)                 |
| Maximum<br/>   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default<br/>   | **NULL**                                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_RESTYPE\_DUMP\_LOG\_QUERY**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Resource Type Common Properties](resource-type-common-properties.md)
</dt> </dl>

 

 





