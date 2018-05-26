---
title: ResiliencyLevel
description: Specifies the resiliency level for the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: F23A7A7E-DC42-489D-B6D6-5C7BA10DCE40
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ResiliencyLevel Failover Cluster
topic_type:
- apiref
api_name:
- ResiliencyLevel
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ResiliencyLevel

Specifies the resiliency level for the cluster.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)<br/> |
| Minimum<br/>   | 1<br/>                                         |
| Maximum<br/>   | 2<br/>                                         |
| Default<br/>   | 1<br/>                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_RESILIENCY\_LEVEL**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





