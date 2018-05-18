---
Description: 'Creates a job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '938cbd90-3d68-43ae-a942-c3b65065a3ca'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::CreateJob method'
---

# IScheduler::CreateJob method

Creates a job.

## Syntax


```C++
HRESULT CreateJob(
  [out] ISchedulerJob **job
);
```



## Parameters

<dl> <dt>

*job* \[out\]
</dt> <dd>

An [**ISchedulerJob**](ischedulerjob.md) interface that defines the newly created job. The job uses the default job template to specify the job's default property values and constraints.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

To specify a specific template to use, call the [**ISchedulerJob::SetJobTemplate**](ischedulerjob-setjobtemplate.md) method.

After defining the job (setting property values and adding tasks), call the [**IScheduler::SubmitJob**](ischeduler-submitjob.md) method to add the job to the scheduler and scheduling queue. If the job is not ready to be added to the scheduling queue, you can call the [**IScheduler::AddJob**](ischeduler-addjob.md) method to add the job to the scheduler.

## Examples

For an example, see [Creating and Submitting a Job](creating-and-submitting-a-job.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::AddJob**](ischeduler-createjob.md)
</dt> <dt>

[**IScheduler::CancelJob**](ischeduler-canceljob.md)
</dt> <dt>

[**IScheduler::CreateCommand**](ischeduler-createcommand.md)
</dt> <dt>

[**IScheduler::SubmitJob**](ischeduler-submitjob.md)
</dt> <dt>

[**IScheduler::OpenJob**](ischeduler-openjob.md)
</dt> </dl>

 

 




