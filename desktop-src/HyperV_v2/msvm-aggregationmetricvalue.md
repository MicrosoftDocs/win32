---
description: Represents the instance value of a metric defined by an instance of the Msvm\_AggregationMetricDefinition class.
ms.assetid: 6dfcb711-6137-492a-aff4-82facbd11949
title: Msvm_AggregationMetricValue class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_AggregationMetricValue
- Msvm_AggregationMetricValue.InstanceID
- Msvm_AggregationMetricValue.Caption
- Msvm_AggregationMetricValue.Description
- Msvm_AggregationMetricValue.ElementName
- Msvm_AggregationMetricValue.MetricDefinitionId
- Msvm_AggregationMetricValue.MeasuredElementName
- Msvm_AggregationMetricValue.TimeStamp
- Msvm_AggregationMetricValue.Duration
- Msvm_AggregationMetricValue.MetricValue
- Msvm_AggregationMetricValue.BreakdownDimension
- Msvm_AggregationMetricValue.BreakdownValue
- Msvm_AggregationMetricValue.Volatile
- Msvm_AggregationMetricValue.AggregationTimeStamp
- Msvm_AggregationMetricValue.AggregationDuration
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_AggregationMetricValue class

Represents the instance value of a metric defined by an instance of the [**Msvm\_AggregationMetricDefinition**](msvm-aggregationmetricdefinition.md) class. The properties inherited from [**Msvm\_BaseMetricValue**](msvm-basemetricvalue.md) provide the actual metric value. The properties defined by this class provide information about the interval over which the aggregation function was applied.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_AggregationMetricValue : CIM_AggregationMetricValue
{
  string   InstanceID;
  string   Caption;
  string   Description;
  string   ElementName;
  string   MetricDefinitionId;
  string   MeasuredElementName;
  datetime TimeStamp;
  datetime Duration;
  string   MetricValue;
  string   BreakdownDimension;
  string   BreakdownValue;
  boolean  Volatile;
  datetime AggregationTimeStamp;
  datetime AggregationDuration;
};
```

## Members

The **Msvm\_AggregationMetricValue** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_AggregationMetricValue** class has these properties.

<dl> <dt>

**AggregationDuration**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Represents the time duration over which the aggregation was computed. The start of a monitoring interval over which the aggregation function is applied is determined by subtracting the **AggregationDuration** from the **AggregationTimeStamp**. This property is inherited from **CIM\_AggregationMetricValue**.

</dd> <dt>

**AggregationTimeStamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifies the time when the aggregation function was applied to determine the value of the metric instance. This is not the same as the time when the instance was created. For a given **CIM\_AggregationMetricValue** instance, the **AggregationTimeStamp** changes whenever the aggregation function is applied to calculate the value. This property is inherited from **CIM\_AggregationMetricValue**.

</dd> <dt>

**BreakdownDimension**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies one breakdown dimension from the **BreakdownDimensions** array defined in the associated [**Msvm\_BaseMetricDefinition**](msvm-basemetricdefinition.md). This is the dimension along which this set of metric values is broken down. This property is inherited from [**CIM\_BaseMetricDefinition**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**BreakdownValue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Defines a value of the **BreakdownDimension** property defined for this metric value instance. For example, if the **BreakdownDimension** is "TransactionName", this property could name the actual transaction to which this particular metric value applies. This property is inherited from [**CIM\_BaseMetricDefinition**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**Duration**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the time duration over which this metric value is valid. This property should not exist for time stamps that apply only to a point in time, but should be specified for values that are considered valid for a certain time period (for example, sampling). If the **Duration** property exists and is not **Null**, the **TimeStamp** property specifies the end of the interval. This property is inherited from [**CIM\_BaseMetricDefinition**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A display name for the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

A string that uniquely identifies an instance of this class. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**MeasuredElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A descriptive name for the element to which the metric value belongs (the measured element). This property is inherited from [**CIM\_BaseMetricDefinition**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**MetricDefinitionId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The key of the [**Msvm\_BaseMetricDefinition**](msvm-basemetricdefinition.md) instance for this value. This property is inherited from [**CIM\_BaseMetricDefinition**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**MetricValue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The value of the metric that is represented as a string. This property is inherited from [**CIM\_BaseMetricDefinition**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**TimeStamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the time when the metric value was captured or computed. Be aware that this is different from the time when the instance was created. This property is inherited from [**CIM\_BaseMetricDefinition**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**Volatile**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if the value for the next point in time will use the same class instance and just change the property values (such as the **Value** or **TimeStamp**). If **True**, the instance is reused. If **False**, the existing instances remain unchanged and a new instance is created for the new point in time. This property is inherited from [**CIM\_BaseMetricDefinition**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

