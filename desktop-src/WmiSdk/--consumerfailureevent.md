---
description: Represents the occurrence of some other event that is being dropped because of the failure of an event consumer.
ms.assetid: bb6a1ce9-72a2-4528-8bc8-71ac053b6b1d
ms.tgt_platform: multiple
title: '__ConsumerFailureEvent class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __ConsumerFailureEvent
- All
- All
- All
- All
- All
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_ConsumerFailureEvent class

The **\_\_ConsumerFailureEvent** system class represents the occurrence of some other event that is being dropped because of the failure of an event consumer.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __ConsumerFailureEvent : __EventDroppedEvent
{
  uint32              ErrorCode;
  string              ErrorDescription;
  object              ErrorObject;
  object              Event;
  __EventConsumer REF IntendedConsumer;
  uint8               SECURITY_DESCRIPTOR[];
  uint64              TIME_CREATED;
};
```

## Members

The **\_\_ConsumerFailureEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_ConsumerFailureEvent** class has these properties.

<dl> <dt>

**ErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Error code returned by the consumer.

</dd> <dt>

**ErrorDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Extended error code description, if available.

</dd> <dt>

**ErrorObject**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Object in error.

</dd> <dt>

**Event**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Event in error. This property is inherited from [**\_\_EventDroppedEvent**](--eventdroppedevent.md).

</dd> <dt>

**IntendedConsumer**
</dt> <dd> <dl> <dt>

Data type: **\_\_EventConsumer**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the intended consumer. This property is inherited from [**\_\_EventDroppedEvent**](--eventdroppedevent.md).

</dd> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor used by the event provider to determine which users can receive the event. This property is inherited from [**\_\_Event**](--event.md).

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

The **\_\_ConsumerFailureEvent** class is derived from [**\_\_EventDroppedEvent**](--eventdroppedevent.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_EventDroppedEvent**](/windows/desktop/WmiSdk/--eventdroppedevent)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> </dl>

 

