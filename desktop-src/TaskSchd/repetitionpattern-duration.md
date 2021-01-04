---
title: RepetitionPattern.Duration property
description: For scripting, gets or sets how long the pattern is repeated.
ms.assetid: '41a56414-981b-440a-b51a-228125baf303'
keywords:
- Duration property Task Scheduler
- Duration property Task Scheduler , RepetitionPattern object
- RepetitionPattern object Task Scheduler , Duration property
topic_type:
- apiref
api_name:
- RepetitionPattern.Duration
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RepetitionPattern.Duration property

For scripting, gets or sets how long the pattern is repeated.

## Syntax


```VB
RepetitionPattern.Duration As String
```



## Property value

How long the pattern is repeated. The format for this string is PnYnMnDTnHnMnS, where nY is the number of years, nM is the number of months, nD is the number of days, 'T' is the date/time separator, nH is the number of hours, nM is the number of minutes, and nS is the number of seconds (for example, PT5M specifies 5 minutes and P1M4DT2H5M specifies one month, four days, two hours, and five minutes). The minimum time allowed is one minute.

If no value is specified for the duration, then the pattern is repeated indefinitely.

## Remarks

If you specify a repetition duration for a task, you must also specify the repetition interval.

When reading or writing XML for a task, the repetition duration is specified in the [**Duration**](taskschedulerschema-duration-repetitiontype-element.md) element of the Task Scheduler schema.

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

 

 





