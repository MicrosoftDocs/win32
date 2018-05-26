---
title: CIM\_MetricServiceCapabilities class
description: Describes the capabilities of a CIM\_MetricService object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7fcfd8b3-e895-4b35-b16c-b7d632e1d279
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_MetricServiceCapabilities class
- CIM_MetricServiceCapabilities class, described
topic_type:
- apiref
api_name:
- CIM_MetricServiceCapabilities
- CIM_MetricServiceCapabilities.Caption
- CIM_MetricServiceCapabilities.Description
- CIM_MetricServiceCapabilities.InstanceID
- CIM_MetricServiceCapabilities.ElementName
- CIM_MetricServiceCapabilities.ElementNameEditSupported
- CIM_MetricServiceCapabilities.MaxElementNameLen
- CIM_MetricServiceCapabilities.RequestedStatesSupported
- CIM_MetricServiceCapabilities.ElementNameMask
- CIM_MetricServiceCapabilities.ControllableMetrics
- CIM_MetricServiceCapabilities.MetricsControlTypes
- CIM_MetricServiceCapabilities.ControllableManagedElements
- CIM_MetricServiceCapabilities.ManagedElementControlTypes
- CIM_MetricServiceCapabilities.SupportedMethods
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_MetricServiceCapabilities class

Describes the capabilities of a [**CIM\_MetricService**](cim-metricservice.md) object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.22.0"), UMLPackagePath("CIM::Metrics::BaseMetrics")]
class CIM_MetricServiceCapabilities : CIM_EnabledLogicalElementCapabilities
{
  string  Caption;
  string  Description;
  string  InstanceID;
  string  ElementName;
  boolean ElementNameEditSupported;
  uint16  MaxElementNameLen;
  uint16  RequestedStatesSupported[];
  string  ElementNameMask;
  string  ControllableMetrics[];
  uint16  MetricsControlTypes[];
  string  ControllableManagedElements[];
  uint16  ManagedElementControlTypes[];
  uint16  SupportedMethods[];
};
```

## Members

The **CIM\_MetricServiceCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_MetricServiceCapabilities** class has these properties.

<dl> <dt>

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

**ControllableManagedElements**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_MetricServiceCapabilities**.**ManagedElementControlTypes**")
</dt> </dl>

An array that contains identifiers of the [**CIM\_ManagedElement**](cim-managedelement.md) instances that are controlled by the metric service. The identifiers must be formatted as Web-Based Enterprise Management (WBEM) URIs. In order to use this property, the metric service must support enabling or disabling at least one metric that is defined for the **CIM\_ManagedElement** instance.

</dd> <dt>

**ControllableMetrics**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_MetricServiceCapabilities**.**MetricControlTypes**")
</dt> </dl>

An array that contains identifiers of the [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md) that defines the metrics that are managed by the metric service. The identifiers must be formatted as Web-Based Enterprise Management (WBEM) URIs.

In order to use this property, a [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md) instance must be associated with a [**CIM\_MetricService**](cim-metricservice.md) instance through the [**CIM\_ServiceAffectsElement**](cim-serviceaffectselement.md) class. In addition the metric service must support enabling or disabling at least one metric that is defined by the **CIM\_BaseMetricDefinition** instance.

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
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The user friendly name for this class instance. In addition, the user friendly name can be used as a index property for a query. This value does not have to be unique within its namespace.

This property is inherited from [**CIM\_Capabilities**](cim-capabilities.md).

</dd> <dt>

**ElementNameEditSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("FC-SWAPI.INCITS-T11\|SWAPI\_UNIT\_CONFIG\_CAPS\_T\|EditName"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedElement**](cim-managedelement.md).**ElementName**")
</dt> </dl>

**true** if the **ElementName** property of the enabled logical element can be modified; otherwise, **false**.

This property is inherited from [**CIM\_EnabledLogicalElementCapabilities**](cim-enabledlogicalelementcapabilities.md).

</dd> <dt>

**ElementNameMask**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElementCapabilities**](cim-enabledlogicalelementcapabilities.md).**MaxElementNameLen**")
</dt> </dl>

A regular expression that indicates the restrictions on the **ElementalName** property of the enable logical element. See *DMTF standard ABNF with the Management Profile Specification Usage Guide*, appendix C for the permitted syntax.

> [!Note]  
> If this property and the **ElementalNameMask** property of the enable logical element describe the maximum length of **ElementalName**, the smaller value is used.

 

This property is inherited from [**CIM\_EnabledLogicalElementCapabilities**](cim-enabledlogicalelementcapabilities.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
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

 

This property is inherited from [**CIM\_Capabilities**](cim-capabilities.md).

</dd> <dt>

**ManagedElementControlTypes**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_MetricServiceCapabilities**.**ControllableManagedElements**")
</dt> </dl>

An array that indicates the control types that are supported by the metric service for the managed elements in the **ControllableManagedElements** array. This array corresponds to the **ControllableManagedElements** array. The control types in this array are associated with metrics through the **ControllableManagedElements** array.

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Discrete"></span><span id="discrete"></span><span id="DISCRETE"></span>

<span id="Discrete"></span><span id="discrete"></span><span id="DISCRETE"></span>**Discrete** (2)


</dt> <dd>

The metrics service can enable and disable the associated metrics individually.

</dd> <dt>

<span id="Bulk"></span><span id="bulk"></span><span id="BULK"></span>

<span id="Bulk"></span><span id="bulk"></span><span id="BULK"></span>**Bulk** (3)


</dt> <dd>

The metrics service can enable and disable all associated metrics with a single operation.

</dd> <dt>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>**Both** (4)


</dt> <dd>

The metrics service can enable and disable the associated metrics individually, and with a single operation.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd></dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific**


</dt> <dd></dd> </dl>

</dd> <dt>

**MaxElementNameLen**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (256), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("FC-SWAPI.INCITS-T11\|SWAPI\_UNIT\_CONFIG\_CAPS\_T\|MaxNameChars"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_FCSwitchCapabilities.ElementNameEditSupported", "[**CIM\_EnabledLogicalElementCapabilities**](cim-enabledlogicalelementcapabilities.md).**ElementNameMask**")
</dt> </dl>

The maximum supported length of the **ElementName** property of the enabled logical element.

This property is inherited from [**CIM\_EnabledLogicalElementCapabilities**](cim-enabledlogicalelementcapabilities.md).

</dd> <dt>

**MetricsControlTypes**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_MetricServiceCapabilities**.**ControllableMetrics**")
</dt> </dl>

An array that indicates the control types that are supported by the metric service. This array corresponds to the **ControllableMetrics** array. The control types in this array are associated with metrics through the **ControllableMetrics** array.

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Discrete"></span><span id="discrete"></span><span id="DISCRETE"></span>

<span id="Discrete"></span><span id="discrete"></span><span id="DISCRETE"></span>**Discrete** (2)


</dt> <dd>

The metrics service can enable and disable the associated metrics individually.

</dd> <dt>

<span id="Bulk"></span><span id="bulk"></span><span id="BULK"></span>

<span id="Bulk"></span><span id="bulk"></span><span id="BULK"></span>**Bulk** (3)


</dt> <dd>

The metrics service can enable and disable all associated metrics with a single operation.

</dd> <dt>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>**Both** (4)


</dt> <dd>

The metrics service can enable and disable the associated metrics individually, and with a single operation.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd></dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific**


</dt> <dd></dd> </dl>

</dd> <dt>

**RequestedStatesSupported**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**RequestStateChange**")
</dt> </dl>

The possible states that can be requested on the enabled logical element by the [**RequestStateChange**](cim-enabledlogicalelement-requeststatechange.md) method.

This property is inherited from [**CIM\_EnabledLogicalElementCapabilities**](cim-enabledlogicalelementcapabilities.md).

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> <dt>

<span id="Shut_Down"></span><span id="shut_down"></span><span id="SHUT_DOWN"></span>

**Shut Down** (4)


</dt> <dd></dd> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>

**Offline** (6)


</dt> <dd></dd> <dt>

<span id="Test"></span><span id="test"></span><span id="TEST"></span>

**Test** (7)


</dt> <dd></dd> <dt>

<span id="Defer"></span><span id="defer"></span><span id="DEFER"></span>

**Defer** (8)


</dt> <dd></dd> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>

**Quiesce** (9)


</dt> <dd></dd> <dt>

<span id="Reboot"></span><span id="reboot"></span><span id="REBOOT"></span>

**Reboot** (10)


</dt> <dd></dd> <dt>

<span id="Reset"></span><span id="reset"></span><span id="RESET"></span>

**Reset** (11)


</dt> <dd></dd> </dl>

</dd> <dt>

**SupportedMethods**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains names of methods that are supported by the metric service.

The possible values are:

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

**DMTF Reserved**


</dt> <dd>8 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl>

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

[**CIM\_EnabledLogicalElementCapabilities**](cim-enabledlogicalelementcapabilities.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





