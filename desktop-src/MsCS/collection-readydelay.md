---
title: ReadyDelay
description: Indicates how much time (in seconds) should be pass after the ReadySetting criteria is met is before any sets dependent on to the group set are allowed to start.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 457DD069-D300-40C1-8AA9-25B9018DFC3D
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ReadyDelay Failover Cluster
topic_type:
- apiref
api_name:
- ReadyDelay
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ReadyDelay

Indicates how much time (in seconds) should be pass after the [**ReadySetting**](collection-readysetting.md) criteria is met is before any sets dependent on to the group set are allowed to start.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)<br/> |
| Minimum<br/>   | 0<br/>                                         |
| Maximum<br/>   | 0xFFFFFFFF<br/>                                |
| Default<br/>   | 0<br/>                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_COLLECTION\_READY\_DELAY**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Collection Common Properties](collection-common-properties.md)
</dt> </dl>

 

 





