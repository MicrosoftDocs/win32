---
description: Shows the specified metrics.
ms.assetid: 3716b5e6-b360-4719-a0f3-60b8d39deb31
title: ShowMetrics method of the Msvm_MetricService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_MetricService.ShowMetrics
api_type: 
- COM
api_location: 
- vmms.exe
---

# ShowMetrics method of the Msvm\_MetricService class

Shows the specified metrics.

## Syntax


```mof
uint32 ShowMetrics(
  [in]  CIM_ManagedElement       REF Subject,
  [in]  CIM_BaseMetricDefinition REF Definition,
  [out] CIM_ManagedElement       REF ManagedElements[],
  [out] CIM_BaseMetricDefinition REF DefinitionList[],
  [out] string                       MetricNames[],
  [out] uint16                       MetricCollectionEnabled[]
);
```



## Parameters

<dl> <dt>

*Subject* \[in\]
</dt> <dd>

The Subject parameter identifies an instance of [**CIM\_ManagedElement**](cim-managedelement.md) for which the method returns references to instances of [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md) that define metrics that are being captured for the **CIM\_ManagedElement**.

</dd> <dt>

*Definition* \[in\]
</dt> <dd>

The Definition parameter identifies an instance of [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md). The method returns references to instances of [**CIM\_ManagedElement**](cim-managedelement.md) for which metrics defined by the instance of **CIM\_BaseMetricDefinition** are available to be collected.

</dd> <dt>

*ManagedElements* \[out\]
</dt> <dd>

Upon successful completion of the method, the *ManagedElements*\[\] parameter may contain references to [**CIM\_ManagedElement**](cim-managedelement.md) for which the metric identified by *Definition* parameter is available for collection.

</dd> <dt>

*DefinitionList* \[out\]
</dt> <dd>

Upon successful completion of the method, the *DefinitionList* parameter may contain references to instances of [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md) that define metrics available for collection for the [**CIM\_ManagedElement**](cim-managedelement.md) identified by the *Subject* parameter.

</dd> <dt>

*MetricNames* \[out\]
</dt> <dd>

Upon successful completion of the method, each array index of the *MetricNames* parameter shall contain the value of the Name property for the instance of [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md) referenced by the corresponding array index of the *DefinitionList* parameter.

</dd> <dt>

*MetricCollectionEnabled* \[out\]
</dt> <dd>

The *MetricCollectionEnabled* parameter indicates whether a metric is being collected for a managed element.

<dt>

<span id="Enable"></span><span id="enable"></span><span id="ENABLE"></span>

**Enable** (2)


</dt> <dd></dd> <dt>

<span id="Disable"></span><span id="disable"></span><span id="DISABLE"></span>

**Disable** (3)


</dt> <dd></dd> <dt>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>

**Reserved** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (..)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved** (32768..65535)


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

[**Msvm\_MetricService**](msvm-metricservice.md)
</dt> </dl>

 

 




