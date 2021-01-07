---
description: Reports an instance deletion event, which is a type of intrinsic event generated when an instance is deleted from the namespace.
ms.assetid: a370fc95-15e3-49c3-98de-2f40d742f207
ms.tgt_platform: multiple
title: '__InstanceDeletionEvent class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __InstanceDeletionEvent
- All
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_InstanceDeletionEvent class

The **\_\_InstanceDeletionEvent** system class reports an instance deletion event, which is a type of [intrinsic event](determining-the-type-of-event-to-receive.md) generated when an instance is deleted from the namespace.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __InstanceDeletionEvent : __InstanceOperationEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  object TargetInstance;
  uint64 TIME_CREATED;
};
```

## Members

The **\_\_InstanceDeletionEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_InstanceDeletionEvent** class has these properties.

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

Copy of the instance that was deleted. This property is inherited from [**\_\_InstanceOperationEvent**](--instanceoperationevent.md).

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

The **\_\_InstanceDeletionEvent** class is derived from [**\_\_InstanceOperationEvent**](--instanceoperationevent.md).

**Deletion of a resource: \_\_InstanceDeletionEvent**

If you want to ensure that a particular antivirus scanner program continues to run on a computer, you can write a script that monitors the processes on the computer to determine whether any of them stop.

Notification queries that request notification of the deletion of a resource and use intrinsic events all use syntax similar to the following:

`SELECT * FROM __InstanceDeletionEvent WHERE TargetInstance ISA 'Win32_Process' and TargetInstance.Name = 'notepad.exe' `

## Examples

The [Monitor process deletion event](https://Gallery.TechNet.Microsoft.Com/060a9adb-f99b-4f34-ba65-19b5f5815a38) VBScript code sample on TechNet Gallery uses **\_\_InstanceDeletionEvent** to monitor the first occurrence of a WMI instance deletion event for [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process).

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

 

