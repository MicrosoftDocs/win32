---
description: Used to control the collection of metrics for a managed element or elements.
ms.assetid: 3DC043ED-A790-4322-BF80-55961E9946C2
title: ControlMetrics method of the Msvm_MetricService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_MetricService.ControlMetrics
api_type: 
- COM
api_location: 
- vmms.exe
---

# ControlMetrics method of the Msvm\_MetricService class

Used to control the collection of metrics for a managed element or elements.

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

A [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement) instance that identifies the managed elements for which metrics will be collected. If this parameter is **Null**, the metrics for all the managed elements associated with the *Definition* parameter will be collected.

</dd> <dt>

*Definition* \[in\]
</dt> <dd>

An [**Msvm\_BaseMetricDefinition**](msvm-basemetricdefinition.md) instance that specifies which metrics will be collected. If this parameter is **Null**, the metrics for all the definitions associated with the managed element identified by the *Subject* parameter will be collected

</dd> <dt>

*MetricCollectionEnabled* \[in\]
</dt> <dd>

Specifies the operation to perform on the metrics collection. This must be one of the following values.

<dt>

<span id="Enable"></span><span id="enable"></span><span id="ENABLE"></span>

<span id="Enable"></span><span id="enable"></span><span id="ENABLE"></span>**Enable** (2)


</dt> <dd>

Enable metrics collection.

</dd> <dt>

<span id="Disable"></span><span id="disable"></span><span id="DISABLE"></span>

<span id="Disable"></span><span id="disable"></span><span id="DISABLE"></span>**Disable** (3)


</dt> <dd>

Disable metrics collection.

</dd> <dt>

<span id="Reset"></span><span id="reset"></span><span id="RESET"></span>

<span id="Reset"></span><span id="reset"></span><span id="RESET"></span>**Reset** (4)


</dt> <dd>

Reset metrics values.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (..)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved** (32768..65535)


</dt> <dd></dd> </dl> </dd> </dl>

## Return value

This method returns one of the following values.

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

## Remarks

This method will fail in the following instances:

-   The *Subject* and *Definition* parameters are both **Null**.
-   The *Subject* and *Definition* parameters are both non-**Null** and there is not an instance of [**Msvm\_MetricDefForME**](msvm-metricdefforme.md) that associates the two instances.
-   The *Definition* parameter is a reference to an instance of [**Msvm\_BaseMetricDefinition**](msvm-basemetricdefinition.md) that is not associated with the [**Msvm\_MetricService**](msvm-metricservice.md) through [**Msvm\_ServiceAffectsElement**](msvm-serviceaffectselement.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_MetricService**](msvm-metricservice.md)
</dt> </dl>

 

