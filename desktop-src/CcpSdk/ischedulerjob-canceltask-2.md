---
Description: 'Cancels the specified task and provides the specified message to the user to explain why the task was canceled.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9668AC1D-3F62-4BD6-8DC6-8FA0F656F799'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::CancelTask\_2 method'
---

# ISchedulerJob::CancelTask\_2 method

Cancels the specified task and provides the specified message to the user to explain why the task was canceled.

## Syntax


```C++
HRESULT CancelTask_2(
  [in] ITaskId *TaskId,
  [in] BSTR    Message
);
```



## Parameters

<dl> <dt>

*TaskId* \[in\]
</dt> <dd>

A [**ITaskId**](itaskid.md) interface for the task that you want to cancel.

</dd> <dt>

*Message* \[in\]
</dt> <dd>

A string that specifies the message that you want to provide to the user to explain why the task was canceled.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Remarks

To cancel a task, the state of the task must be Configuring, Submitted, Queued, or Running. If a task is running when it is canceled, the task ends and the state of the task changes to Failed. If you cancel a task with a task of Configuring or Queued, the state of the task changes to Canceled.

If you cancel a parametric task, the state of the parametric master task always changes to Canceled, and all of the individual subtasks are canceled. If the subtask is running when you cancel the parametric task, the state of the subtask changes to Failed. If the subtask is in a state other than Running, the state of the subtask changes to Canceled.

To determine the state of a task, use the [**ISchedulerTask::State**](ischedulertask-state.md) property.

You can call the [**ISchedulerJob::RequeueTask**](ischedulerjob-requeuetask.md) method to queue the task again.

The **ISchedulerJob::CancelTask\_2** method honors the grace period for the cancellation of the task.

To cancel a task without providing a message to the user that explains the reason you canceled the task, use the [**ISchedulerJob::CancelTask**](ischedulerjob-canceltask.md) method.

To cancel a task immediately without using the grace period for canceling a task in Windows HPC Server 2008 R2, use the [**ISchedulerJob::CancelTask\_3**](ischedulerjob-canceltask-3.md) method.

Calling the **ISchedulerJob::CancelTask\_2** method is equivalent to calling the [**ISchedulerJob::CancelTask\_3**](ischedulerjob-canceltask-3.md) method with the *isForce* parameter set to VARIANT\_FALSE. For better performance, call the **ISchedulerJob::CancelTask\_3** method with the *isForce* parameter set to VARIANT\_FALSE instead of calling **ISchedulerJob::CancelTask\_2**.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::CancelTask**](ischedulerjob-canceltask.md)
</dt> <dt>

[**ISchedulerJob::CancelTask\_3**](ischedulerjob-canceltask-3.md)
</dt> <dt>

[**ISchedulerJob::AddTask**](ischedulerjob-addtask.md)
</dt> <dt>

[**ISchedulerJob::CreateTask**](ischedulerjob-createtask.md)
</dt> <dt>

[**ISchedulerJob::SubmitTask**](ischedulerjob-submittask.md)
</dt> </dl>

 

 




