---
title: MonthlyTrigger.RandomDelay property
description: For scripting, gets or sets a delay time that is randomly added to the start time of the trigger.
ms.assetid: '6b2a42dc-4002-4e51-9a8a-2982f83835d6'
keywords: ["RandomDelay property Task Scheduler", "RandomDelay property Task Scheduler , MonthlyTrigger object", "MonthlyTrigger object Task Scheduler , RandomDelay property"]
topic_type:
- apiref
api_name:
- MonthlyTrigger.RandomDelay
api_location:
- taskschd.dll
api_type:
- COM
---

# MonthlyTrigger.RandomDelay property

For scripting, gets or sets a delay time that is randomly added to the start time of the trigger.

## Syntax


```VB
MonthlyTrigger.RandomDelay As String
```



## Property value

The delay time that is randomly added to the start time of the trigger. The format for this string is P&lt;days&gt;DT&lt;hours&gt;H&lt;minutes&gt;M&lt;seconds&gt;S (for example, P2DT5S is a 2 day, 5 second delay).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**MonthlyTrigger**](monthlytrigger.md)
</dt> </dl>

 

 





