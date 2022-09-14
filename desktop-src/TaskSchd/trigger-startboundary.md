---
title: Trigger.StartBoundary property
description: For scripting, gets or sets the date and time when the trigger is activated.
ms.assetid: '0687cdda-e72c-47cd-ac0c-0de2f8afc3e8'
keywords:
- StartBoundary property Task Scheduler
- StartBoundary property Task Scheduler , Trigger object
- Trigger object Task Scheduler , StartBoundary property
topic_type:
- apiref
api_name:
- Trigger.StartBoundary
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Trigger.StartBoundary property

For scripting, gets or sets the date and time when the trigger is activated.

## Syntax


```VB
Trigger.StartBoundary As String
```



## Property value

The date and time when the trigger is activated. The date and time must be in the following format: YYYY-MM-DDTHH:MM:SS(+-)HH:MM. For example the date October 11th, 2005 at 1:21:17 in the Pacific Time zone would be written as 2005-10-11T13:21:17-08:00. The (+-)HH:MM section of the format describes the time zone as a certain number of hours ahead or behind Coordinated Universal Time (Greenwich Mean Time).

## Remarks

When reading or writing XML for a task, the trigger start boundary is specified in the [**StartBoundary**](taskschedulerschema-startboundary-triggerbasetype-element.md) element of the Task Scheduler schema.

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

 

 





