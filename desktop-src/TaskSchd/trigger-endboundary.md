---
title: Trigger.EndBoundary property
description: For scripting, gets or sets the date and time when the trigger is deactivated. The trigger cannot start the task after it is deactivated.
ms.assetid: 'f34e6ba8-f6ef-43a0-8e3a-76c6a5f1ac04'
keywords:
- EndBoundary property Task Scheduler
- EndBoundary property Task Scheduler , Trigger object
- Trigger object Task Scheduler , EndBoundary property
topic_type:
- apiref
api_name:
- Trigger.EndBoundary
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Trigger.EndBoundary property

For scripting, gets or sets the date and time when the trigger is deactivated. The trigger cannot start the task after it is deactivated.

## Syntax


```VB
Trigger.EndBoundary As String
```



## Property value

The date and time when the trigger is deactivated. The date and time must be in the following format: YYYY-MM-DDTHH:MM:SS(+-)HH:MM. For example the date October 11th, 2005 at 1:21:17 in the Pacific time zone would be written as 2005-10-11T13:21:17-08:00. The (+-)HH:MM section of the format describes the time zone as a certain number of hours ahead or behind Coordinated Universal Time (Greenwich Mean Time).

## Remarks

When reading or writing XML for a task, the enabled property is specified using the [**EndBoundary**](taskschedulerschema-endboundary-triggerbasetype-element.md) element of the Task Scheduler schema.

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

 

 





