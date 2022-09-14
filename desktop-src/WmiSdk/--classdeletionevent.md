---
description: Represents a class deletion event, which is a type of intrinsic event generated when a class is removed from the namespace.
ms.assetid: dd44c03e-4d0d-4750-942d-495893d21650
ms.tgt_platform: multiple
title: '__ClassDeletionEvent class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __ClassDeletionEvent
- All
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_ClassDeletionEvent class

The **\_\_ClassDeletionEvent** system class represents a class deletion event, which is a type of [intrinsic event](determining-the-type-of-event-to-receive.md) generated when a class is removed from the namespace.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __ClassDeletionEvent : __ClassOperationEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  object TargetClass;
  uint64 TIME_CREATED;
};
```

## Members

The **\_\_ClassDeletionEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_ClassDeletionEvent** class has these properties.

<dl> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor used by the event provider to determine which users can receive the event. This property is inherited from [**\_\_Event**](--event.md).

</dd> <dt>

**TargetClass**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Copy of the newly deleted class reported by the class deletion event. This property is inherited from [**\_\_ClassOperationEvent**](--classoperationevent.md).

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

The **\_\_ClassDeletionEvent** class is derived from [**\_\_ClassOperationEvent**](--classoperationevent.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_ClassOperationEvent**](/windows/desktop/WmiSdk/--classoperationevent)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> </dl>

 

