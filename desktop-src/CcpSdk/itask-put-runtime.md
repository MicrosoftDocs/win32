---
Description: 'Sets the run-time limit for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '78986f48-31ee-4699-b0a1-9877dfc4cfaa'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::put\_Runtime method'
---

# ITask::put\_Runtime method

Sets the run-time limit for the task.

## Syntax


```C++
HRESULT put_Runtime(
  [in] BSTR Val
);
```



## Parameters

<dl> <dt>

*Val* \[in\]
</dt> <dd>

The run-time limit for the task. The value can be "Infinite" or a string in the format *dd*:*hh*:*mm* where *dd* is the number of days, *hh* is the number of hours, and *mm* is the number of minutes. You must provide leading zeros; for example, to specify a run time of one minute, use the string "00:00:01". The default is "Infinite".

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The wall clock is used to determine the run time. The time is your best guess of how long the task will take; however, it needs to be fairly accurate because it is used to allocate resources. If the task exceeds this time, the task is terminated and its status becomes TaskStatus\_Failed.

If the task's run-time value is greater than the job's [run-time](ijob-put-runtime.md) value, then the task will run until it exceeds the job's run-time value. If this occurs, the task is terminated and its status becomes TaskStatus\_Failed.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ITask**](itask.md)
</dt> <dt>

[**ITask::get\_Runtime**](itask-get-runtime.md)
</dt> <dt>

[**IJob::put\_Runtime**](ijob-put-runtime.md)
</dt> </dl>

 

 




