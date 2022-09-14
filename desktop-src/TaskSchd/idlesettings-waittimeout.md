---
title: IdleSettings.WaitTimeout property
description: For scripting, gets or sets a value that indicates the amount of time that the Task Scheduler will wait for an idle condition to occur.
ms.assetid: 1be1c62b-bab0-41f8-9f64-e778aba4891f
keywords:
- WaitTimeout property Task Scheduler
- WaitTimeout property Task Scheduler , IdleSettings object
- IdleSettings object Task Scheduler , WaitTimeout property
topic_type:
- apiref
api_name:
- IdleSettings.WaitTimeout
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IdleSettings.WaitTimeout property

For scripting, gets or sets a value that indicates the amount of time that the Task Scheduler will wait for an idle condition to occur. If no value is specified for this property, then the Task Scheduler service will wait indefinitely for an idle condition to occur.

## Syntax


```VB
IdleSettings.WaitTimeout As String
```



## Property value

A value that indicates the amount of time that the Task Scheduler will wait for an idle condition to occur. The format for this string is PnYnMnDTnHnMnS, where nY is the number of years, nM is the number of months, nD is the number of days, 'T' is the date/time separator, nH is the number of hours, nM is the number of minutes, and nS is the number of seconds (for example, PT5M specifies 5 minutes and P1M4DT2H5M specifies one month, four days, two hours, and five minutes). The minimum time allowed is 1 minute. If this value is **NULL**, then the delay will be set to the default of 1 hour.

## Remarks

When reading or writing XML for a task, this setting is specified in the [**WaitTimeout**](taskschedulerschema-waittimeout-idlesettingstype-element.md) element of the Task Scheduler schema.

If a task is triggered by an idle trigger, then the **IdleSettings.WaitTimeout** property is ignored.

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

 

 





