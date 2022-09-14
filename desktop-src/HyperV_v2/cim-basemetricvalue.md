---
description: Represents the instance value of a metric.
ms.assetid: 6b272ae8-7684-45bb-bff8-6559680cc8b6
title: CIM_BaseMetricValue class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_BaseMetricValue
- CIM_BaseMetricValue.InstanceID
- CIM_BaseMetricValue.MetricDefinitionId
- CIM_BaseMetricValue.MeasuredElementName
- CIM_BaseMetricValue.TimeStamp
- CIM_BaseMetricValue.Duration
- CIM_BaseMetricValue.MetricValue
- CIM_BaseMetricValue.BreakdownDimension
- CIM_BaseMetricValue.BreakdownValue
- CIM_BaseMetricValue.Volatile
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_BaseMetricValue class

Represents the instance value of a metric.

## Syntax

``` syntax
[Abstract, Version("2.19.0"), UMLPackagePath("CIM::Metrics::BaseMetric"), AMENDMENT]
class CIM_BaseMetricValue : CIM_ManagedElement
{
  string   InstanceID;
  string   MetricDefinitionId;
  string   MeasuredElementName;
  datetime TimeStamp;
  datetime Duration;
  string   MetricValue;
  string   BreakdownDimension;
  string   BreakdownValue;
  boolean  Volatile;
};
```

## Members

The **CIM\_BaseMetricValue** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_BaseMetricValue** class has these properties.

<dl> <dt>

**BreakdownDimension**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The dimension for which this set of metric values is broken down based on **BreakdownDimensions** property of the associated [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md) object.

</dd> <dt>

**BreakdownValue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The value of the **BreakdownDimension** property defined for this instance value. For example, if **BreakdownDimension** contains "TransactionName", this property could name the actual transaction to which this particular metric value applies.

</dd> <dt>

**Duration**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md).**TimeScope**", "**CIM\_BaseMetricValue**.**TimeStamp**")
</dt> </dl>

The time duration over which this metric value is valid. This property should not exist for time stamps that only apply to a point in time, but should be defined for values that are considered valid for a certain time period (ex. sampling). If the **Duration** property exists and is non-Null, the **TimeStamp** value should be the end of the interval.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("InstanceID")
</dt> </dl>

Uniquely identifies an instance of this class within the scope of the containing namespace.

> [!IMPORTANT]
>
> In order to ensure uniqueness within the namespace, the value of the **InstanceID** property should be constructed in the following pattern: *OrgID*:*LocalID*
>
> *OrgID* must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity that defines the **InstanceID**, or be a registered ID that is assigned by a recognized global authority. This pattern is similar to the structure of schema class names. In addition, to ensure uniqueness, the first colon in **InstanceID** must be between the *OrgID* and*LocalID*. Therefore the *OrgID* must not contain a colon (':').
>
> *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
>
> If the above pattern is not used, the defining entity must assure that the resultant **InstanceID** value is not re-used across any **InstanceID** properties that are produced by this provider or other providers for this namespace.
>
> For Distributed Management Task Force (DMTF) defined instances, the pattern must be used with the *OrgID* set to CIM.

 

</dd> <dt>

**MeasuredElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A descriptive name for the element that is measure by the metric.

This property is required if the metric definition is not associated with a [**CIM\_ManagedElement**](cim-managedelement.md) object, and may be used in other cases to provide supplemental information. This allows metrics to be captured independent of any **CIM\_ManagedElement** object.

If there are multiple [**CIM\_ManagedElement**](cim-managedelement.md) objects associated with the metric value, then you can choose one of the managed elements to create the supplemental information for the metric. The property is not meant to be used as a foreign key to query the measured element. Instead, the association to the **CIM\_ManagedElement** should be used.

</dd> <dt>

**MetricDefinitionId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](/windows/desktop/WmiSdk/standard-qualifiers), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md).**Id**")
</dt> </dl>

The key of the [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md) instance that is associated with this instance value.

</dd> <dt>

**MetricValue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

A string representation of the metric value. The original data type of the metric value is specified in the associated [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md) object.

</dd> <dt>

**TimeStamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md).**TimeScope**", "**CIM\_BaseMetricValue**.**Duration**")
</dt> </dl>

The time when the value of a metric instance is computed. This is different from the time when the instance is created. If the **Volatile** property is true, this value changes whenever a new measurement snapshot is taken.

A management application may establish a time series of metric data by retrieving the instances of **CIM\_BaseMetricValue** and sorting them according to their **TimeStamp** value.

</dd> <dt>

**Volatile**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the **TimeStamp** value changes whenever the value of the metric instance changes. False if this object must remain unchanged and a new object created for the new **TimeStamp** value.

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

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> </dl>

 

