---
description: Describes the capabilities of the associated Msvm\_MetricService instance.
ms.assetid: 4E24D675-8265-4B5E-9551-550510B138FE
title: Msvm_MetricServiceCapabilities class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_MetricServiceCapabilities
- Msvm_MetricServiceCapabilities.InstanceID
- Msvm_MetricServiceCapabilities.Caption
- Msvm_MetricServiceCapabilities.Description
- Msvm_MetricServiceCapabilities.ElementName
- Msvm_MetricServiceCapabilities.ElementNameEditSupported
- Msvm_MetricServiceCapabilities.MaxElementNameLen
- Msvm_MetricServiceCapabilities.RequestedStatesSupported
- Msvm_MetricServiceCapabilities.ElementNameMask
- Msvm_MetricServiceCapabilities.ControllableMetrics
- Msvm_MetricServiceCapabilities.MetricsControlTypes
- Msvm_MetricServiceCapabilities.ControllableManagedElements
- Msvm_MetricServiceCapabilities.ManagedElementControlTypes
- Msvm_MetricServiceCapabilities.SupportedMethods
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_MetricServiceCapabilities class

Describes the capabilities of the associated [**Msvm\_MetricService**](msvm-metricservice.md) instance.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_MetricServiceCapabilities : CIM_MetricServiceCapabilities
{
  string  InstanceID;
  string  Caption = "Hyper-V Metric Service Capabilities";
  string  Description = "Defines Hyper-V Metric Service Capabilities";
  string  ElementName = "Hyper-V Metric Service Capabilities";
  boolean ElementNameEditSupported;
  unit16  MaxElementNameLen;
  unit16  RequestedStatesSupported[];
  string  ElementNameMask;
  string  ControllableMetrics[];
  uint16  MetricsControlTypes[];
  string  ControllableManagedElements[];
  uint16  ManagedElementControlTypes[];
  uint16  SupportedMethods[];
};
```

## Members

The **Msvm\_MetricServiceCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_MetricServiceCapabilities** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement), and it is always set to "Hyper-V Metric Service Capabilities".

</dd> <dt>

**ControllableManagedElements**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ArrayType** ("Indexed")
</dt> </dl>

Identifies the instances of [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement) that can be controlled by the associated **CIM\_MetricService** instance. If this property is **Null**, all elements can be controlled. This property is inherited from **CIM\_MetricServiceCapabilities**.

</dd> <dt>

**ControllableMetrics**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ArrayType** ("Indexed")
</dt> </dl>

Identifies the instances of **CIM\_BaseMetricDefinition** that can be controlled by the associated **CIM\_MetricService** instance. If this property is **Null**, all metrics can be controlled. This property is inherited from **CIM\_MetricServiceCapabilities**.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement), and it is always set to "Defines Hyper-V Metric Service Capabilities".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A display name for the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement), and it is always set to "Hyper-V Metric Service Capabilities".

</dd> <dt>

**ElementNameEditSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **ElementName** property can be modified. This property is inherited from **CIM\_EnabledLogicalElementCapabilities**.

</dd> <dt>

**ElementNameMask**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the restrictions on **ElementName**, expressed as a regular expression. This property is inherited from **CIM\_EnabledLogicalElementCapabilities**.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Uniquely identifies an instance of this class. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**ManagedElementControlTypes**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ArrayType** ("Indexed")
</dt> </dl>

Identifies the type of control supported by the associated **CIM\_MetricService** instance for the [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement) object identified by the value at the same array index in the **ControllableManagedElements** property. If this property is **Null**, all control types are supported. This property is inherited from **CIM\_MetricServiceCapabilities**.



| Value                                                                                   | Meaning                    |
|-----------------------------------------------------------------------------------------|----------------------------|
| <dl> <dt>0</dt> </dl>            | Unknown<br/>         |
| <dl> <dt>2</dt> </dl>            | Discrete<br/>        |
| <dl> <dt>3</dt> </dl>            | Bulk<br/>            |
| <dl> <dt>4</dt> </dl>            | Both<br/>            |
| <dl> <dt>5..32767</dt> </dl>     | DMTF reserved<br/>   |
| <dl> <dt>32768..65535</dt> </dl> | Vendor specific<br/> |



 

</dd> <dt>

**MaxElementNameLen**
</dt> <dd> <dl> <dt>

Data type: **unit16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxValue** (256)
</dt> </dl>

Specifies the maximum supported length of the **ElementName** property. This property is inherited from **CIM\_EnabledLogicalElementCapabilities**.

</dd> <dt>

**MetricsControlTypes**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ArrayType** ("Indexed")
</dt> </dl>

Identifies the type of control supported by the associated **CIM\_MetricService** instance for the **CIM\_BaseMetricDefinition** identified by the value at the same array index in the **ControllableMetrics** property. If this property is **Null**, all control types are supported. This property is inherited from **CIM\_MetricServiceCapabilities**.



| Value                                                                                   | Meaning                    |
|-----------------------------------------------------------------------------------------|----------------------------|
| <dl> <dt>0</dt> </dl>            | Unknown<br/>         |
| <dl> <dt>2</dt> </dl>            | Discrete<br/>        |
| <dl> <dt>3</dt> </dl>            | Bulk<br/>            |
| <dl> <dt>4</dt> </dl>            | Both<br/>            |
| <dl> <dt>5..32767</dt> </dl>     | DMTF reserved<br/>   |
| <dl> <dt>32768..65535</dt> </dl> | Vendor specific<br/> |



 

</dd> <dt>

**RequestedStatesSupported**
</dt> <dd> <dl> <dt>

Data type: **unit16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the possible states that can be requested when using the **RequestStateChange** method on the enabled logical element. This property is inherited from **CIM\_EnabledLogicalElementCapabilities**.



| Value                                                                         | Meaning              |
|-------------------------------------------------------------------------------|----------------------|
| <dl> <dt>2</dt> </dl>  | Enabled<br/>   |
| <dl> <dt>3</dt> </dl>  | Disables<br/>  |
| <dl> <dt>4</dt> </dl>  | Shut Down<br/> |
| <dl> <dt>6</dt> </dl>  | Offline<br/>   |
| <dl> <dt>7</dt> </dl>  | Test<br/>      |
| <dl> <dt>8</dt> </dl>  | Defer<br/>     |
| <dl> <dt>9</dt> </dl>  | Quiesce<br/>   |
| <dl> <dt>10</dt> </dl> | Reboot<br/>    |
| <dl> <dt>11</dt> </dl> | Reset<br/>     |



 

</dd> <dt>

**SupportedMethods**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the methods supported by the metric service. This property is inherited from **CIM\_MetricServiceCapabilities**.



| Value                                                                                   | Meaning                                                                                         |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <dl> <dt>2</dt> </dl>            | The [**ControlMetrics**](controlmetrics-msvm-metricservice.md) method is supported.<br/> |
| <dl> <dt>3</dt> </dl>            | The **ControlMetricsByClass** method is supported.<br/>                                   |
| <dl> <dt>4</dt> </dl>            | The **ShowMetrics** method is supported.<br/>                                             |
| <dl> <dt>5</dt> </dl>            | The **ShowMetricsByClass** method is supported.<br/>                                      |
| <dl> <dt>6</dt> </dl>            | The **GetMetricValues** method is supported.<br/>                                         |
| <dl> <dt>7</dt> </dl>            | The **ControlSampleTimes** method is supported.<br/>                                      |
| <dl> <dt>8..32767</dt> </dl>     | DMTF reserved<br/>                                                                        |
| <dl> <dt>32768..65535</dt> </dl> | Vendor specific<br/>                                                                      |



 

</dd> </dl>

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

[**CIM\_MetricServiceCapabilities**](cim-metricservicecapabilities.md)
</dt> <dt>

[**Msvm\_MetricService**](msvm-metricservice.md)
</dt> </dl>

 

