---
description: Allows specification of the point in time metric gathering is to be started and to specify the preferred sample interval time for periodic data gathering.
ms.assetid: 3dd6dc16-a618-49ff-bbaf-cfa25c249cf1
title: ControlSampleTimes method of the CIM_MetricService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_MetricService.ControlSampleTimes
api_type: 
- COM
api_location: 
- vmms.exe
---

# ControlSampleTimes method of the CIM\_MetricService class

Allows specification of the point in time metric gathering is to be started and to specify the preferred sample interval time for periodic data gathering.

Whenever sampling for additional metrics is started, the settings specified by this method may be used.

## Syntax


```mof
uint32 ControlSampleTimes(
  [in] datetime StartSampleTime,
  [in] datetime PreferredSampleInterval,
  [in] boolean  RestartGathering
);
```



## Parameters

<dl> <dt>

*StartSampleTime* \[in\]
</dt> <dd>

Point in time when sampling for the metrics is to be started.

A value of 99990101000000.000000+000 shall indicate that sampling should start at the next time it is synchronized to the full hour. Sampling is synchronized to the full hour if seconds since midnight modulo sample interval in seconds is equal to 0.

</dd> <dt>

*PreferredSampleInterval* \[in\]
</dt> <dd>

Preferred sample interval time. In order to get correlatable metrics, it is recommended that the sample interval be chosen in a way that 3600 modulo sample interval time in seconds is equal to 0.

It is the responsibility of the CIM metric service implementation to decide whether the requested sample interval time is honored.

The CIM client can check whether or not the metric providers are honoring the requested sample interval time by retrieving related BaseMetricDefinition instances and checking the contents of the [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md).**SampleInterval** property.

</dd> <dt>

*RestartGathering* \[in\]
</dt> <dd>

**TRUE** to request that gathering of all metrics associated to the metric service is re-started with this method call.

</dd> </dl>

## Return value

Returns a 0 on success; otherwise, returns an error.

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Method Reserved** (..)
</dt> <dt>

**Vendor Specific** (32768..65535)
</dt> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_MetricService**](cim-metricservice.md)
</dt> </dl>

 

 




