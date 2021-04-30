---
description: Represents the definition of a metric that is derived from another metric value. A CIM\_AggregationMetricDefinition object should be associated with the CIM\_ManagedElement objects to which it applies.
ms.assetid: 0059bfd6-ecf3-41f0-be6b-0ce46dfbbb18
title: CIM_AggregationMetricDefinition class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_AggregationMetricDefinition
- CIM_AggregationMetricDefinition.ChangeType
- CIM_AggregationMetricDefinition.SimpleFunction
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_AggregationMetricDefinition class

Represents the definition of a metric that is derived from another metric value. A **CIM\_AggregationMetricDefinition** object should be associated with the **CIM\_ManagedElement** objects to which it applies.

## Syntax

``` syntax
[Abstract, Version("2.22.0"), UMLPackagePath("CIM::Metrics::BaseMetric"), AMENDMENT]
class CIM_AggregationMetricDefinition : CIM_BaseMetricDefinition
{
  uint16 ChangeType = 5;
  uint16 SimpleFunction;
};
```

## Members

The **CIM\_AggregationMetricDefinition** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_AggregationMetricDefinition** class has these properties.

<dl> <dt>

**ChangeType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("ChangeType"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_AggregationMetricDefinition**.**IsContinuous**")
</dt> </dl>

Indicates how the metric value changes using common attributes such as direction change, minimum and maximum values, and wrapping semantics.

<dt>

<span id="Simple_Function"></span><span id="simple_function"></span><span id="SIMPLE_FUNCTION"></span>

**Simple Function** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (..)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved** (32768..65535)


</dt> <dd></dd> </dl>

</dd> <dt>

**SimpleFunction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The basic computation performed on an underlying metric to arrive at the value of this derived metric. This property is **NULL** when the **ChangeType** property has a value other than "5" (Simple Function).

<dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (..)


</dt> <dd></dd> <dt>

<span id="Minimum"></span><span id="minimum"></span><span id="MINIMUM"></span>

<span id="Minimum"></span><span id="minimum"></span><span id="MINIMUM"></span>**Minimum** (2)


</dt> <dd>

The metric reports the lowest value detected for the associated monitored entity. This is also known as a low watermark.

</dd> <dt>

<span id="Maximum"></span><span id="maximum"></span><span id="MAXIMUM"></span>

<span id="Maximum"></span><span id="maximum"></span><span id="MAXIMUM"></span>**Maximum** (3)


</dt> <dd>

The metric reports the maximum value detected for the associated monitored entity. This is also known as a high watermark.

</dd> <dt>

<span id="Average"></span><span id="average"></span><span id="AVERAGE"></span>

<span id="Average"></span><span id="average"></span><span id="AVERAGE"></span>**Average** (4)


</dt> <dd>

The metric reports the average value of the underlying metric values.

</dd> <dt>

<span id="Median"></span><span id="median"></span><span id="MEDIAN"></span>

<span id="Median"></span><span id="median"></span><span id="MEDIAN"></span>**Median** (5)


</dt> <dd>

The metric reports the median value of the underlying metric values.

</dd> <dt>

<span id="Mode"></span><span id="mode"></span><span id="MODE"></span>

<span id="Mode"></span><span id="mode"></span><span id="MODE"></span>**Mode** (6)


</dt> <dd>

the metric reports the modal value of the underlying metric values.

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved** (32768..65535)


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

[**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md)
</dt> </dl>

 

