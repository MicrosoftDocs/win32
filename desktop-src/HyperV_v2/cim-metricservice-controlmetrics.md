---
description: ControlMetrics method of the CIM_MetricService class - Enables and disables the collection of metrics.
ms.assetid: afb90863-e70a-46e5-b1b7-d959dcacc306
title: ControlMetrics method of the CIM_MetricService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_MetricService.ControlMetrics
api_type: 
- COM
api_location: 
- vmms.exe
---

# ControlMetrics method of the CIM\_MetricService class

Enables and disables the collection of metrics.**ControlMetrics** is used to control the collection of each type of metric for a [**CIM\_ManagedElement**](cim-managedelement.md), the collection of a given type of metric for all managed elements, or the collection of a specific metric for a specific managed element.

## Syntax


```mof
uint32 ControlMetrics(
  [in] CIM_ManagedElement       REF Subject,
  [in] CIM_BaseMetricDefinition REF Definition,
  [in] uint16                       MetricCollectionEnabled
);
```



## Parameters

<dl> <dt>

*Subject* \[in\]
</dt> <dd>

A [**CIM\_ManagedElement**](cim-managedelement.md) that identifies managed element(s) for which metrics will be controlled.

</dd> <dt>

*Definition* \[in\]
</dt> <dd>

Identifies a [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md) for which metrics will be controlled.

</dd> <dt>

*MetricCollectionEnabled* \[in\]
</dt> <dd>

Indicates the desired operation to perform on the metrics.

<dt>

<span id="Enable"></span><span id="enable"></span><span id="ENABLE"></span>

**Enable** (2)


</dt> <dd></dd> <dt>

<span id="Disable"></span><span id="disable"></span><span id="DISABLE"></span>

**Disable** (3)


</dt> <dd></dd> <dt>

<span id="Reset"></span><span id="reset"></span><span id="RESET"></span>

**Reset** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (..)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved** (32768..65535)


</dt> <dd></dd> </dl> </dd> </dl>

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

 

 




