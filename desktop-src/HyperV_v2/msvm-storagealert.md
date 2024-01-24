---
description: Represents an event that is raised each time the OperationalStatus property of the Msvm\_ResourcePool or Msvm\_LogicalDisk class changes.
ms.assetid: 20E7C22A-A151-4EDC-90D8-4BCD53C42355
title: Msvm_StorageAlert class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_StorageAlert
- Msvm_StorageAlert.AlertingManagedElement
- Msvm_StorageAlert.AlertingElementFormat
- Msvm_StorageAlert.OtherAlertingElementFormat
- Msvm_StorageAlert.AlertType
- Msvm_StorageAlert.PerceivedSeverity
- Msvm_StorageAlert.ProbableCause
- Msvm_StorageAlert.ProbableCauseDescription
- Msvm_StorageAlert.EventTime
- Msvm_StorageAlert.OwningEntity
- Msvm_StorageAlert.MessageArguments
- Msvm_StorageAlert.MessageID
- Msvm_StorageAlert.Message
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_StorageAlert class

Represents an event that is raised each time the **OperationalStatus** property of the [**Msvm\_ResourcePool**](msvm-resourcepool.md) or [**Msvm\_LogicalDisk**](msvm-logicaldisk.md) class changes.

The following syntax is simplified from MOF code and includes these properties.

## Syntax

``` syntax
[Indication, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_StorageAlert : CIM_AlertIndication
{
  string   AlertingManagedElement[];
  uint16   AlertingElementFormat;
  uint16   OtherAlertingElementFormat;
  uint16   AlertType;
  uint16   PerceivedSeverity;
  uint16   ProbableCause;
  string   ProbableCauseDescription;
  datetime EventTime;
  string   OwningEntity;
  string   MessageArguments[];
  string   MessageID;
  string   Message;
};
```

## Members

The **Msvm\_StorageAlert** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_StorageAlert** class has these properties.

<dl> <dt>

**AlertingElementFormat**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ModelCorrespondence** ("CIM\_AlertIndication.AlertingManagedElement", "CIM\_AlertIndication.OtherAlertingElementFormat")
</dt> </dl>

Specifies the format of the **AlertingManagedElement** property. The format is a CIMObjectPath, with the format *&lt;NamespacePath&gt;:&lt;ClassName&gt;.&lt;Prop1&gt;=\\"&lt;Value1&gt;\\", "&lt;Prop2&gt;=\\"&lt;Value2&gt;\\"*, which specifies an instance in the CIM Schema.

This property is inherited from the **CIM\_AlertIndication** class.

The possible values are:

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="CIMObjectPath"></span><span id="cimobjectpath"></span><span id="CIMOBJECTPATH"></span>**CIMObjectPath** (2)
</dt> </dl>

</dd> <dt>

**AlertingManagedElement**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The WMI paths of the instance for which the alert is generated.

</dd> <dt>

**AlertType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the primary classification of the alert. The possible values for this property are:

<dl> <dt>

<span id="Quality_of_Service_Alert"></span><span id="quality_of_service_alert"></span><span id="QUALITY_OF_SERVICE_ALERT"></span>**Quality of Service Alert** (3)
</dt> </dl>

</dd> <dt>

**EventTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time at which the underlying event was detected.

</dd> <dt>

**Message**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A formatted message that is constructed by combining some or all of the dynamic elements that are specified in the **MessageArguments** property with the static elements uniquely identified by the **MessageID** property in a message registry or other catalog associated with the **OwningEntity** property.

</dd> <dt>

**MessageArguments**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the dynamic content of the message. If the value of **MessageID** is 32930, the argument at position 0 is the **PoolID** of the [**Msvm\_ResourcePool**](msvm-resourcepoolcomponent.md) instance for which the alert is generated.

</dd> <dt>

**MessageID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Uniquely identifies, within the scope of the **OwningEntity** property, the format of the **Message** property. The possible values for this property are:

32930 ("Storage Pool QoS Insufficient Throughput Message")

</dd> <dt>

**OtherAlertingElementFormat**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that defines "Other" values for **AlertingManagedElement**. This value MUST be set to a non NULL value when **AlertingManagedElement** is set to a value of 1 ("Other"). For all other values of **AlertingManagedElement**, the value of this string must be set to NULL.

This property is inherited from the **CIM\_AlertIndication** class.

</dd> <dt>

**OwningEntity**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Uniquely identifies the entity that owns the definition of the format of the **Message** described in this instance. The value of this property is always "Microsoft-Windows- Hyper-V."

"Microsoft-Windows- Hyper-V"

</dd> <dt>

**PerceivedSeverity**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the severity of the alert indication. The possible values for this property are:

<dl> <dt>

<span id="Information"></span><span id="information"></span><span id="INFORMATION"></span>**Information** (2)
</dt> <dt>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>**Degraded/Warning** (3)
</dt> </dl>

</dd> <dt>

**ProbableCause**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the probable cause of the situation that resulted in the alert indication.

<dl> <dt>

<span id="Storage_Capacity_Problem"></span><span id="storage_capacity_problem"></span><span id="STORAGE_CAPACITY_PROBLEM"></span>**Storage Capacity Problem** (50)
</dt> <dt>

<span id="Previous_Alert_Cleared"></span><span id="previous_alert_cleared"></span><span id="PREVIOUS_ALERT_CLEARED"></span>**Previous Alert Cleared** (59)
</dt> </dl>

</dd> <dt>

**ProbableCauseDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description that corresponds to the value of the **ProbableCause** property.

</dd> </dl>

## Remarks

The Hyper-V WMI provider won't raise events for individual virtual disks to avoid flooding clients with events in case of large scale malfunctions of the underlying storage systems.

When a client receives an **Msvm\_StorageAlert** event, if the value of the **ProbableCause** property is 50 ( Storage Capacity Problem ), the client can discover which virtual disks are operating outside their QoS policy by using one of these procedures:

-   Query all the [**Msvm\_LogicalDisk**](msvm-logicaldisk.md) instances that were allocated from the resource pool for which the event was generated. These **Msvm\_LogicalDisk** instances are associated to the resource pool via the [**Msvm\_ElementAllocatedFromPool**](msvm-elementallocatedfrompool.md) association.
-   Filter the result list by selecting instances whose OperationalStatus contains  Insufficient Throughput .

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_AlertIndication**](cim-alertindication.md)
</dt> <dt>

[**Msvm\_LogicalDisk**](msvm-logicaldisk.md)
</dt> <dt>

[**Msvm\_ResourcePool**](msvm-resourcepoolcomponent.md)
</dt> </dl>

 

 




