---
description: Use the WITHIN clause in event queries to specify a polling interval or a grouping interval.
ms.assetid: e2fc7627-fb3d-4966-b38b-441333868ae3
ms.tgt_platform: multiple
title: WITHIN Clause
ms.topic: article
ms.date: 05/31/2018
---

# WITHIN Clause

Event consumers use the WITHIN clause in event queries to specify a *polling interval* or a *grouping interval*.

A polling interval is the interval that Windows Management Instrumentation (WMI) uses to poll the data provider responsible for the class for [intrinsic events](determining-the-type-of-event-to-receive.md), of which the event queried is a member. This interval is the maximum amount of time that can pass before notification of an event must be delivered. A consumer uses a polling interval in a WITHIN clause when the consumer requires notification of changes to a class, and an event provider is unavailable. The consumer registers for an intrinsic event and includes the polling interval.

To specify a polling interval, place the WITHIN clause immediately before the WHERE clause, as shown following:


```sql
SELECT * FROM IntrinsicEventClass WITHIN interval  WHERE property = value
```



IntrinsicEventClass is the intrinsic event class of which the event is a member, interval is the polling interval, and value is the value for the property on which the consumer requires notification.

The polling interval is a floating-point number, and can be fractional to accept values smaller than 1 second. However, the interval should represent a number of seconds rather than an extremely small value such as 0.001, because specifying a value that is too small can cause WMI to reject the statement as not valid—due to the resource-intensive nature of polling. Because most event consumers do not require immediate notification, it is recommended that they use an interval that is greater than 5 minutes.

The following query example requests that WMI check every 10 seconds for changes that occur to instances of the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class. If an instance of the class is modified within the specified polling interval, a notification event is sent for each modification.


```sql
SELECT * FROM __InstanceModificationEvent WITHIN 10  WHERE TargetInstance ISA "Win32_LogicalDisk"
```



Depending on the query, an event provider and WMI can share the task of providing events. For example, an event provider that supports events of the [**\_\_InstanceCreationEvent**](--instancecreationevent.md) and [**\_\_InstanceModificationEvent**](--instancemodificationevent.md) system classes, and not events of the [**\_\_InstanceDeletionEvent**](--instancedeletionevent.md) system class. The following query enables the event provider to generate the creation and modification events as they occur and have them delivered when they are created. The query also allows WMI to generate **\_\_InstanceDeletionEvent** events every 10 (ten) seconds using the polling mechanism.


```sql
SELECT * FROM __InstanceOperationEvent WITHIN 10  WHERE TargetInstance ISA "MyOwnClass"
```



You can also use the WITHIN clause to specify a grouping interval. A grouping interval is an unsigned 32-bit integer that specifies the time period, after receiving an initial event, during which WMI should collect similar events. When this time period expires, WMI delivers the aggregate event, made up of all the similar events. For more information, see [GROUP Clause](group-clause.md).

Event consumers that register for frequently occurring events use a grouping interval with the WITHIN clause. Adding GROUP WITHIN to the WHERE clause in an event query results in WMI sending one aggregate event rather than many events. The aggregate event is represented by the [**\_\_AggregateEvent**](--aggregateevent.md) system class.

To specify a grouping interval, place the WITHIN clause immediately after the GROUP clause.


```sql
SELECT * FROM EventClass WHERE property = value GROUP WITHIN Interval
```



EventClass is the event class of which the event is a member, value is the value for the property on which the consumer requires notification, and Interval is the grouping interval.

For more information, see [Determining the Type of Event to Receive](determining-the-type-of-event-to-receive.md).

Permanent event consumers can be created with polling queries only if you have administrator privileges.

 

 
