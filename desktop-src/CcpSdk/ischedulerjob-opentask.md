---
Description: 'Opens a task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '62f79988-e2d0-4341-9729-34e68864e86c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::OpenTask method'
---

# ISchedulerJob::OpenTask method

Opens a task.

## Syntax


```C++
HRESULT OpenTask(
  [in]  ITaskId        *id,
  [out] ISchedulerTask **ppTask
);
```



## Parameters

<dl> <dt>

*id* \[in\]
</dt> <dd>

An [**ITaskId**](itaskid.md) interface that identifies the task to open.

</dd> <dt>

*ppTask* \[out\]
</dt> <dd>

An [**ISchedulerTask**](ischedulertask.md) interface to the opened task.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

You can use the [**IScheduler::CreateTaskId**](ischeduler-createtaskid.md) or [**IScheduler::CreateParametricTaskId**](ischeduler-createparametrictaskid.md) method to create the task identifier.

Only the job owner or administrator can open the task.

## Examples

For an example, see [Implementing the Event Handlers for Job Events in C++](implementing-the-event-handlers-for-job-events-in-c--.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Header<br/>       | <dl> <dt>Azroles.h</dt> </dl>                   |
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

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




