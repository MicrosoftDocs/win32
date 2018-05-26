---
title: Trigger.ExecutionTimeLimit property
description: For scripting, gets or sets the maximum amount of time that the task launched by the trigger is allowed to run.
ms.assetid: cfd0b02b-2040-49c1-88a1-c9663c834450
keywords:
- ExecutionTimeLimit property Task Scheduler
- ExecutionTimeLimit property Task Scheduler , Trigger object
- Trigger object Task Scheduler , ExecutionTimeLimit property
topic_type:
- apiref
api_name:
- Trigger.ExecutionTimeLimit
api_location:
- taskschd.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Trigger.ExecutionTimeLimit property

For scripting, gets or sets the maximum amount of time that the task launched by the trigger is allowed to run.

## Syntax


```VB
Trigger.ExecutionTimeLimit As String
```



## Property value

The maximum amount of time that the task launched by the trigger is allowed to run. The format for this string is PnYnMnDTnHnMnS, where nY is the number of years, nM is the number of months, nD is the number of days, 'T' is the date/time separator, nH is the number of hours, nM is the number of minutes, and nS is the number of seconds (for example, PT5M specifies 5 minutes and P1M4DT2H5M specifies one month, four days, two hours, and five minutes).

## Remarks

When reading or writing XML for a task, the execution time limit is specified in the [**ExecutionTimeLimit**](taskschedulerschema-executiontimelimit-triggerbasetype-element.md) element of the Task Scheduler schema.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





