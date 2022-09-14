---
description: Causes an event to be generated on a specific date at a specific time.
ms.assetid: bcb64c81-3b40-4665-a880-a100629656e0
ms.tgt_platform: multiple
title: '__AbsoluteTimerInstruction class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __AbsoluteTimerInstruction
- All
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_AbsoluteTimerInstruction class

The **\_\_AbsoluteTimerInstruction** system class causes an event to be generated on a specific date at a specific time. An event consumer registers to receive an absolute timer event by creating an instance of this class. The event is generated one time.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __AbsoluteTimerInstruction : __TimerInstruction
{
  datetime EventDateTime;
  boolean  SkipIfPassed = FALSE;
  string   TimerId;
};
```

## Members

The **\_\_AbsoluteTimerInstruction** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_AbsoluteTimerInstruction** class has these properties.

<dl> <dt>

**EventDateTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Fixed-length string in [DMTF format](date-and-time-format.md) that specifies when the timer fires.

</dd> <dt>

**SkipIfPassed**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the timer event occurs if WMI cannot generate it at the correct time interval, or the consumer requesting to receive the event is unavailable. If **TRUE**, the event will not occur. The default is **FALSE**. When WMI or the consumer becomes available, a notification event is generated and received. This property is inherited from [**\_\_TimerInstruction**](--timerinstruction.md).

<dt>

FALSE
</dt> <dd>

When WMI or the consumer becomes available again, a notification event will be generated and received.

</dd> <dt>

TRUE
</dt> <dd>

The timer event does not occur if WMI is unavailable to generate it at the appropriate time interval, or the consumer requesting to receive the event is unavailable.

</dd> </dl>

</dd> <dt>

**TimerId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](standard-qualifiers.md)
</dt> </dl>

Unique user-assigned string that identifies a specific timer event. To avoid naming conflicts with other timer identifiers, the string form of a distributed computer environment style GUID can be used. This property is inherited from [**\_\_TimerInstruction**](--timerinstruction.md).

</dd> </dl>

## Remarks

The **\_\_AbsoluteTimerInstruction** class is derived from [**\_\_TimerInstruction**](--timerinstruction.md).

WMI generates the absolute timer event by creating an instance of the [**\_\_TimerEvent**](--timerevent.md) class.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_TimerInstruction**](/windows/desktop/WmiSdk/--timerinstruction)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> <dt>

[Receiving Timed or Repeating Events](receiving-a-timed-or-repeating-event.md)
</dt> <dt>

[Receiving Events at All Times](receiving-events-at-all-times.md)
</dt> <dt>

[Receiving Events for the Duration of Your Application](receiving-events-for-the-duration-of-your-application.md)
</dt> </dl>

 

