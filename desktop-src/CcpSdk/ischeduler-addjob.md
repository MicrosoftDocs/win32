---
Description: 'Adds the specified job to the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f0549d5b-d219-4375-b1db-55db7393d6bf'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::AddJob method'
---

# IScheduler::AddJob method

Adds the specified job to the cluster.

## Syntax


```C++
HRESULT AddJob(
  [in] ISchedulerJob *job
);
```



## Parameters

<dl> <dt>

*job* \[in\]
</dt> <dd>

An [**ISchedulerJob**](ischedulerjob.md) interface of the job to add to the cluster. The properties in the interface are updated when the job is added. For example, the Id property is updated with the identifier that the scheduler assigns to the job.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

To create a job, call the [**IScheduler::CreateJob**](ischeduler-createjob.md) method. After setting the job properties and adding the tasks to the job, call the [**IScheduler::SubmitJob**](ischeduler-submitjob.md) method to add the job to the scheduling queue. Note that you can call **SubmitJob** without calling **AddJob** in which case **SubmitJob** will add the job to the scheduler if it has not already been added.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::ConfigureJob**](ischeduler-configurejob.md)
</dt> <dt>

[**IScheduler::CreateJob**](ischeduler-createjob.md)
</dt> <dt>

[**IScheduler::CancelJob**](ischeduler-canceljob.md)
</dt> <dt>

[**IScheduler::SubmitJob**](ischeduler-submitjob.md)
</dt> <dt>

[**IScheduler::OpenJob**](ischeduler-openjob.md)
</dt> </dl>

 

 




