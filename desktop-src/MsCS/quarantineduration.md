---
title: QuarantineDuration
description: Specifies the quarantine duration for a node, in seconds.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: C3995196-A3BD-4D2E-BF3F-C8E0FBC50C50
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- QuarantineDuration Failover Cluster
topic_type:
- apiref
api_name:
- QuarantineDuration
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# QuarantineDuration

Specifies the quarantine duration for a node, in seconds.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)<br/> |
| Minimum<br/>   | 0<br/>                                         |
| Maximum<br/>   | 0xFFFFFFFF<br/>                                |
| Default<br/>   | 0<br/>                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_QUARANTINE\_DURATION**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





