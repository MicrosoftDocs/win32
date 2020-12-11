---
title: LogonTrigger.Delay property
description: For scripting, gets or sets a value that indicates the amount of time between when the user logs on and when the task is started.
ms.assetid: '42198357-18e9-4fff-a8bf-f2da36148dc8'
keywords:
- Delay property Task Scheduler
- Delay property Task Scheduler , LogonTrigger object
- LogonTrigger object Task Scheduler , Delay property
topic_type:
- apiref
api_name:
- LogonTrigger.Delay
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# LogonTrigger.Delay property

For scripting, gets or sets a value that indicates the amount of time between when the user logs on and when the task is started.

## Syntax


```VB
LogonTrigger.Delay As String
```



## Property value

A value that indicates the amount of time between when the user logs on and when the task is started. The format for this string is PnYnMnDTnHnMnS, where nY is the number of years, nM is the number of months, nD is the number of days, 'T' is the date/time separator, nH is the number of hours, nM is the number of minutes, and nS is the number of seconds (for example, PT5M specifies 5 minutes and P1M4DT2H5M specifies one month, four days, two hours, and five minutes).

## Remarks

When reading or writing XML for a task, the logon trigger delay is specified using the [**Delay**](taskschedulerschema-delay-logontriggertype-element.md) element of the Task Scheduler schema.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**LogonTrigger**](logontrigger.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





