---
Description: 'Retrieves the specified job from the scheduler.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ea47aff6-09fc-4ee3-a622-c68f1d8e4748'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::OpenJob method'
---

# IScheduler::OpenJob method

Retrieves the specified job from the scheduler.

## Syntax


```C++
HRESULT OpenJob(
  [in]  long          id,
  [out] ISchedulerJob **job
);
```



## Parameters

<dl> <dt>

*id* \[in\]
</dt> <dd>

The job to retrieve.

</dd> <dt>

*job* \[out\]
</dt> <dd>

An [**ISchedulerJob**](ischedulerjob.md) interface that you can use to access the properties of the job.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The scheduler assigns the identifier when you call the [**IScheduler::AddJob**](ischeduler-addjob.md) or [**IScheduler::SubmitJob**](ischeduler-submitjob.md) method to add the job to the scheduler. To get the identifier, access the [**ISchedulerJob.Id**](ischedulerjob-id.md) property.

## Examples

For an example, see Getting a [Getting a List of Jobs](getting-a-list-of-jobs.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::AddJob**](ischeduler-addjob.md)
</dt> <dt>

[**IScheduler::CreateJob**](ischeduler-createjob.md)
</dt> <dt>

[**IScheduler::CancelJob**](ischeduler-canceljob.md)
</dt> <dt>

[**IScheduler::GetJobIdList**](ischeduler-getjobidlist.md)
</dt> <dt>

[**IScheduler::GetJobList**](ischeduler-getjoblist.md)
</dt> <dt>

[**IScheduler::SubmitJob**](ischeduler-submitjob.md)
</dt> </dl>

 

 




