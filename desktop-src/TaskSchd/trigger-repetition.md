---
title: Trigger.Repetition property
description: For scripting, gets or sets a value that indicates how often the task is run and how long the repetition pattern is repeated after the task is started.
ms.assetid: 'f90b935c-8b69-4c82-ac4b-6b049e7b9703'
keywords:
- Repetition property Task Scheduler
- Repetition property Task Scheduler , Trigger object
- Trigger object Task Scheduler , Repetition property
topic_type:
- apiref
api_name:
- Trigger.Repetition
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Trigger.Repetition property

For scripting, gets or sets a value that indicates how often the task is run and how long the repetition pattern is repeated after the task is started.

## Syntax


```VB
Trigger.Repetition As RepetitionPattern
```



## Property value

A [**RepetitionPattern**](repetitionpattern.md) object that defines how often the task is run and how long the repetition pattern is repeated after the task is started.

## Remarks

When reading or writing your own XML for a task, the repetition pattern for a trigger is specified in the [**Repetition**](taskschedulerschema-repetition-triggerbasetype-element.md) element of the Task Scheduler schema.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> <dt>

[**RepetitionPattern**](repetitionpattern.md)
</dt> </dl>

 

 





