---
description: Generates events at intervals, similar to a WM\_TIMER message in Windows programming.
ms.assetid: 0895a743-a0dd-4833-a2bf-0196369e18b9
ms.tgt_platform: multiple
title: '__IntervalTimerInstruction class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __IntervalTimerInstruction
- All
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_IntervalTimerInstruction class

The **\_\_IntervalTimerInstruction** system class generates events at intervals, similar to a WM\_TIMER message in Windows programming. An event consumer registers to receive interval timer events by creating an event query that references this class. Due to operating system behavior, there are no guarantees that events will be delivered at precisely the requested interval.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __IntervalTimerInstruction : __TimerInstruction
{
  uint32  IntervalBetweenEvents;
  boolean SkipIfPassed = FALSE;
  string  TimerId;
};
```

## Members

The **\_\_IntervalTimerInstruction** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_IntervalTimerInstruction** class has these properties.

<dl> <dt>

**IntervalBetweenEvents**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](standard-qualifiers.md) (milliseconds)
</dt> </dl>

Number of milliseconds between event firings.

</dd> <dt>

**SkipIfPassed**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, this event is to be skipped if the interval is already passed. The default is **FALSE**. This property is inherited from [**\_\_TimerInstruction**](--timerinstruction.md).

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

Unique identifier for this **\_\_IntervalTimerInstruction** object. This property is inherited from [**\_\_TimerInstruction**](--timerinstruction.md).

</dd> </dl>

## Remarks

The **\_\_IntervalTimerInstruction** class is derived from [**\_\_TimerInstruction**](--timerinstruction.md).

The event query entered to register for an interval timer event is usually based on the **TimerId** property. Notification events generated from an interval timer event contain the property **NumFirings** which contains data reflecting how many events fired during the time the events were unable to be received. If **SkipIfPassed** is set to **TRUE**, that information is discarded.

The value for the **IntervalBetweenEvents** property should be reasonably large. If it is too small, WMI may ignore it and not generate the event due to limitations in some operating systems.

WMI generates the interval timer event by creating an instance of the [**\_\_TimerEvent**](--timerevent.md) class.

To receive these timer events in a temporary event consumer, execute [**IWbemServices::ExecNotificationQuery**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execnotificationquery) with the following event query string:


```sql
SELECT * FROM __TimerEvent WHERE TimerID = "MyEvent"
```



To receive these timer events in a permanent event consumer, you must load the previous query into an event filter, define a logical consumer, and create a filter-to-consumer binding for the filter and consumer. For more information, see [Receiving Events at All Times](receiving-events-at-all-times.md).

## Examples

The following MOF declaration shows how to generate an interval timer event with the key property set to "MyEvent" every 10 seconds:


```mof
instance of __IntervalTimerInstruction
{
  TimerId = "MyEvent";     // inherited from __TimerInstruction
  SkipIfPassed = FALSE;    // also inherited
  IntervalBetweenEvents = 10000;
};
```



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
</dt> </dl>

 

