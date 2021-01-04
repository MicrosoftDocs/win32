---
title: StopAtDurationEnd (repetitionType) Element
description: Specifies that a running instances of the task is stopped at the end of the repetition pattern duration.
ms.assetid: 4e34b5b2-ac93-4951-9de4-3e89614517d1
keywords:
- StopAtDurationEnd element Task Scheduler
topic_type:
- apiref
api_name:
- StopAtDurationEnd
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# StopAtDurationEnd (repetitionType) Element

Specifies that a running instance of the task is stopped at the end of the repetition pattern duration. This is applicable only if repetitions are set.

``` syntax
<xs:element name="StopAtDurationEnd"
 type="boolean"
 />
```

The **StopAtDurationEnd** element is defined by the [**repetitionType**](taskschedulerschema-repetitiontype-complextype.md) complex type.

## Parent element

| Element | Derived from | Description |
|-|-|-|
| [**Repetition**](taskschedulerschema-repetition-triggerbasetype-element.md) | [**repetitionType**](taskschedulerschema-repetitiontype-complextype.md) | Specifies how often the task is run and how long the repetition pattern is repeated after the task is started.<br/> |

## Remarks

For scripting development, this setting is specified using the [**RepetitionPattern.StopAtDurationEnd**](repetitionpattern-stopatdurationend.md) property.

For C++ development, this setting is specified using the [**IRepetitionPattern::StopAtDurationEnd**](/windows/win32/api/taskschd/nf-taskschd-irepetitionpattern-get_stopatdurationend) property.

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |

## See also

[Task Scheduler Schema Elements](task-scheduler-schema-elements.md)

[Task Scheduler](task-scheduler-start-page.md)
