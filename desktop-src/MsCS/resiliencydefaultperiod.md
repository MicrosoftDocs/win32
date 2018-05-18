---
title: ResiliencyDefaultPeriod
description: Specifies the default resiliency period, in seconds, for the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '05A61769-F5A5-4D65-B936-0139BEB9444A'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ResiliencyDefaultPeriod Failover Cluster"]
topic_type:
- apiref
api_name:
- ResiliencyDefaultPeriod
api_type:
- NA
---

# ResiliencyDefaultPeriod

Specifies the default resiliency period, in seconds, for the cluster.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](clusprop-dword.md)<br/> |
| Minimum<br/>   | 0<br/>                                         |
| Maximum<br/>   | 0xFFFFFFFF<br/>                                |
| Default<br/>   | 240<br/>                                       |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_RESILIENCY\_DEFAULT\_SECONDS**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





