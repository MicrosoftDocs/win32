---
Description: 'Queues a task again.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5e24e0ce-1b70-4fba-8b64-7c243d44a1ee'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::RequeueTask method'
---

# ISchedulerJob::RequeueTask method

Queues a task again.

## Syntax


```C++
HRESULT RequeueTask(
  [in] ITaskId *id
);
```



## Parameters

<dl> <dt>

*id* \[in\]
</dt> <dd>

An [**ITaskId**](itaskid.md) interface that identifies the task.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

Typically, you queue a task again if you were able to fix the cause of the failure, and you want to try running the task again.

If you call this method while the task is running, the task is canceled. You cannot call this method for a completed task.

You can queue a task again only if the [**ISchedulerTask.IsRerunnable**](ischedulertask-isrerunnable.md) property is set to VARIANT\_TRUE.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::AddTask**](ischedulerjob-addtask.md)
</dt> <dt>

[**ISchedulerJob::CancelTask**](ischedulerjob-canceltask.md)
</dt> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




