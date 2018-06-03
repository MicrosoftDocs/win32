---
title: MaximumMonitors
description: The maximum number of monitors.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 52B24EE5-1C51-41A4-A325-87609F98B975
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- MaximumMonitors Failover Cluster
topic_type:
- apiref
api_name:
- MaximumMonitors
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MaximumMonitors

The maximum number of monitors.



| Attribute | Value                                               |
|-----------|-----------------------------------------------------|
| Data type | **DWORD**                                           |
| Access    | [Read/write](read-write-properties.md)             |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)           |
| Minimum   | **CLUSTER\_RESOURCE\_TYPE\_MAX\_MONITORS\_MIN**     |
| Maximum   | **CLUSTER\_RESOURCE\_TYPE\_MAX\_MONITORS\_MAX**     |
| Default   | **CLUSTER\_RESOURCE\_TYPE\_MAX\_MONITORS\_DEFAULT** |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_RESTYPE\_DUMP\_SERVICES**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Resource Common Properties](resource-common-properties.md)
</dt> </dl>

 

 





