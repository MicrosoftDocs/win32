---
title: FailbackWindowEnd
description: Provides the latest time that the group can be failed back to the node identified as its preferred owner node. The following table summarizes the attributes of the FailbackWindowEnd property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6da1df59-1bfb-486e-bdb2-fc384a46a18d
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- FailbackWindowEnd Failover Cluster ,for groups
- FailbackWindowEnd Failover Cluster
topic_type:
- apiref
api_name:
- FailbackWindowEnd
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FailbackWindowEnd

Provides the latest time that the [group](groups.md) can be [failed back](failback.md) to the [node](nodes.md) identified as its [*preferred owner*](https://www.bing.com/search?q=*preferred owner*) node. The following table summarizes the attributes of the **FailbackWindowEnd** property.



| Attribute | Value                                                               |
|-----------|---------------------------------------------------------------------|
| Data type | **DWORD**                                                           |
| Access    | Read/write                                                          |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)                           |
| Minimum   | 0 (specifies midnight)                                              |
| Maximum   | 23 (specifies 11:00 P.M.) or -1 (0xFFFFFFFF for no failback window) |
| Default   | -1 ( 0xFFFFFFFF)                                                    |



 

## Remarks

The value of the **FailbackWindowEnd** property can be set to the following values:



| Value           | Description                                                                   |
|-----------------|-------------------------------------------------------------------------------|
| 0 to 23         | Indicates the hour of day (local cluster time) that the failback window ends. |
| -1 (0xFFFFFFFF) | No failback window exists.                                                    |



 

Both the [**FailbackWindowStart**](groups-failbackwindowstart.md) and **FailbackWindowEnd** properties must be specified for a failback window to exist.

-   If a failback window exists, failback will only take place between the hours of [**FailbackWindowStart**](groups-failbackwindowstart.md) and **FailbackWindowEnd** if the group's preferred node is active or becomes active during that interval.
-   If no failback window exists, failback occurs immediately after the preferred node becomes active.

## Examples

The property value portion of a [property list](property-lists.md) entry for **FailbackWindowEnd** can be set with the following example code:


```C++
DWORD FailbackWindowEndData = 12;
CLUSPROP_DWORD FailbackWindowEndValue;

FailbackWindowEndValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
FailbackWindowEndValue.cbLength = sizeof(DWORD);
FailbackWindowEndValue.dw = FailbackWindowEndData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dt>

[**FailbackWindowStart**](groups-failbackwindowstart.md)
</dt> </dl>

 

 





