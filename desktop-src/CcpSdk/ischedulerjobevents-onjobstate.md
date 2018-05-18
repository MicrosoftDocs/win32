---
Description: 'Is called when the state of the job changes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2523d4fb-1068-404b-b357-dbaf6c5b4f08'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJobEvents::OnJobState method'
---

# ISchedulerJobEvents::OnJobState method

Is called when the state of the job changes.

## Syntax


```C++
HRESULT OnJobState(
  [in] VARIANT           Sender,
  [in] IJobStateEventArg *pArgs
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

An [**IJobStateEventArg**](ijobstateeventarg.md) interface that provides information related to the state of the job.

</dd> </dl>

## Return value

You must return S\_OK.

## Remarks

To get the job, query the **pdispVal** member of *Sender* for the [**IScheduler**](ischeduler.md) interface. Then, pass the [**IJobStateEventArg.JobId**](ijobstateeventarg-jobid.md) property to the [**IScheduler::OpenJob**](ischeduler-openjob.md) method.

The dispatch identifier for this method is 0x60020000.

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

[**ISchedulerJobEvents::OnTaskState**](ischedulerjobevents-ontaskstate.md)
</dt> </dl>

 

 




