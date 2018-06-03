---
title: DumpPolicy
description: Specifies the dump collection policy for the cluster service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: E5DB06E7-1826-488C-98EF-5EA5D6A8D3F7
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DumpPolicy Failover Cluster
topic_type:
- apiref
api_name:
- DumpPolicy
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DumpPolicy

Specifies the dump collection policy for the cluster service.



| Attribute            | Value                                                                   |
|----------------------|-------------------------------------------------------------------------|
| Data type<br/> | **ULARGE\_INTEGER**<br/>                                          |
| Access<br/>    | [Read/write](read-write-properties.md)                                 |
| Structure<br/> | [**CLUSPROP\_ULARGE\_INTEGER**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_ularge_integer)<br/> |
| Minimum<br/>   | 0<br/>                                                            |
| Maximum<br/>   | 0<br/>                                                            |
| Default<br/>   | 0<br/>                                                            |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_RESTYPE\_DUMP\_POLICY**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Resource Type Common Properties](resource-type-common-properties.md)
</dt> </dl>

 

 





