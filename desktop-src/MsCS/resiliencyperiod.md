---
title: ResiliencyPeriod
description: Specifies the resiliency period for a group, in seconds.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: EB7C2AE2-097E-4DC7-8677-B2F289CAD3C9
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ResiliencyPeriod Failover Cluster
topic_type:
- apiref
api_name:
- ResiliencyPeriod
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ResiliencyPeriod

Specifies the resiliency period for a group, in seconds.



| Attribute            | Value                                     |
|----------------------|-------------------------------------------|
| Data type<br/> | **DWORD**                                 |
| Access<br/>    | [Read/write](read-write-properties.md)   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum<br/>   | 0<br/>                              |
| Maximum<br/>   | 0xFFFFFFFF<br/>                     |
| Default<br/>   | 0<br/>                              |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_GRP\_RESILIENCY\_PERIOD**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Group Common Properties](group-common-properties.md)
</dt> </dl>

 

 





