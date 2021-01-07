---
description: Describes the capabilities of a CIM\_MetricService object.
ms.assetid: 3b4da02f-5298-46d4-876c-404baca38c03
title: CIM_MetricServiceCapabilities class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_MetricServiceCapabilities
- CIM_MetricServiceCapabilities.ControllableMetrics
- CIM_MetricServiceCapabilities.MetricsControlTypes
- CIM_MetricServiceCapabilities.ControllableManagedElements
- CIM_MetricServiceCapabilities.ManagedElementControlTypes
- CIM_MetricServiceCapabilities.SupportedMethods
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_MetricServiceCapabilities class

Describes the capabilities of a [**CIM\_MetricService**](cim-metricservice.md) object.

## Syntax

``` syntax
[Abstract, Version("2.22.0"), UMLPackagePath("CIM::Metrics::BaseMetrics"), AMENDMENT]
class CIM_MetricServiceCapabilities : CIM_EnabledLogicalElementCapabilities
{
  string ControllableMetrics[];
  uint16 MetricsControlTypes[];
  string ControllableManagedElements[];
  uint16 ManagedElementControlTypes[];
  uint16 SupportedMethods[];
};
```

## Members

The **CIM\_MetricServiceCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_MetricServiceCapabilities** class has these properties.

<dl> <dt>

**ControllableManagedElements**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_MetricServiceCapabilities**.**ManagedElementControlTypes**")
</dt> </dl>

An array that contains identifiers of the [**CIM\_ManagedElement**](cim-managedelement.md) instances that are controlled by the metric service. The identifiers must be formatted as Web-Based Enterprise Management (WBEM) URIs. In order to use this property, the metric service must support enabling or disabling at least one metric that is defined for the **CIM\_ManagedElement** instance.

</dd> <dt>

**ControllableMetrics**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_MetricServiceCapabilities**.**MetricControlTypes**")
</dt> </dl>

An array that contains identifiers of the [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md) that defines the metrics that are managed by the metric service. The identifiers must be formatted as Web-Based Enterprise Management (WBEM) URIs.

In order to use this property, a [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md) instance must be associated with a [**CIM\_MetricService**](cim-metricservice.md) instance through the [**CIM\_ServiceAffectsElement**](cim-serviceaffectselement.md) class. In addition the metric service must support enabling or disabling at least one metric that is defined by the **CIM\_BaseMetricDefinition** instance.

</dd> <dt>

**ManagedElementControlTypes**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_MetricServiceCapabilities**.**ControllableManagedElements**")
</dt> </dl>

An array that indicates the control types that are supported by the metric service for the managed elements in the **ControllableManagedElements** array. This array corresponds to the **ControllableManagedElements** array. The control types in this array are associated with metrics through the **ControllableManagedElements** array.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Discrete"></span><span id="discrete"></span><span id="DISCRETE"></span>

**Discrete** (2)


</dt> <dd></dd> <dt>

<span id="Bulk"></span><span id="bulk"></span><span id="BULK"></span>

**Bulk** (3)


</dt> <dd></dd> <dt>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>

**Both** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (..)


</dt> <dd></dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific** (32768..65535)


</dt> <dd></dd> </dl>

</dd> <dt>

**MetricsControlTypes**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_MetricServiceCapabilities**.**ControllableMetrics**")
</dt> </dl>

An array that indicates the control types that are supported by the metric service. This array corresponds to the **ControllableMetrics** array. The control types in this array are associated with metrics through the **ControllableMetrics** array.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Discrete"></span><span id="discrete"></span><span id="DISCRETE"></span>

**Discrete** (2)


</dt> <dd></dd> <dt>

<span id="Bulk"></span><span id="bulk"></span><span id="BULK"></span>

**Bulk** (3)


</dt> <dd></dd> <dt>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>

**Both** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (..)


</dt> <dd></dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific** (32768..65535)


</dt> <dd></dd> </dl>

</dd> <dt>

**SupportedMethods**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains names of methods that are supported by the metric service.

<dt>

<span id="ControlMetrics"></span><span id="controlmetrics"></span><span id="CONTROLMETRICS"></span>

**ControlMetrics** (2)


</dt> <dd></dd> <dt>

<span id="ControlMetricsByClass"></span><span id="controlmetricsbyclass"></span><span id="CONTROLMETRICSBYCLASS"></span>

**ControlMetricsByClass** (3)


</dt> <dd></dd> <dt>

<span id="ShowMetrics"></span><span id="showmetrics"></span><span id="SHOWMETRICS"></span>

**ShowMetrics** (4)


</dt> <dd></dd> <dt>

<span id="ShowMetricsByClass"></span><span id="showmetricsbyclass"></span><span id="SHOWMETRICSBYCLASS"></span>

**ShowMetricsByClass** (5)


</dt> <dd></dd> <dt>

<span id="GetMetricValues"></span><span id="getmetricvalues"></span><span id="GETMETRICVALUES"></span>

**GetMetricValues** (6)


</dt> <dd></dd> <dt>

<span id="ControlSampleTimes"></span><span id="controlsampletimes"></span><span id="CONTROLSAMPLETIMES"></span>

**ControlSampleTimes** (7)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (..)


</dt> <dd></dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific** (0x8000..)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_EnabledLogicalElementCapabilities**](cim-enabledlogicalelementcapabilities.md)
</dt> </dl>

 

