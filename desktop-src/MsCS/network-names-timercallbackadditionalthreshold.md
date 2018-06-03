---
title: TimerCallbackAdditionalThreshold
description: Provides the TBD of the network being managed by a Cluster Name resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d102c63d-992d-41c2-b440-67821a841b4b
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- TimerCallbackAdditionalThreshold Failover Cluster ,for cluster names
- TimerCallbackAdditionalThreshold Failover Cluster
topic_type:
- apiref
api_name:
- TimerCallbackAdditionalThreshold
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TimerCallbackAdditionalThreshold

Provides the TBD of the [network](networks.md) being managed by a [Cluster Name](network-name.md) resource. The following table summarizes the attributes of the **TimerCallbackAdditionalThreshold** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | TBD                                       |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 0x7FFFFFFF                                |
| Default   | 5                                         |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for [**HostRecordTTL**](hostrecordttl.md) can be set with the following example code.


```C++
DWORD          TimerCallbackAdditionalThresholdData = 10;
CLUSPROP_DWORD TimerCallbackAdditionalThresholdValue;

TimerCallbackAdditionalThresholdValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
TimerCallbackAdditionalThresholdValue.cbLength  = sizeof(DWORD);
TimerCallbackAdditionalThresholdValue.dw        = TimerCallbackAdditionalThresholdData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Cluster Name Private Properties](network-name-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> </dl>

 

 





