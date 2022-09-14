---
description: Specifies instructions on how timer events should be generated for consumers.
ms.assetid: b08edb25-bedf-4014-a835-4050f5749479
ms.tgt_platform: multiple
title: '__TimerInstruction class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __TimerInstruction
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_TimerInstruction class

The **\_\_TimerInstruction** abstract system class specifies instructions on how [timer events](receiving-a-timed-or-repeating-event.md) should be generated for consumers.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[abstract]
class __TimerInstruction : __EventGenerator
{
  boolean SkipIfPassed = FALSE;
  string  TimerId;
};
```

## Members

The **\_\_TimerInstruction** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_TimerInstruction** class has these properties.

<dl> <dt>

**SkipIfPassed**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes whether a notification event will be generated and receive when a consumer becomes available.

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

Unique user-assigned string that identifies this particular timer event. To avoid naming conflicts with other timer identifiers, the string form of a distributed computer environment (DCE)-style GUID can be used. This property is part of the [**\_\_TimerEvent**](--timerevent.md) instance that represents the event.

</dd> </dl>

## Remarks

The **\_\_TimerInstruction** class is derived from [**\_\_EventGenerator**](--eventgenerator.md).

The **\_\_TimerInstruction** subclasses are [**\_\_AbsoluteTimerInstruction**](--absolutetimerinstruction.md), used by consumers to register for an absolute timer event, and [**\_\_IntervalTimerInstruction**](--intervaltimerinstruction.md), used to register for an interval timer event.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_EventGenerator**](/windows/desktop/WmiSdk/--eventgenerator)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> </dl>

 

