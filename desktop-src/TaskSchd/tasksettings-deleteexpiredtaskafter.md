---
title: TaskSettings.DeleteExpiredTaskAfter property
description: For scripting, gets or sets the amount of time that the Task Scheduler will wait before deleting the task after it expires.
ms.assetid: 'c57d736c-e3ce-44b8-809e-44f7c0321d70'
keywords:
- DeleteExpiredTaskAfter property Task Scheduler
- DeleteExpiredTaskAfter property Task Scheduler , TaskSettings object
- TaskSettings object Task Scheduler , DeleteExpiredTaskAfter property
topic_type:
- apiref
api_name:
- TaskSettings.DeleteExpiredTaskAfter
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TaskSettings.DeleteExpiredTaskAfter property

For scripting, gets or sets the amount of time that the Task Scheduler will wait before deleting the task after it expires. If no value is specified for this property, then the Task Scheduler service will not delete the task.

This property is read/write.

## Syntax


```VB
TaskSettings.DeleteExpiredTaskAfter As String
```



## Property value

A string that gets or sets the amount of time that the Task Scheduler will wait before deleting the task after it expires. The format for this string is PnYnMnDTnHnMnS, where nY is the number of years, nM is the number of months, nD is the number of days, 'T' is the date/time separator, nH is the number of hours, nM is the number of minutes, and nS is the number of seconds (for example, PT5M specifies 5 minutes and P1M4DT2H5M specifies one month, four days, two hours, and five minutes).

## Remarks

A task expires after the end boundary has been exceeded for all triggers associated with the task. The end boundary for a trigger is specified by the [EndBoundary](trigger-endboundary.md) property inherited by all trigger objects.

When reading or writing XML for a task, this setting is specified in the [**DeleteExpiredTaskAfter (settingsType)**](taskschedulerschema-deleteexpiredtaskafter-settingstype-element.md) element of the Task Scheduler schema.

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

 

 





