---
Description: 'Is called when the state of a task in the job changes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '00ae8ee8-a7fd-4140-989f-8533f09ae436'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJobEvents::OnTaskState method'
---

# ISchedulerJobEvents::OnTaskState method

Is called when the state of a task in the job changes.

## Syntax


```C++
HRESULT OnTaskState(
  [in] VARIANT            Sender,
  [in] ITaskStateEventArg *pArgs
);
```



## Parameters

<dl> <dt>

*Sender* \[in\]
</dt> <dd>

A variant that contains the Scheduler object.

</dd> <dt>

*pArgs* \[in\]
</dt> <dd>

An [**ITaskStateEventArg**](itaskstateeventarg.md) interface that provides information related to the state of the job.

</dd> </dl>

## Return value

You must return S\_OK.

## Remarks

To get the job, query the **pdispVal** member of *Sender* for the [**IScheduler**](ischeduler.md) interface. Then, pass the [**ITaskStateEventArg.JobId**](itaskstateeventarg-jobid.md) property to the [**IScheduler::OpenJob**](ischeduler-openjob.md) method. To get the task, pass the [**ITaskStateEventArg.TaskId**](itaskstateeventarg-taskid.md) property to the [**ISchedulerJob::OpenTask**](ischedulerjob-opentask.md) method.

The dispatch identifier for this method is 0x60020001.

## Examples

For an example, see [Implementing the Event Handlers for Job Events in C++](implementing-the-event-handlers-for-job-events-in-c--.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJobEvents**](ischedulerjobevents.md)
</dt> <dt>

[**ISchedulerJobEvents::OnJobState**](ischedulerjobevents-onjobstate.md)
</dt> </dl>

 

 




