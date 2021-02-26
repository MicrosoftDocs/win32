---
title: TimeTrigger.RandomDelay property
description: For scripting, gets or sets a delay time that is randomly added to the start time of the trigger. | TimeTrigger.RandomDelay property
ms.assetid: 'ee55dd85-9696-4872-8670-f919fca7481d'
keywords:
- RandomDelay property Task Scheduler
- RandomDelay property Task Scheduler , TimeTrigger object
- TimeTrigger object Task Scheduler , RandomDelay property
topic_type:
- apiref
api_name:
- TimeTrigger.RandomDelay
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TimeTrigger.RandomDelay property

For scripting, gets or sets a delay time that is randomly added to the start time of the trigger.

## Syntax


```VB
TimeTrigger.RandomDelay As String
```



## Property value

The delay time that is randomly added to the start time of the trigger. The format for this string is PnYnMnDTnHnMnS, where nY is the number of years, nM is the number of months, nD is the number of days, 'T' is the date/time separator, nH is the number of hours, nM is the number of minutes, and nS is the number of seconds (for example, PT5M specifies 5 minutes and P1M4DT2H5M specifies one month, four days, two hours, and five minutes).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

 





