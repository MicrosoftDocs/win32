---
Description: 'Cancels a task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '803a599c-1843-49fc-88db-64c71226b290'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::CancelTask method'
---

# ISchedulerJob::CancelTask method

Cancels a task.

## Syntax


```C++
HRESULT CancelTask(
  [in] ITaskId *taskId
);
```



## Parameters

<dl> <dt>

*taskId* \[in\]
</dt> <dd>

An [**ITaskId**](itaskid.md) interface that identifies the task to cancel.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property of the job.

## Remarks

To cancel a task, the [**state**](taskstate.md) of the task must be Configuring, Submitted, Queued, or Running. If a task is running when it is canceled, the task is ends and the state of the task changes to Failed. If you cancel a task with a state of Configuring or Queued, the state of the task changes to Canceled.

If you cancel a parametric task, the state of the parametric master task always changes to Canceled, and all of the individual subtasks are canceled. If the subtask is running when you cancel the parametric task, the state of the subtask changes to Failed. If the subtask is in a state other than Running, the state of the subtask changes to Canceled.

To determine the state of a task, access the [**ISchedulerTask::State**](ischedulertask-state.md) property.

You can call the [**ISchedulerJob::RequeueTask**](ischedulerjob-requeuetask.md) method to queue the task again.

The **ISchedulerJob::CancelTask** method honors the grace period for the cancellation of the task.

To cancel a task and provide a message to the user that explains the reason you canceled the task in Windows HPC Server 2008 R2, use the [**ISchedulerJob::CancelTask\_2**](ischedulerjob-canceltask-2.md) or [**ISchedulerJob::CancelTask\_3**](ischedulerjob-canceltask-3.md) method. To cancel a task immediately without using the grace period for canceling a task in Windows HPC Server 2008 R2, use the **ISchedulerJob::CancelTask\_3** method.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::CancelTask\_2**](ischedulerjob-canceltask-2.md)
</dt> <dt>

[**ISchedulerJob::CancelTask\_3**](ischedulerjob-canceltask-3.md)
</dt> <dt>

[**ISchedulerJob::AddTask**](ischedulerjob-addtask.md)
</dt> <dt>

[**ISchedulerJob::CreateTask**](ischedulerjob-createtask.md)
</dt> <dt>

[**ISchedulerJob::GetTaskIdList**](ischedulerjob-gettaskidlist.md)
</dt> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




