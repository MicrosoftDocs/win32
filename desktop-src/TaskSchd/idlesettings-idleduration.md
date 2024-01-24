---
title: IdleSettings.IdleDuration property
description: For scripting, gets or sets a value that indicates the amount of time that the computer must be in an idle state before the task is run.
ms.assetid: 32b9a14e-e37e-4e3a-81eb-041387f2017b
keywords:
- IdleDuration property Task Scheduler
- IdleDuration property Task Scheduler , IdleSettings object
- IdleSettings object Task Scheduler , IdleDuration property
topic_type:
- apiref
api_name:
- IdleSettings.IdleDuration
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IdleSettings.IdleDuration property

For scripting, gets or sets a value that indicates the amount of time that the computer must be in an idle state before the task is run.

## Syntax


```VB
IdleSettings.IdleDuration As String
```



## Property value

A value that indicates the amount of time that the computer must be in an idle state before the task is run). The format for this string is PnYnMnDTnHnMnS, where nY is the number of years, nM is the number of months, nD is the number of days, 'T' is the date/time separator, nH is the number of hours, nM is the number of minutes, and nS is the number of seconds (for example, PT5M specifies 5 minutes and P1M4DT2H5M specifies one month, four days, two hours, and five minutes). The minimum value is one minute. If this value is **NULL**, then the delay will be set to the default of 10 minutes.

## Remarks

When reading or writing XML for a task, this setting is specified in the [**Duration**](taskschedulerschema-duration-idlesettingstype-element.md) element of the Task Scheduler schema.

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

[**IdleSettings**](idlesettings.md)
</dt> </dl>

 

 





