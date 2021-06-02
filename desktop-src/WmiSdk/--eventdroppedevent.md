---
description: Represents the occurrence of an event that is dropped. A dropped event is an event that is not delivered to an event consumer.
ms.assetid: fae267a9-e0ec-43fa-a3c3-d50345775a1d
ms.tgt_platform: multiple
title: '__EventDroppedEvent class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __EventDroppedEvent
- All
- All
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_EventDroppedEvent class

The **\_\_EventDroppedEvent** system class represents the occurrence of an event that is dropped. A dropped event is an event that is not delivered to an event consumer.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __EventDroppedEvent : __SystemEvent
{
  __Event             Event;
  __EventConsumer REF IntendedConsumer;
  uint8               SECURITY_DESCRIPTOR[];
  uint64              TIME_CREATED;
};
```

## Members

The **\_\_EventDroppedEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_EventDroppedEvent** class has these properties.

<dl> <dt>

**Event**
</dt> <dd> <dl> <dt>

Data type: **\_\_Event**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Event that is dropped.

</dd> <dt>

**IntendedConsumer**
</dt> <dd> <dl> <dt>

Data type: **\_\_EventConsumer**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to an instance of [**\_\_EventConsumer**](--eventconsumer.md) that represents the permanent consumer you identify to receive an event. Different permanent consumers that subscribe to an event can continue to receive the event.

</dd> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor that an event provider uses to determine the users who can receive an event. This property is inherited from [**\_\_Event**](--event.md).

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time when an event is generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Time (UTC) format. This property is inherited from [**\_\_Event**](--event.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> </dl>

## Remarks

The **\_\_EventDroppedEvent** class is derived from [**\_\_SystemEvent**](--systemevent.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_SystemEvent**](/windows/desktop/WmiSdk/--systemevent)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> </dl>

 

