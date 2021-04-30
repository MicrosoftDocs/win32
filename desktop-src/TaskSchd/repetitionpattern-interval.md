---
title: RepetitionPattern.Interval property
description: For scripting, gets or sets the amount of time between each restart of the task.
ms.assetid: 'c48bd304-21f3-435e-99f5-3b2da0078bb8'
keywords:
- Interval property Task Scheduler
- Interval property Task Scheduler , RepetitionPattern object
- RepetitionPattern object Task Scheduler , Interval property
topic_type:
- apiref
api_name:
- RepetitionPattern.Interval
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RepetitionPattern.Interval property

For scripting, gets or sets the amount of time between each restart of the task.

## Syntax


```VB
RepetitionPattern.Interval As String
```



## Property value

The amount of time between each restart of the task. The format for this string is `P<days>DT<hours>H<minutes>M<seconds>S` (for example, "PT5M" is 5 minutes, "PT1H" is 1 hour, and "PT20M" is 20 minutes). The maximum time allowed is 31 days, and the minimum time allowed is 1 minute.

## Remarks

If you specify a repetition duration for a task, you must also specify the repetition interval.

When reading or writing XML for a task, the repetition interval is specified in the [**Interval**](taskschedulerschema-interval-repetitiontype-element.md) element of the Task Scheduler schema.

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
</dt> </dl>

 

 





