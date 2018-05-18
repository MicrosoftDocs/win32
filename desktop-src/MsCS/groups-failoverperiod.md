---
title: FailoverPeriod
description: Specifies a number of hours during which a maximum number of failover attempts, specified by FailoverThreshold, can occur. The following table summarizes the attributes of the FailoverPeriod property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5277a4a7-2866-4c16-8ad0-ea3a33714583'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["FailoverPeriod Failover Cluster ,for groups", "FailoverPeriod Failover Cluster"]
topic_type:
- apiref
api_name:
- FailoverPeriod
api_type:
- NA
---

# FailoverPeriod

Specifies a number of hours during which a maximum number of [failover](failover.md) attempts, specified by [**FailoverThreshold**](groups-failoverthreshold.md), can occur. The following table summarizes the attributes of the **FailoverPeriod** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 0                                         |
| Maximum   | 1193                                      |
| Default   | 6                                         |



 

## Remarks

If the [Cluster service](cluster-service.md) exceeds the number of failover attempts specified by [**FailoverThreshold**](groups-failoverthreshold.md) within the time interval specified by **FailoverPeriod**, it stops trying to fail over the [group](groups.md).

For example, if [**FailoverThreshold**](groups-failoverthreshold.md) is set to 2 and **FailoverPeriod** is set to 1, then a [node](nodes.md) can tolerate two failover attempts of the group within any 1-hour interval. More than three failover attempts can occur, as long as they occur over an interval that is greater than 1 hour.

**FailoverPeriod** has a maximum value of 1193 hours. If a value for **FailoverPeriod** is not specified, the default value is 6 hours.

## Examples

The property value portion of a [property list](property-lists.md) entry for **FailoverPeriod** can be set with the following example code:


```C++
DWORD          FailoverPeriodData = 5;
CLUSPROP_DWORD FailoverPeriodValue;

FailoverPeriodValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
FailoverPeriodValue.cbLength  = sizeof(DWORD);
FailoverPeriodValue.dw        = FailoverPeriodData;
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

[**FailoverThreshold**](groups-failoverthreshold.md)
</dt> <dt>

[**RestartPeriod**](resources-restartperiod.md)
</dt> </dl>

 

 





