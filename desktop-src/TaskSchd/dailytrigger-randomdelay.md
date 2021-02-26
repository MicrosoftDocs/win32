---
title: DailyTrigger.RandomDelay property
description: For scripting, gets or sets a delay time that is randomly added to the start time of the trigger. | DailyTrigger.RandomDelay property
ms.assetid: 0494a963-bdaf-4f3f-a2e3-9482409ecda4
keywords:
- RandomDelay property Task Scheduler
- RandomDelay property Task Scheduler , DailyTrigger object
- DailyTrigger object Task Scheduler , RandomDelay property
topic_type:
- apiref
api_name:
- DailyTrigger.RandomDelay
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# DailyTrigger.RandomDelay property

For scripting, gets or sets a delay time that is randomly added to the start time of the trigger.

## Syntax


```VB
DailyTrigger.RandomDelay As String
```



## Property value

The delay time that is randomly added to the start time of the trigger. The format for this string is P<days>DT<hours>H<minutes>M<seconds>S (for example, P2DT5S is a 2 day, 5 second delay).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**DailyTrigger**](dailytrigger.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





