---
Description: 'Clones the specified job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a6d679f0-fe61-4064-b387-6f1fa210542f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::CloneJob method'
---

# IScheduler::CloneJob method

Clones the specified job.

## Syntax


```C++
HRESULT CloneJob(
  [in]  long          id,
  [out] ISchedulerJob **pNewJob
);
```



## Parameters

<dl> <dt>

*id* \[in\]
</dt> <dd>

The job to clone.

</dd> <dt>

*pNewJob* \[out\]
</dt> <dd>

An [**ISchedulerJob**](ischedulerjob.md) interface that defines the newly cloned job.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

Only the owner of the job can clone the job. The job can be in any state when cloned.

The state of the new job is Configuring. After modifying the job (if necessary), call the [**IScheduler::SubmitJob**](ischeduler-submitjob.md) method to schedule the new job to run. If the job is not ready to run (you need to add tasks or change property values), call the [**IScheduler::AddJob**](ischeduler-createjob.md) method to save the job in the scheduler.

This method copies all the tasks (and instances for a parametric task) and the following subset of job properties:

-   JobPropertyIds.AutoCalculateMax
-   JobPropertyIds.AutoCalculateMin
-   JobPropertyIds.EncryptedPassword
-   JobPropertyIds.FailOnTaskFailure
-   JobPropertyIds.IsExclusive
-   JobPropertyIds.JobTemplate
-   JobPropertyIds.JobType
-   JobPropertyIds.MaxCores
-   JobPropertyIds.MaxCoresPerNode
-   JobPropertyIds.MaxMemory
-   JobPropertyIds.MaxNodes
-   JobPropertyIds.MaxSockets
-   JobPropertyIds.MinCores
-   JobPropertyIds.MinCoresPerNode
-   JobPropertyIds.MinMemory
-   JobPropertyIds.MinNodes
-   JobPropertyIds.MinSockets
-   JobPropertyIds.Name
-   JobPropertyIds.NextJobTaskId
-   JobPropertyIds.NodeGroups
-   JobPropertyIds.OrderBy
-   JobPropertyIds.Owner
-   JobPropertyIds.Priority
-   JobPropertyIds.Project
-   JobPropertyIds.RequestedNodes
-   JobPropertyIds.RuntimeSeconds
-   JobPropertyIds.RunUntilCanceled
-   JobPropertyIds.SoftwareLicense
-   JobPropertyIds.UnitType
-   JobPropertyIds.UserName

This method also copies the following subset of task properties:

-   TaskPropertyIds.CommandLine
-   TaskPropertyIds.DependsOn
-   TaskPropertyIds.EndValue
-   TaskPropertyIds.Id
-   TaskPropertyIds.IncrementValue
-   TaskPropertyIds.IsExclusive
-   TaskPropertyIds.IsParametric
-   TaskPropertyIds.IsRerunnable
-   TaskPropertyIds.MaxCores
-   TaskPropertyIds.MaxNodes
-   TaskPropertyIds.MaxSockets
-   TaskPropertyIds.MinCores
-   TaskPropertyIds.MinNodes
-   TaskPropertyIds.MinSockets
-   TaskPropertyIds.Name
-   TaskPropertyIds.RequiredNodes
-   TaskPropertyIds.RuntimeSeconds
-   TaskPropertyIds.StartValue
-   TaskPropertyIds.StdErrFilePath
-   TaskPropertyIds.StdInFilePath
-   TaskPropertyIds.StdOutFilePath
-   TaskPropertyIds.WorkDirectory

## Examples

For an example, see [Cloning a Job](cloning-a-job.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::CreateJob**](ischeduler-createjob.md)
</dt> <dt>

[**ISchedulerJob::RestoreFromXml**](ischedulerjob-restorefromxml.md)
</dt> </dl>

 

 




