---
title: Trigger Structures for Task Scheduler 1.0
description: Task Scheduler 1.0 uses several structures to define the criteria of a trigger.
ms.assetid: 'dd2ae4f6-fb2d-41f8-9400-7426b7ca4546'
---

# Trigger Structures for Task Scheduler 1.0

Task Scheduler 1.0 uses several structures to define the criteria of a trigger.

> [!Note]  
> For more information about Task Scheduler 2.0 triggers, see [Trigger Interfaces](trigger-interfaces.md#).

 

## Task Scheduler 1.0 Structures

The following illustration shows the [**TASK\_TRIGGER**](task-trigger.md) structure. It has three required members (**wBeginYear**, **wBeginMonth**, and **wBeginDay**) that must be set when creating a new trigger. (To jump to the reference page for this structure, click the structure name in the illustration.)

![task trigger structure](images/tsktri1.png)

Be aware that the **TriggerType** member uses the [**TASK\_TRIGGER\_TYPE**](task-trigger-type.md) enumeration and the **Type** member uses a **TASK\_TRIGGER\_UNION** structure. The **TASK\_TRIGGER\_TYPE** enumeration is used to specify the type of trigger (event and time-based trigger types). The [**TRIGGER\_TYPE\_UNION**](trigger-type-union.md) structure is used to combine the [**DAILY**](daily.md), [**WEEKLY**](weekly.md), [**MONTHLYDATE**](monthlydate.md) (day of month), and [**MONTHLYDOW**](monthlydow.md) (day of week) structures that are used to specify when a time-based trigger will fire.

If **TriggerType** specifies a one-time time-based trigger or an event-based trigger, the **Type** member is ignored. The [**TRIGGER\_TYPE\_UNION**](trigger-type-union.md) structure is used only if the **TriggerType** member specifies a daily, weekly, day-of-month, or monthly day-of-week time-based trigger.

In addition, the setting of the **Type** member indicates which member of the [**TRIGGER\_TYPE\_UNION**](trigger-type-union.md) structure is used. The following illustration shows the relationship between the values of the [**TASK\_TRIGGER\_TYPE**](task-trigger-type.md) enumeration and the members of the **TRIGGER\_TYPE\_STRUCTURE** structure. (To jump to the reference pages for these structures click the structure name in the illustration.)

![relationship between task trigger type enumeration values and members of the trigger type structure structure](images/tsktri3.png)

## Related topics

<dl> <dt>

[Task Triggers](task-triggers.md)
</dt> <dt>

[Trigger Types](trigger-types.md)
</dt> <dt>

[Trigger Interfaces](trigger-interfaces.md)
</dt> </dl>

 

 




