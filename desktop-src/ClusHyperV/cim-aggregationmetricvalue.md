---
title: CIM\_AggregationMetricValue class
description: Represents the instance value of a metric defined by an instance of CIM\_AggregationMetricDefinition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '64d67945-651f-4695-a0df-bba38d3d61e5'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_AggregationMetricValue class", "CIM_AggregationMetricValue class, described"]
topic_type:
- apiref
api_name:
- CIM_AggregationMetricValue
- CIM_AggregationMetricValue.Caption
- CIM_AggregationMetricValue.Description
- CIM_AggregationMetricValue.ElementName
- CIM_AggregationMetricValue.InstanceID
- CIM_AggregationMetricValue.MetricDefinitionId
- CIM_AggregationMetricValue.MeasuredElementName
- CIM_AggregationMetricValue.TimeStamp
- CIM_AggregationMetricValue.Duration
- CIM_AggregationMetricValue.MetricValue
- CIM_AggregationMetricValue.BreakdownDimension
- CIM_AggregationMetricValue.BreakdownValue
- CIM_AggregationMetricValue.Volatile
- CIM_AggregationMetricValue.AggregationTimeStamp
- CIM_AggregationMetricValue.AggregationDuration
api_location:
- VMMS.exe
api_type:
- DllExport
---

# CIM\_AggregationMetricValue class

Represents the instance value of a metric defined by an instance of **CIM\_AggregationMetricDefinition**.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.22.0"), UMLPackagePath("CIM::Metrics::BaseMetric")]
class CIM_AggregationMetricValue : CIM_BaseMetricValue
{
  string   Caption;
  string   Description;
  string   ElementName;
  string   InstanceID;
  string   MetricDefinitionId;
  string   MeasuredElementName;
  datetime TimeStamp;
  datetime Duration;
  string   MetricValue;
  string   BreakdownDimension;
  string   BreakdownValue;
  boolean  Volatile;
  datetime AggregationTimeStamp;
  datetime AggregationDuration;
};
```

## Members

The **CIM\_AggregationMetricValue** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_AggregationMetricValue** class has these properties.

<dl> <dt>

**AggregationDuration**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_AggregationMetricValue**.**AggregationTimeStamp**")
</dt> </dl>

Represents the time duration over which the aggregation was computed. The start of a monitoring interval over which the aggregation function is applied is determined by subtracting the **AggregationDuration** value from the **AggregationTimestamp** value.

</dd> <dt>

**AggregationTimeStamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_AggregationMetricValue**.**Duration**")
</dt> </dl>

The time when the aggregation function was applied to determine the value of the metric instance. This is different from the time when the instance is created. The **AggregationTimeStamp** value changes whenever the aggregation function is applied to calculate the value.

</dd> <dt>

**BreakdownDimension**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The dimension for which this set of metric values is broken down based on **BreakdownDimensions** property of the associated [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md) object.

This property is inherited from [**CIM\_BaseMetricValue**](cim-basemetricvalue.md).

</dd> <dt>

**BreakdownValue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The value of the **BreakdownDimension** property defined for this instance value. For example, if **BreakdownDimension** contains "TransactionName", this property could name the actual transaction to which this particular metric value applies.

This property is inherited from [**CIM\_BaseMetricValue**](cim-basemetricvalue.md).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Duration**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md).**TimeScope**", "[**CIM\_BaseMetricValue**](cim-basemetricvalue.md).**TimeStamp**")
</dt> </dl>

The time duration over which this metric value is valid. This property should not exist for time stamps that only apply to a point in time, but should be defined for values that are considered valid for a certain time period (ex. sampling). If the **Duration** property exists and is non-Null, the **TimeStamp** value should be the end of the interval.

This property is inherited from [**CIM\_BaseMetricValue**](cim-basemetricvalue.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Uniquely identifies an instance of this class within the scope of the containing namespace.

> \[!Important\]
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

 

This property is inherited from [**CIM\_BaseMetricValue**](cim-basemetricvalue.md).

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

This property is inherited from [**CIM\_BaseMetricValue**](cim-basemetricvalue.md).

</dd> <dt>

**MetricDefinitionId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md).**Id**")
</dt> </dl>

The key of the [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md) instance that is associated with this instance value.

This property is inherited from [**CIM\_BaseMetricValue**](cim-basemetricvalue.md).

</dd> <dt>

**MetricValue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A string representation of the metric value. The original data type of the metric value is specified in the associated [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md) object.

This property is inherited from [**CIM\_BaseMetricValue**](cim-basemetricvalue.md).

</dd> <dt>

**TimeStamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md).**TimeScope**", "[**CIM\_BaseMetricValue**](cim-basemetricvalue.md).**Duration**")
</dt> </dl>

The time when the value of a metric instance is computed. This is different from the time when the instance is created. If the **Volatile** property is true, this value changes whenever a new measurement snapshot is taken.

A management application may establish a time series of metric data by retrieving the instances of [**CIM\_BaseMetricValue**](cim-basemetricvalue.md) and sorting them according to their **TimeStamp** value.

This property is inherited from [**CIM\_BaseMetricValue**](cim-basemetricvalue.md).

</dd> <dt>

**Volatile**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the **TimeStamp** value changes whenever the value of the metric instance changes. False if this object must remain unchanged and a new object created for the new **TimeStamp** value.

This property is inherited from [**CIM\_BaseMetricValue**](cim-basemetricvalue.md).

</dd> </dl>

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

[**CIM\_BaseMetricValue**](cim-basemetricvalue.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





