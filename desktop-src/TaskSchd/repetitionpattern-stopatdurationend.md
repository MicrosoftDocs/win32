---
title: RepetitionPattern.StopAtDurationEnd property
description: For scripting, gets or sets a Boolean value that indicates if a running instance of the task is stopped at the end of the repetition pattern duration.
ms.assetid: '421f2d6f-7c35-44b4-97f2-45f46ca5e40e'
keywords:
- StopAtDurationEnd property Task Scheduler
- StopAtDurationEnd property Task Scheduler , RepetitionPattern object
- RepetitionPattern object Task Scheduler , StopAtDurationEnd property
topic_type:
- apiref
api_name:
- RepetitionPattern.StopAtDurationEnd
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RepetitionPattern.StopAtDurationEnd property

For scripting, gets or sets a Boolean value that indicates if a running instance of the task is stopped at the end of the repetition pattern duration.

## Syntax


```VB
RepetitionPattern.StopAtDurationEnd As Boolean
```



## Property value

A Boolean value that indicates if a running instance of the task is stopped at the end of the repetition pattern duration.

## Remarks

When reading or writing XML for a task, this information is specified in the [**StopAtDurationEnd**](taskschedulerschema-stopatdurationend-repetitiontype-element.md) element of the Task Scheduler schema.

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

 

 





