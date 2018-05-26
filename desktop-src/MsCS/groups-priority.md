---
title: Priority
description: The priority value of the resource group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6B07E8A9-FE27-4A6E-9081-49F3E6C9B86A
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Priority Failover Cluster
topic_type:
- apiref
api_name:
- Priority
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Priority

The priority value of the resource group. This property controls entities such as the start order.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | **PriorityDisabled** (0)                  |
| Maximum   | **PriorityHigh** (3000)                   |
| Default   | **PriorityMedium** (2000)                 |



 

## Remarks

The **Priority** property can be set to one of the following values.



| Value                     | Description                                                                           |
|---------------------------|---------------------------------------------------------------------------------------|
| **PriorityDisabled** (0)  | Disabled priority. A group that has a disabled priority does not start automatically. |
| **PriorityLow** (1000)    | Low priority.                                                                         |
| **PriorityMedium** (2000) | Medium priority.                                                                      |
| **PriorityHigh** (3000)   | High priority.                                                                        |



 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Group Common Properties](group-common-properties.md)
</dt> </dl>

 

 





