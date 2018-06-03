---
title: QuarantineThreshold
description: Specifies the quarantine threshold for a node, in minutes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 22CBB428-EBFC-43A4-8327-D92F31A1B5B3
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- QuarantineThreshold Failover Cluster
topic_type:
- apiref
api_name:
- QuarantineThreshold
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# QuarantineThreshold

Specifies the quarantine threshold for a node, in minutes.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)<br/> |
| Minimum<br/>   | 0<br/>                                         |
| Maximum<br/>   | 0xFFFFFFFF<br/>                                |
| Default<br/>   | 3<br/>                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_QUARANTINE\_THRESHOLD**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





