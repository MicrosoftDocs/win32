---
description: Is a base class for all intrinsic events that relate to a class.
ms.assetid: 554bbabd-2639-40f5-8786-6df2188db0ec
ms.tgt_platform: multiple
title: '__ClassOperationEvent class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __ClassOperationEvent
- All
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_ClassOperationEvent class

The **\_\_ClassOperationEvent** system class is a base class for all intrinsic events that relate to a class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __ClassOperationEvent : __Event
{
  uint8  SECURITY_DESCRIPTOR[];
  object TargetClass;
  uint64 TIME_CREATED;
};
```

## Members

The **\_\_ClassOperationEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_ClassOperationEvent** class has these properties.

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

Class affected by the event. For creation events, this is the newly created class. For modification events, this is the new version of the changed class. For deletion events, this is the deleted class.

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

The **\_\_ClassOperationEvent** class is derived from [**\_\_Event**](--event.md).

Instances of **\_\_ClassOperationEvent** are not created; only instances of its subclasses are created. The following classes derive from **\_\_ClassOperationEvent**:

[**\_\_ClassCreationEvent**](--classcreationevent.md)

[**\_\_ClassModificationEvent**](--classmodificationevent.md)

[**\_\_ClassDeletionEvent**](--classdeletionevent.md)

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
</dt> </dl>

 

