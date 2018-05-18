---
Description: 'Creates a task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '77757143-566f-4f9f-82dd-920a5f4b4e0f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::CreateTask method'
---

# ISchedulerJob::CreateTask method

Creates a task.

## Syntax


```C++
HRESULT CreateTask(
  [out] ISchedulerTask **ppTask
);
```



## Parameters

<dl> <dt>

*ppTask* \[out\]
</dt> <dd>

An [**ISchedulerTask**](ischedulertask.md) interface that you use to define the task.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

The initial state of the task is Configuring (see [**TaskState**](taskstate.md)). You can add tasks to the job when the job is in the Configuring state. If the job is running, you can call the [**ISchedulerJob::SubmitTask**](ischedulerjob-submittask.md) method to add the task to the running job.

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

[**ISchedulerJob::AddTask**](ischedulerjob-addtask.md)
</dt> <dt>

[**ISchedulerJob::GetTaskIdList**](ischedulerjob-gettaskidlist.md)
</dt> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




