---
title: CIM\_AggregationMetricDefinition class
description: Represents the definition of a metric that is derived from another metric value. A CIM\_AggregationMetricDefinition object should be associated with the CIM\_ManagedElement objects to which it applies.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3a91e5c2-aa88-47a4-9274-f1ef06211aea
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_AggregationMetricDefinition class
- CIM_AggregationMetricDefinition class, described
topic_type:
- apiref
api_name:
- CIM_AggregationMetricDefinition
- CIM_AggregationMetricDefinition.InstanceID
- CIM_AggregationMetricDefinition.Caption
- CIM_AggregationMetricDefinition.Description
- CIM_AggregationMetricDefinition.ElementName
- CIM_AggregationMetricDefinition.Id
- CIM_AggregationMetricDefinition.Name
- CIM_AggregationMetricDefinition.DataType
- CIM_AggregationMetricDefinition.Calculable
- CIM_AggregationMetricDefinition.Units
- CIM_AggregationMetricDefinition.BreakdownDimensions
- CIM_AggregationMetricDefinition.IsContinuous
- CIM_AggregationMetricDefinition.TimeScope
- CIM_AggregationMetricDefinition.GatheringType
- CIM_AggregationMetricDefinition.ProgrammaticUnits
- CIM_AggregationMetricDefinition.ChangeType
- CIM_AggregationMetricDefinition.SimpleFunction
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_AggregationMetricDefinition class

Represents the definition of a metric that is derived from another metric value. A **CIM\_AggregationMetricDefinition** object should be associated with the **CIM\_ManagedElement** objects to which it applies.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.22.0"), UMLPackagePath("CIM::Metrics::BaseMetric")]
class CIM_AggregationMetricDefinition : CIM_BaseMetricDefinition
{
  string  InstanceID;
  string  Caption;
  string  Description;
  string  ElementName;
  string  Id;
  string  Name;
  uint16  DataType;
  uint16  Calculable;
  string  Units;
  string  BreakdownDimensions[];
  boolean IsContinuous;
  uint16  TimeScope;
  uint16  GatheringType;
  string  ProgrammaticUnits;
  uint16  ChangeType = 5;
  uint16  SimpleFunction;
};
```

## Members

The **CIM\_AggregationMetricDefinition** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_AggregationMetricDefinition** class has these properties.

<dl> <dt>

**BreakdownDimensions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains free format strings that can be used to break down queries of [**CIM\_BaseMetricValue**](cim-basemetricvalue.md) objects along a certain dimension. The strings should be meaningful to the end users of the metric data. In addition, the strings should indicate which break down dimensions are supported for the metric definition, by the underlying instrumentation.

An example is a transaction name that allows the break down of the total value for all transactions into a set of values, one for each transaction name. Other examples are an application system, or a user group name.

This property is inherited from [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md).

</dd> <dt>

**Calculable**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The characteristics of the metric used to perform calculations.

This property is inherited from [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md).

<dt>

<span id="Non-calculable"></span><span id="non-calculable"></span><span id="NON-CALCULABLE"></span>

<span id="Non-calculable"></span><span id="non-calculable"></span><span id="NON-CALCULABLE"></span>**Non-calculable** (1)


</dt> <dd>

The value can not be used to create a sum of values.

</dd> <dt>

<span id="Summable"></span><span id="summable"></span><span id="SUMMABLE"></span>

<span id="Summable"></span><span id="summable"></span><span id="SUMMABLE"></span>**Summable** (2)


</dt> <dd>

The value can be used to create a sum of values.

</dd> <dt>

<span id="Non-summable"></span><span id="non-summable"></span><span id="NON-SUMMABLE"></span>

<span id="Non-summable"></span><span id="non-summable"></span><span id="NON-SUMMABLE"></span>**Non-summable** (3)


</dt> <dd>

The value should not be used to create a sum of values.

</dd> </dl>

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

**ChangeType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("ChangeType"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_AggregationMetricDefinition**.**IsContinuous**")
</dt> </dl>

Indicates how the metric value changes using common attributes such as direction change, minimum and maximum values, and wrapping semantics.

<dt>

<span id="Simple_Function"></span><span id="simple_function"></span><span id="SIMPLE_FUNCTION"></span>

<span id="Simple_Function"></span><span id="simple_function"></span><span id="SIMPLE_FUNCTION"></span>**Simple Function** (5)


</dt> <dd>

The derived metric value is calculated by applying the basic mathematical function identified by the **SimpleFunction** property to the underlying metric values.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved.

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd>

Reserved.

</dd> </dl>

</dd> <dt>

**DataType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The data type of the metric.

This property is inherited from [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md).

<dt>

<span id="boolean"></span><span id="BOOLEAN"></span>

**boolean** (1)


</dt> <dd></dd> <dt>

<span id="char16"></span><span id="CHAR16"></span>

**char16** (2)


</dt> <dd></dd> <dt>

<span id="datetime"></span><span id="DATETIME"></span>

**datetime** (3)


</dt> <dd></dd> <dt>

<span id="real32"></span><span id="REAL32"></span>

**real32** (4)


</dt> <dd></dd> <dt>

<span id="real64"></span><span id="REAL64"></span>

**real64** (5)


</dt> <dd></dd> <dt>

<span id="sint16"></span><span id="SINT16"></span>

**sint16** (6)


</dt> <dd></dd> <dt>

<span id="sint32"></span><span id="SINT32"></span>

**sint32** (7)


</dt> <dd></dd> <dt>

<span id="sint64"></span><span id="SINT64"></span>

**sint64** (8)


</dt> <dd></dd> <dt>

<span id="sint8"></span><span id="SINT8"></span>

**sint8** (9)


</dt> <dd></dd> <dt>

<span id="string"></span><span id="STRING"></span>

**string** (10)


</dt> <dd></dd> <dt>

<span id="uint16"></span><span id="UINT16"></span>

**uint16** (11)


</dt> <dd></dd> <dt>

<span id="uint32"></span><span id="UINT32"></span>

**uint32** (12)


</dt> <dd></dd> <dt>

<span id="uint64"></span><span id="UINT64"></span>

**uint64** (13)


</dt> <dd></dd> <dt>

<span id="uint8"></span><span id="UINT8"></span>

**uint8** (14)


</dt> <dd></dd> </dl>

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

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**GatheringType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates how the metric values are gathered by the underlying instrumentation.

This property is inherited from [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

The gathering type is not known.

</dd> <dt>

<span id="OnChange"></span><span id="onchange"></span><span id="ONCHANGE"></span>

<span id="OnChange"></span><span id="onchange"></span><span id="ONCHANGE"></span>**OnChange** (2)


</dt> <dd>

CIM metric values get updated immediately when the values inside measured resource change. Metric of this gathering type reflect the data of a resource at any time. An example is the number of logged on users that gets updated immediately as users log on and off of a system.

</dd> <dt>

<span id="Periodic"></span><span id="periodic"></span><span id="PERIODIC"></span>

<span id="Periodic"></span><span id="periodic"></span><span id="PERIODIC"></span>**Periodic** (3)


</dt> <dd>

CIM metric values get updated periodically. For instance, to a client application, a metric value applying to the current time will appear constant during each gathering interval, and then jumps to the new value at the end of each gathering interval.

</dd> <dt>

<span id="OnRequest"></span><span id="onrequest"></span><span id="ONREQUEST"></span>

<span id="OnRequest"></span><span id="onrequest"></span><span id="ONREQUEST"></span>**OnRequest** (4)


</dt> <dd>

The CIM metric value is determined each time a client application reads it. Metrics of this gathering type retrieve data that might only be accurate during the request.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved.

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd>

Reserved.

</dd> </dl>

</dd> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The unique ID of the metric definition. Open Software Foundation (OSF) UUID/GUIDs are recommended.

This property is inherited from [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Uniquely and opaquely identifies an instance of this class within the scope of the containing namespace.

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

 

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**IsContinuous**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the metric value is continuous; otherwise, false.

This property is inherited from [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the metric. This name does not have to be unique, but should be descriptive and may contain blank spaces.

This property is inherited from [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md).

</dd> <dt>

**ProgrammaticUnits**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The specific units of a value. The value of this property should be a legal value of the Programmatic Units qualifier as defined in Appendix C.1 of DSP0004 V2.4 or later.

This property is inherited from [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md).

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

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved.

</dd> <dt>

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

The metric reports the modal value of the underlying metric values.

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd>

Reserved.

</dd> </dl>

</dd> <dt>

**TimeScope**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_BaseMetricValue**](cim-basemetricvalue.md).**TimeStamp**", "**CIM\_BaseMetricValue**.**Duration**")
</dt> </dl>

The time scope that applies to the metric designer.

This property is inherited from [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

The time scope was not qualified by the metric designer, or is unknown to the provider.

</dd> <dt>

<span id="Point"></span><span id="point"></span><span id="POINT"></span>

<span id="Point"></span><span id="point"></span><span id="POINT"></span>**Point** (2)


</dt> <dd>

The metric applies to a point in time. For corresponding [**CIM\_BaseMetricValue**](cim-basemetricvalue.md) instances, the **TimeStamp** property specifies the point in time, and the **Duration** property contains "0".

</dd> <dt>

<span id="Interval"></span><span id="interval"></span><span id="INTERVAL"></span>

<span id="Interval"></span><span id="interval"></span><span id="INTERVAL"></span>**Interval** (3)


</dt> <dd>

The metric applies to a time interval. For corresponding [**CIM\_BaseMetricValue**](cim-basemetricvalue.md) instances, the **TimeStamp** property specifies the end of the time interval, and **Duration** property specifies the duration of the time interval.

</dd> <dt>

<span id="StartupInterval"></span><span id="startupinterval"></span><span id="STARTUPINTERVAL"></span>

<span id="StartupInterval"></span><span id="startupinterval"></span><span id="STARTUPINTERVAL"></span>**StartupInterval** (4)


</dt> <dd>

The metric applies to a time interval that began at the startup of the measured resource, such as a [**CIM\_ManagedElement**](cim-managedelement.md) that is associated with a metric using the [**CIM\_MetricDefForME**](cim-metricdefforme.md) class.

For corresponding [**CIM\_BaseMetricValue**](cim-basemetricvalue.md) instances, **TimeStamp** property specifies the end of the time interval. If the **Duration** property is "0", this indicates that the startup time of the measured resource is unknown. Otherwise, **Duration** specifies the duration between the startup time of the resource and **TimeStamp** value.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved.

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd>

Reserved.

</dd> </dl>

</dd> <dt>

**Units**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The units of the metric. Examples are bytes, packets, jobs, files, milliseconds, and amps.

This property is inherited from [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





