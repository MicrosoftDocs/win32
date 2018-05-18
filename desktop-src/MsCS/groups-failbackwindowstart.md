---
title: FailbackWindowStart
description: Provides the earliest time (that is, local time as kept by the cluster) that the group can be failed back to the node identified as its preferred owner node. The following table summarizes the attributes of the FailbackWindowStart property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '33168423-88cb-4f7f-ad52-dc0299986f21'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["FailbackWindowStart Failover Cluster ,for groups", "FailbackWindowStart Failover Cluster"]
topic_type:
- apiref
api_name:
- FailbackWindowStart
api_type:
- NA
---

# FailbackWindowStart

Provides the earliest time (that is, local time as kept by the [*cluster*](c-gly.md#-wolf-cluster-gly)) that the group can be [failed back](failback.md) to the [node](nodes.md) identified as its [*preferred owner*](p-gly.md#-wolf-preferred-owner-gly) node. The following table summarizes the attributes of the **FailbackWindowStart** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 0 (specifies midnight)                    |
| Maximum   | 23 (specifies 11:00 P.M.)                 |
| Default   | -1 (unsigned 0xFFFFFFFF)                  |



 

## Remarks

The value of the **FailbackWindowStart** property can be set to the following values.



| Value           | Description                                                                   |
|-----------------|-------------------------------------------------------------------------------|
| 0 to 23         | Indicates the hour of day (local cluster time) that the failback window ends. |
| -1 (0xFFFFFFFF) | No failback window exists.                                                    |



 

Both the [**FailbackWindowEnd**](groups-failbackwindowend.md) and **FailbackWindowStart** properties must be specified for a failback window to exist.

-   If a failback window exists, failback will only take place between the hours of **FailbackWindowStart** and [**FailbackWindowEnd**](groups-failbackwindowend.md) if the group's preferred node is active or becomes active during that interval.
-   If no failback window exists, failback occurs immediately after the preferred node becomes active.

If the current owner of the group fails before the time specified by **FailbackWindowStart**, every group hosted by the failed node is moved regardless of the failback window settings.

## Examples

The property value portion of a [property list](property-lists.md) entry for **FailbackWindowStart** can be set with the following example code:


```C++
DWORD FailbackWindowStartData = 10;
CLUSPROP_DWORD FailbackWindowStartValue;

FailbackWindowStartValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
FailbackWindowStartValue.cbLength = sizeof(DWORD);
FailbackWindowStartValue.dw = FailbackWindowStartData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> <dt>

[**FailbackWindowEnd**](groups-failbackwindowend.md)
</dt> </dl>

 

 





