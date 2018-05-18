---
title: ControlSampleTimes method of the CIM\_MetricService class
description: Specifies when metrics are gathered for a metric service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '502aff19-cc41-43cc-87e9-7c605de32c76'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ControlSampleTimes method", "ControlSampleTimes method, CIM_MetricService class", "CIM_MetricService class, ControlSampleTimes method"]
topic_type:
- apiref
api_name:
- CIM_MetricService.ControlSampleTimes
api_location:
- VMMS.exe
api_type:
- COM
---

# ControlSampleTimes method of the CIM\_MetricService class

Specifies when metrics are gathered for a metric service.

## Syntax


```mof
uint32 ControlSampleTimes(
  [in] datetime StartSampleTime,
  [in] datetime PreferredSampleInterval,
  [in] boolean  RestartGathering
);
```



## Parameters

<dl> <dt>

*StartSampleTime* \[in\]
</dt> <dd>

The point in time to start metric sampling.

</dd> <dt>

*PreferredSampleInterval* \[in\]
</dt> <dd>

The preferred sample interval time for periodic data gathering.

</dd> <dt>

*RestartGathering* \[in\]
</dt> <dd>

**true** to request that metric gathering is restarted for the metric service; otherwise, **false**.

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Method Reserved** (3–32767)
</dt> <dt>

**Vendor Specific** (32768–65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_MetricService**](cim-metricservice.md)
</dt> </dl>

 

 





