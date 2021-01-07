---
description: Serves as a base class for all intrinsic events that relate to an instance.
ms.assetid: f6d2b6e5-0dca-4cb5-95a5-33b45cd76807
ms.tgt_platform: multiple
title: '__InstanceOperationEvent class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __InstanceOperationEvent
- All
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_InstanceOperationEvent class

The **\_\_InstanceOperationEvent** system class serves as a base class for all intrinsic events that relate to an instance.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __InstanceOperationEvent : __Event
{
  uint8  SECURITY_DESCRIPTOR[];
  object TargetInstance;
  uint64 TIME_CREATED;
};
```

## Members

The **\_\_InstanceOperationEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_InstanceOperationEvent** class has these properties.

<dl> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor used by the event provider to determine which users can receive the event. This property is inherited from [**\_\_Event**](--event.md).

</dd> <dt>

**TargetInstance**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Instance affected by the event. For creation events, this is the newly created instance. For modification events, this is the new version of the changed instance. For deletion events, this is the deleted instance.

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time at which the event was generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Times (UTC) format. This property is inherited from [**\_\_Event**](--event.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> </dl>

## Remarks

The **\_\_InstanceOperationEvent** class is derived from [**\_\_Event**](--event.md).

Instances of **\_\_InstanceOperationEvent** are not created; only instances of its subclasses are created. The following classes derive from **\_\_InstanceOperationEvent**:

[**\_\_InstanceCreationEvent**](--instancecreationevent.md)

[**\_\_InstanceModificationEvent**](--instancemodificationevent.md)

[**\_\_InstanceDeletionEvent**](--instancedeletionevent.md)

**Overview**

Just as there is a WMI class that represents each type of system resource that can be managed using WMI, there is a WMI class that represents each type of WMI event. When an event that can be monitored by WMI occurs, an instance of the corresponding WMI event class is created. A WMI event occurs when that instance is created.

There are three major types of WMI event classes, all of which are derived from the [**\_\_Event**](--event.md) WMI class: Intrinsic Events, Extrinsic Events, and Timer Events. Intrinsic Events, in turn, are represented by three distinct classes derived from the **\_\_Event** class: [**\_\_NamespaceOperationEvent**](--namespaceoperationevent.md), **\_\_InstanceOperationEvent**, and [**\_\_ClassOperationEvent**](--classoperationevent.md).

Intrinsic Events

Intrinsic events are used to monitor a resource represented by a class in the CIM repository. Each resource is represented by an instance of a class. This means that monitoring a resource using WMI actually involves monitoring the instances that correspond to the resource.

Intrinsic events can also be used to monitor changes to a namespace or class in the repository. However, monitoring changes to namespaces or classes is of limited value to system administrators.

An intrinsic event is represented by an instance of a class derived from \_\_InstanceOperationEvent, \_\_NamespaceOperationEvent, or \_\_ClassOperationEvent. Any changes to instances in WMI are represented by the \_\_InstanceOperationEvent class and the classes derived from it: \_\_InstanceCreationEvent, \_\_InstanceModificationEvent, and \_\_InstanceDeletionEvent.

Monitoring resources using WMI involves monitoring instances and all changes to instances are represented by \_\_InstanceOperationEvent and the classes derived from it. This means that monitoring resources ultimately involves monitoring instances of \_\_InstanceOperationEvent-derived classes.

You register interest in instances of one of these classes by issuing a notification query expressed in WQL. The query uses syntax similar to the following:

`SELECT * FROM __InstanceOperationEventOrDerivedClass WITHIN PollingInterval WHERE TargetInstance ISA WMIClassName AND TargetInstance.WMIClassPropertyName = Value`

For a longer discussion of using the WMI instance events to monitor computer activity, see [How Can I Monitor for Different Types of Events With Just One Script?](https://blogs.technet.com/b/heyscriptingguy/archive/2005/04/04/how-can-i-monitor-for-different-types-of-events-with-just-one-script.aspx)

## Examples

The [Monitor process event](https://Gallery.TechNet.Microsoft.Com/94c7dc4c-813a-411d-aa3f-f98982cd2a2f) VBScript code sample on TechNet Gallery uses **\_\_InstanceOperationEvent** to monitors the first WMI instance event for [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_Event**](/windows/desktop/WmiSdk/--event)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> <dt>

[Determining the Type of Event to Receive](determining-the-type-of-event-to-receive.md)
</dt> <dt>

[Writing to a Log File Based on an Event](writing-to-a-log-file-based-on-an-event.md)
</dt> </dl>

 

