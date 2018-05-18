---
Description: 'Retrieves the task-related error message or task cancellation message.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ac745a7b-e1ae-4ce1-9e4c-b8cea9dd976f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::ErrorMessage property'
---

# ISchedulerTask::ErrorMessage property

Retrieves the task-related error message or task cancellation message.

This property is read-only.

## Syntax


```C++
HRESULT get_ErrorMessage(
  [out] BSTR *pErrorMessage
);
```



## Property value

The message.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The message contains the last run-time error message that was set for the task. The message can also contain the reason why the user canceled the task.

Check the message if the task state is Failed or Canceled.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerJob.ErrorMessage**](ischedulerjob-errormessage.md)
</dt> </dl>

 

 




