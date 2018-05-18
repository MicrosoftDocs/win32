---
Description: 'Retrieves the time that the task was submitted.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd006b4f6-ced0-4c55-b9a8-eddce173da63'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::get\_SubmitTime method'
---

# ITask::get\_SubmitTime method

Retrieves the time that the task was submitted.

## Syntax


```C++
HRESULT get_SubmitTime(
  [out] DATE *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The time that the task was submitted.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

A task is submitted when its parent job is submitted.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJob::get\_SubmitTime**](ijob-get-submittime.md)
</dt> <dt>

[**ITask**](itask.md)
</dt> <dt>

[**ITask::get\_CreateTime**](itask-get-createtime.md)
</dt> <dt>

[**ITask::get\_EndTime**](itask-get-endtime.md)
</dt> <dt>

[**ITask::get\_StartTime**](itask-get-starttime.md)
</dt> </dl>

 

 




