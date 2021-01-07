---
description: Provides the ability to return a filtered list of CIM\_BaseMetricValue instances.
ms.assetid: c207a0ef-11f1-42c4-af77-3dcf3fbff8a7
title: GetMetricValues method of the CIM_MetricService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_MetricService.GetMetricValues
api_type: 
- COM
api_location: 
- vmms.exe
---

# GetMetricValues method of the CIM\_MetricService class

Provides the ability to return a filtered list of [**CIM\_BaseMetricValue**](cim-basemetricvalue.md) instances.

## Syntax


```mof
uint32 GetMetricValues(
  [in]  CIM_BaseMetricDefinition REF Definition,
  [in]  uint16                       Range,
  [in]  uint16                       Count,
  [out] CIM_BaseMetricValue      REF Values[]
);
```



## Parameters

<dl> <dt>

*Definition* \[in\]
</dt> <dd>

Identifies a [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md) for which metrics will be returned.

</dd> <dt>

*Range* \[in\]
</dt> <dd>

Identifies how the instances are selected. The algorithm for ordering value instances is metric-definition specific.

<dt>

<span id="Minimum"></span><span id="minimum"></span><span id="MINIMUM"></span>

**Minimum** (2)


</dt> <dd></dd> <dt>

<span id="Maximum"></span><span id="maximum"></span><span id="MAXIMUM"></span>

**Maximum** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (..)


</dt> <dd></dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific** (32768..65535)


</dt> <dd></dd> </dl> </dd> <dt>

*Count* \[in\]
</dt> <dd>

Identifies the maximum number of instances to be returned by the method.

</dd> <dt>

*Values* \[out\]
</dt> <dd>

Upon successful completion of the method, contains references to instances of [**CIM\_BaseMetricValue**](cim-basemetricvalue.md), filtered according to the values of the input parameters.

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

 

 




