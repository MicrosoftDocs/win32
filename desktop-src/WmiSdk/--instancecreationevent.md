---
description: Reports an instance creation event, which is a type of intrinsic event that is generated when a new instance is added to the namespace.
ms.assetid: 41976479-70e3-4914-a56a-fa94a1fd31c7
ms.tgt_platform: multiple
title: '__InstanceCreationEvent class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __InstanceCreationEvent
- All
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_InstanceCreationEvent class

The **\_\_InstanceCreationEvent** system class reports an instance creation event, which is a type of [intrinsic event](determining-the-type-of-event-to-receive.md) that is generated when a new instance is added to the namespace.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __InstanceCreationEvent : __InstanceOperationEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  object TargetInstance;
  uint64 TIME_CREATED;
};
```

## Members

The **\_\_InstanceCreationEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_InstanceCreationEvent** class has these properties.

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

Copy of the instance that was created. This property is inherited from [**\_\_InstanceOperationEvent**](--instanceoperationevent.md).

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time at which the event was generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Time (UTC) format. This property is inherited from [**\_\_Event**](--event.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> </dl>

## Remarks

The **\_\_InstanceCreationEvent** class is derived from [**\_\_InstanceOperationEvent**](--instanceoperationevent.md).

**Creation of a resource: \_\_InstanceCreationEvent**

Suppose you are interested in receiving a notification if Notepad is run on a certain computer. When Notepad runs, a corresponding process is created. Processes can be managed by using WMI and are represented by the Win32\_Process class. When Notepad starts running, a corresponding instance of the Win32\_Process class becomes available through WMI. If you have registered your interest in this event (by issuing the appropriate event notification query), the availability of this instance results in the creation of an instance of the **\_\_InstanceCreationEvent** class.

Notification queries that request notification of the creation of a resource and use intrinsic events all use syntax similar to the following:

`SELECT * FROM __InstanceCreationEvent WITHIN PollingInterval WHERE TargetInstance ISA 'Win32_Process' and TargetInstance.Name = 'notepad.exe'`

For a larger discussion of using **\_\_InstanceCreationEvent** as a way to monitor file systems, see [WMI and File System Monitoring](https://www.codeproject.com/Articles/42212/WMI-and-File-System-Monitoring) on CodeProject.

## Examples

The [Create Permanent WMI Event registration to monitor files](https://Gallery.TechNet.Microsoft.Com/Create-Permenant-WMI-Event-f67ce5c2) PowerShell example on TechNet Gallery uses **\_\_InstanceCreationEvent** as part of a complex script to set up a permanent WMI event registration.

The [PowerShell WMI Permanent Events](https://Gallery.TechNet.Microsoft.Com/PowerShell-WMI-Permanent-7e17f262) PowerShell example on TechNet Gallery uses **\_\_InstanceCreationEvent** as part of a demonstration script for setting up a permanent event registration.

The [Monitor process creation event](https://Gallery.TechNet.Microsoft.Com/6f137d9e-f00a-4f0a-ad07-7d752ff5251d) VBScript sample on TechNet uses **\_\_InstanceCreationEvent** to monitors the first WMI instance creation event for [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process).

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

 

