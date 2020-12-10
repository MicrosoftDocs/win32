---
title: SessionStateChangeTrigger.Delay property
description: For scripting, gets or sets a value that indicates how long of a delay takes place before a task is started after a Terminal Server session state change is detected.
ms.assetid: '3a17884f-fd74-491a-99dc-dce300a2cc77'
keywords:
- Delay property Task Scheduler
- Delay property Task Scheduler , SessionStateChangeTrigger object
- SessionStateChangeTrigger object Task Scheduler , Delay property
topic_type:
- apiref
api_name:
- SessionStateChangeTrigger.Delay
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SessionStateChangeTrigger.Delay property

For scripting, gets or sets a value that indicates how long of a delay takes place before a task is started after a Terminal Server session state change is detected. The format for this string is PnYnMnDTnHnMnS, where nY is the number of years, nM is the number of months, nD is the number of days, 'T' is the date/time separator, nH is the number of hours, nM is the number of minutes, and nS is the number of seconds (for example, PT5M specifies 5 minutes and P1M4DT2H5M specifies one month, four days, two hours, and five minutes).

## Syntax


```VB
SessionStateChangeTrigger.Delay As String
```



## Property value

The delay that takes place before a task is started after a Terminal Server session state change is detected.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



 

 





