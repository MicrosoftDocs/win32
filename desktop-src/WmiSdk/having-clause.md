---
description: The HAVING clause is used to filter the events that are received during the grouping interval specified in the WITHIN clause.
ms.assetid: 787e31df-df6a-4fb0-a1c0-18bd60867e2f
ms.tgt_platform: multiple
title: HAVING Clause
ms.topic: article
ms.date: 05/31/2018
---

# HAVING Clause

The HAVING clause is used to filter the events that are received during the grouping interval specified in the [WITHIN clause](within-clause.md). For example, a SELECT statement could be constructed so that it returns nothing unless there HAVE been at least 5 events within the past 30 second INTERVAL.

The WITHIN clause follows immediately in the [SELECT statement](select-statement-for-event-queries.md) after the [GROUP](group-clause.md) clause. The HAVING clause operates on the **NumberOfEvents** property of the [**\_\_AggregateEvent**](--aggregateevent.md) system class, of which the group created by the GROUP clause is a member. The HAVING clause can use all of the standard relational operators.

The syntax is as follows:

``` syntax
SELECT * FROM EventClass [WHERE property = value] 
  GROUP WITHIN interval [BY property_list]
  HAVING NumberOfEvents operator constant
```

The *EventClass* value is the event class of which the event is a member, and *value* is the value for the property on which notification is required. The interval is an unsigned integer that represents the grouping interval (in seconds) after receiving the first event. The property list is a comma-delimited list of one or more properties that are included in the event class. The operator is any relational operator. The constant value is any unsigned 32-bit integer indicating the number of events used for filtering.

When using the HAVING clause, the WHERE and BY clauses are optional.

The following event query requests that notifications of the **EmailEvent** class be grouped into one event 300 seconds after the first event that WMI receives. Also, the query requests the [**\_\_AggregateEvent**](--aggregateevent.md) instance should be delivered only if WMI receives more than five email events in that 300 seconds.


```sql
SELECT * FROM EmailEvent GROUP WITHIN 300 HAVING NumberOfEvents > 5
```



The following example groups all events received in 600 seconds (that is, 10 minutes) by the **TargetInstance**.**SourceName** property. In this example, aggregate events are delivered only if the number of [**Win32\_NTLogEvent**](/previous-versions/windows/desktop/eventlogprov/win32-ntlogevent) events received from the same source exceeds 25. Keep in mind that the ISA operator causes the **TargetInstance** property of the [**\_\_InstanceCreationEvent**](--instancecreationevent.md) system class to represent an instance of the **Win32\_NTLogEvent** class.


```sql
SELECT * FROM __InstanceCreationEvent 
  WHERE TargetInstance ISA "Win32_NTLogEvent" 
  GROUP WITHIN 600 BY TargetInstance.SourceName
  HAVING NumberOfEvents > 25
```



 

 
