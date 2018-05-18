---
title: GetMetricValues method of the CIM\_MetricService class
description: Retrieves a filtered list of metric values.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd636e2b2-df93-44bc-a9b4-ea5dd616b95d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetMetricValues method", "GetMetricValues method, CIM_MetricService class", "CIM_MetricService class, GetMetricValues method"]
topic_type:
- apiref
api_name:
- CIM_MetricService.GetMetricValues
api_location:
- VMMS.exe
api_type:
- COM
---

# GetMetricValues method of the CIM\_MetricService class

Retrieves a filtered list of metric values.

## Syntax


```mof
uint32 GetMetricValues(
  [in]  CIM_BaseMetricDefinition REF Definition,
  [in]  uint16                       Range,
  [in]  uint16                       Count,
  [out] CIM_BaseMetricValue      REF Values[]
);
```



## Parameters

<dl> <dt>

*Definition* \[in\]
</dt> <dd>

A reference to the metric definition from which to retrieve metric values.

</dd> <dt>

*Range* \[in\]
</dt> <dd>

Indicates how the metric value instances are selected. The algorithm for ordering value instances is metric definition specific.

<dt>

<span id="Minimum"></span><span id="minimum"></span><span id="MINIMUM"></span>

**Minimum** (2)


</dt> <dd></dd> <dt>

<span id="Maximum"></span><span id="maximum"></span><span id="MAXIMUM"></span>

**Maximum** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl> </dd> <dt>

*Count* \[in\]
</dt> <dd>

The maximum number of metric value instances to return.

</dd> <dt>

*Values* \[out\]
</dt> <dd>

An array that contains the returned metric values.

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

 

 





