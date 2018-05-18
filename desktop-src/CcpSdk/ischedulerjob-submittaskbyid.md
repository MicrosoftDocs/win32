---
Description: 'Submits a task to the job using the task identifier to identify the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7855991c-dc7d-4d05-b9b3-698080afac1e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::SubmitTask method'
---

# ISchedulerJob::SubmitTask method

Submits a task to the job using the task identifier to identify the task.

## Syntax


```C++
HRESULT SubmitTask(
  [in] ITaskId *taskId
);
```



## Parameters

<dl> <dt>

*taskId* \[in\]
</dt> <dd>

An [**ITaskId**](itaskid.md) interface that identifies the task to add to the job.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

You can call this method any time after the job is added to the scheduler (see [**IScheduler::AddJob**](ischeduler-addjob.md)). Before the job is added to the scheduler, you must call the [**ISchedulerJob::AddTask**](ischedulerjob-addtask.md) method to add tasks to the job. After the job is submitted (see [**IScheduler::SubmitJob**](ischeduler-submitjob.md)), you must call this method or the [**SubmitTask**](ischedulerjob-submittask.md) method to add a task to the job if you want the task to run (if you call the **AddTask** method after the job is submitted, the task will not run until you submit the task). If you call the **SubmitTaskById** method, you must first call the **AddTask** method to get a task identifier assigned to the task.

You cannot submit a task after the job finishes.

The task will run in the order in which it was added to the job.

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

[**ISchedulerJob::CreateTask**](ischedulerjob-createtask.md)
</dt> <dt>

[**ISchedulerJob::GetTaskIdList**](ischedulerjob-gettaskidlist.md)
</dt> <dt>

[**ISchedulerJob::SubmitTask**](ischedulerjob-submittask.md)
</dt> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




