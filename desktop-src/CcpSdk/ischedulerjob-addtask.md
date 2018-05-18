---
Description: 'Adds the task to the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c929c592-8cd9-4985-a97a-fe2675a50985'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::AddTask method'
---

# ISchedulerJob::AddTask method

Adds the task to the job.

## Syntax


```C++
HRESULT AddTask(
  [in] ISchedulerTask *pTask
);
```



## Parameters

<dl> <dt>

*pTask* \[in\]
</dt> <dd>

An [**ISchedulerTask**](ischedulertask.md) interface of the task to add to the job. To create the task, call the [**ISchedulerJob::CreateTask**](ischedulerjob-createtask.md) method.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

Typically, you call this method while the job is in the Configuring state. After you submit the job (see [**IScheduler::SubmitJob**](ischeduler-submitjob.md)), you must call the [**ISchedulerJob::SubmitTask**](ischedulerjob-submittask.md) or [**ISchedulerJob::SubmitTaskById**](ischedulerjob-submittaskbyid.md) method to add a task to the job if you want the task to run (if you call the **AddTask** method after the job is submitted, the task will not run until you submit the task). You cannot add or submit a task after the job finishes. If you call the **SubmitTaskById** method, you must first call the **AddTask** method to get a task identifier assigned to the task.

The task will run in the order in which it was added to the job.

## Examples

For an example, see [Creating and Submitting a Job](creating-and-submitting-a-job.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::CreateTask**](ischedulerjob-createtask.md)
</dt> <dt>

[**ISchedulerJob::GetTaskIdList**](ischedulerjob-gettaskidlist.md)
</dt> <dt>

[**ISchedulerJob::SubmitTask**](ischedulerjob-submittask.md)
</dt> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




