---
description: Reports an instance modification event, which is a type of intrinsic event generated when an instance changes in the namespace.
ms.assetid: aa35f349-8b57-435f-bf82-76daf2b43ec9
ms.tgt_platform: multiple
title: '__InstanceModificationEvent class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __InstanceModificationEvent
- All
- All
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_InstanceModificationEvent class

The **\_\_InstanceModificationEvent** system class reports an instance modification event, which is a type of [intrinsic event](determining-the-type-of-event-to-receive.md) generated when an instance changes in the namespace.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __InstanceModificationEvent : __InstanceOperationEvent
{
  object PreviousInstance;
  uint8  SECURITY_DESCRIPTOR[];
  object TargetInstance;
  uint64 TIME_CREATED;
};
```

## Members

The **\_\_InstanceModificationEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_InstanceModificationEvent** class has these properties.

<dl> <dt>

**PreviousInstance**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Copy of the instance prior to modification.

</dd> <dt>

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

New version of the changed instance. This property is inherited from [**\_\_InstanceOperationEvent**](--instanceoperationevent.md).

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

The **\_\_InstanceModificationEvent** class is derived from [**\_\_InstanceOperationEvent**](--instanceoperationevent.md).

**Modification of a resource: \_\_InstanceModificationEvent**

Suppose you suspect that a management application you are using is erroneously changing the startup type of a service on one of your servers. You want to write a WMI script to monitor any modifications made to the configuration of the service. As soon as a modification is made to a service, its corresponding TargetInstance reflects the modification.

If you register your interest in this event, a modification to the configuration of the service results in the creation of an instance of the **\_\_InstanceModificationEvent** class.

Notification queries that request notification of the modification of a resource and use intrinsic events all use syntax similar to the following:

`SELECT * FROM __InstanceModificationEvent WITHIN PollingInterval WHERE TargetInstance ISA 'Win32_Service' and TargetInstance.Name = 'alerter'`

## Examples

The [Monitor process modification event](https://Gallery.TechNet.Microsoft.Com/daa06cdd-c1d9-4179-ba67-83aef2b9a079) VBScript sample on TechNet Gallery uses **\_\_InstanceModificationEvent** to monitor the first occurrence of a WMI instance modification event for [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_InstanceOperationEvent**](/windows/desktop/WmiSdk/--instanceoperationevent)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> </dl>

 

