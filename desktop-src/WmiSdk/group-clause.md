---
description: The GROUP clause causes WMI to generate a single notification to represent a group of events.
ms.assetid: 811e72f8-2e50-4696-ad58-50bb5e211afb
ms.tgt_platform: multiple
title: GROUP Clause
ms.topic: article
ms.date: 05/31/2018
---

# GROUP Clause

The GROUP clause causes WMI to generate a single notification to represent a group of events. The representative notification is an instance of the [**\_\_AggregateEvent**](--aggregateevent.md) system class. The **\_\_AggregateEvent** system class contains two properties: **Representative** and **NumberOfEvents**. The **Representative** property is an embedded object that contains one of the instances received during the grouping interval specified in the [WITHIN clause](within-clause.md). For example, if an aggregate event is generated to notify of instance modification events, **Representative** contains one instance of the [**\_\_InstanceModificationEvent**](--instancemodificationevent.md) class. The **NumberOfEvents** property contains the number of events received during the grouping interval. The grouping interval specifies the time period, after receiving an initial event, during which WMI should collect similar events.

The GROUP clause must contain a WITHIN clause to specify the grouping interval and can contain the BY or HAVING keyword, or both. The GROUP clause is placed after the WHERE clause, as shown following:

``` syntax
SELECT * FROM EventClass [WHERE property = value] 
    GROUP WITHIN interval [BY property_list]
    [HAVING NumberOfEvents operator integer]
```

The *EventClass* value is the event class of which the event is a member, and *value* is the value for the property on which notification is required. The interval is an unsigned integer that represents the grouping interval after receiving the first event. The unsigned integer is a number of seconds. The property list is a comma-delimited list of one or more properties that are included in the event class; *operator* is any relational operator; and *integer* is an unsigned 32-bit integer indicating a number of events.

When using the GROUP clause, the WHERE, BY, and HAVING clauses are optional.

A basic use of the GROUP clause might request a grouping of events within a time interval that starts when the first event is received. For example, the following query groups all of the email events sent within 5 minutes. Instead of paging a user every time a piece of new email is received, the permanent consumer might use this query to inform the user only if new email has been received within the last 5 minutes.


```sql
SELECT * FROM EmailEvent GROUP WITHIN 300
```



If more detailed information is required, events can be grouped by one or more properties of the event class. The following query requests that email events be combined with other events that have the same value in the **Sender** property:


```sql
SELECT * FROM EmailEvent GROUP WITHIN 300 BY Sender
```



A still greater level of detail can be achieved by adding a WHERE clause. For example, the following query notifies a user of new email from a particular sender that has arrived within the last 10 minutes, combined with other events that have the same value in the **Importance** property:


```sql
SELECT * FROM EventClass WHERE Sender = "MyBoss" 
  GROUP WITHIN 300 BY Importance
```



 

 



