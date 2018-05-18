---
title: FailoverThreshold
description: Specifies the maximum number of failover attempts that can be made on a group within a time interval defined by FailoverPeriod. The following table summarizes the attributes of the FailoverThreshold property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a747dde3-a73c-48db-b961-c59417e81b1f'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["FailoverThreshold Failover Cluster ,for groups", "FailoverThreshold Failover Cluster"]
topic_type:
- apiref
api_name:
- FailoverThreshold
api_type:
- NA
---

# FailoverThreshold

Specifies the maximum number of [failover](failover.md) attempts that can be made on a [group](groups.md) within a time interval defined by [**FailoverPeriod**](groups-failoverperiod.md). The following table summarizes the attributes of the **FailoverThreshold** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 0                                         |
| Maximum   | 0xFFFFFFFF                                |
| Default   | 0xFFFFFFFF                                |



 

## Remarks

If the [Cluster service](cluster-service.md) exceeds the number of failover attempts specified by **FailoverThreshold** within the time interval specified by [**FailoverPeriod**](groups-failoverperiod.md), it stops trying to fail over the group.

For example, if **FailoverThreshold** is set to 2 and [**RestartPeriod**](resources-restartperiod.md) is set to 1, a [node](nodes.md) can tolerate 2 failover attempts of the group within any 1-hour interval. More than 3 failover attempts can occur, as long as they occur over an interval that is greater than 1 hour.

If a value for **FailoverThreshold** is not specified, the default value is the number of nodes in the cluster minus 1. This is represented as 0xFFFFFFFF.

## Examples

The property value portion of a [property list](property-lists.md) entry for **FailoverThreshold** can be set with the following example code:


```C++
DWORD          FailoverThresholdData = 5;
CLUSPROP_DWORD FailoverThresholdValue;

FailoverThresholdValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
FailoverThresholdValue.cbLength  = sizeof(DWORD);
FailoverThresholdValue.dw        = FailoverThresholdData;
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

[**FailoverPeriod**](groups-failoverperiod.md)
</dt> <dt>

[**RestartPeriod**](resources-restartperiod.md)
</dt> </dl>

 

 





