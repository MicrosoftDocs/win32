---
title: S2DIOLatencyThreshold
description: Specifies the IO latency threshold for Storage Spaces Direct (2SD).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 70EE1C2E-71BE-43AF-9A8F-A5E66F0074C7
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- S2DIOLatencyThreshold Failover Cluster
topic_type:
- apiref
api_name:
- S2DIOLatencyThreshold
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# S2DIOLatencyThreshold

Specifies the IO latency threshold for Storage Spaces Direct (2SD).



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)<br/> |
| Minimum<br/>   | 50<br/>                                        |
| Maximum<br/>   | 20000<br/>                                     |
| Default<br/>   | 10000<br/>                                     |



 

## Remarks

The constant for this property is **CLUSTER\_S2D\_IO\_LATENCY\_THRESHOLD**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





