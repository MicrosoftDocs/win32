---
title: RetryPeriodOnFailure
description: Specifies the interval of time (in milliseconds) that a resource should remain in a failed state before the Cluster service attempts to restart it. The following table summarizes the attributes of the RetryPeriodOnFailure property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'dd0e19c5-70c7-4d9e-8ce8-fc5bc13a961c'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["RetryPeriodOnFailure Failover Cluster ,for resources", "RetryPeriodOnFailure Failover Cluster"]
topic_type:
- apiref
api_name:
- RetryPeriodOnFailure
api_type:
- NA
---

# RetryPeriodOnFailure

Specifies the interval of time (in milliseconds) that a [resource](resources.md) should remain in a failed state before the [Cluster service](cluster-service.md) attempts to restart it. The following table summarizes the attributes of the **RetryPeriodOnFailure** property.



| Attribute | Value                                                  |
|-----------|--------------------------------------------------------|
| Data type | **DWORD**                                              |
| Access    | [Read/write](read-write-properties.md)                |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md)              |
| Minimum   | [**RestartPeriod**](resources-restartperiod.md) value |
| Maximum   | 0xFFFFFFFF (no retry)                                  |
| Default   | 0x36EE80                                               |



 

## Remarks

When adjusting the **RetryPeriodOnFailure** property:

-   Intervals measured in minutes (multiples of 0xEA60) are recommended.
-   Do not set the interval any lower than that specified by the [**RestartPeriod**](resources-restartperiod.md) property.

The Cluster Service attempts to restart the resource by calling its resource DLL's [**Online**](online.md) entry point function.

## Examples

The property value portion of a [property list](property-lists.md) entry for **RetryPeriodOnFailure** can be set with the following example code:


```C++
DWORD RetryPeriodOnFailureData = ( 5 * 0xEA60 ); // 5 minutes
CLUSPROP_DWORD RetryPeriodOnFailureValue;
RetryPeriodOnFailureValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
RetryPeriodOnFailureValue.cbLength = sizeof(DWORD);
RetryPeriodOnFailureValue.dw = RetryPeriodOnFailureData;
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

[**RestartAction**](resources-restartaction.md)
</dt> <dt>

[**RestartPeriod**](resources-restartperiod.md)
</dt> <dt>

[**RestartThreshold**](resources-restartthreshold.md)
</dt> </dl>

 

 





