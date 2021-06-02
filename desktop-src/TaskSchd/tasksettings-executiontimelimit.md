---
title: TaskSettings.ExecutionTimeLimit property
description: For scripting, gets or sets the amount of time that is allowed to complete the task.
ms.assetid: '5b8b8d4b-e705-4407-95c9-bf8baacb58c1'
keywords:
- ExecutionTimeLimit property Task Scheduler
- ExecutionTimeLimit property Task Scheduler , TaskSettings object
- TaskSettings object Task Scheduler , ExecutionTimeLimit property
topic_type:
- apiref
api_name:
- TaskSettings.ExecutionTimeLimit
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskSettings.ExecutionTimeLimit property

For scripting, gets or sets the amount of time that is allowed to complete the task. By default, a task will be stopped 72 hours after it starts to run. You can change this by changing this setting.

This property is read/write.

## Syntax


```VB
TaskSettings.ExecutionTimeLimit As String
```



## Property value

The amount of time that is allowed to complete the task. The format for this string is PnYnMnDTnHnMnS, where nY is the number of years, nM is the number of months, nD is the number of days, 'T' is the date/time separator, nH is the number of hours, nM is the number of minutes, and nS is the number of seconds (for example, PT5M specifies 5 minutes and P1M4DT2H5M specifies one month, four days, two hours, and five minutes). A value of PT0S will enable the task to run indefinitely. When this parameter is set to Nothing, the execution time limit is infinite.

## Remarks

When reading or writing XML for a task, this setting is specified in the [**ExecutionTimeLimit**](taskschedulerschema-executiontimelimit-settingstype-element.md) element of the Task Scheduler schema.

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

 

 





