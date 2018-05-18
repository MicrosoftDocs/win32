---
title: RepetitionPattern.StopAtDurationEnd property
description: For scripting, gets or sets a Boolean value that indicates if a running instance of the task is stopped at the end of the repetition pattern duration.
ms.assetid: 'a43b5b32-a496-4f59-89f2-4b8566332e03'
keywords: ["StopAtDurationEnd property Task Scheduler", "StopAtDurationEnd property Task Scheduler , RepetitionPattern object", "RepetitionPattern object Task Scheduler , StopAtDurationEnd property"]
topic_type:
- apiref
api_name:
- RepetitionPattern.StopAtDurationEnd
api_location:
- taskschd.dll
api_type:
- COM
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



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





