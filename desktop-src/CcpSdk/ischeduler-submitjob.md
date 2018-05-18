---
Description: 'Adds the job to the scheduling queue using the job object to identify the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'de008263-41ed-43a8-9a91-7b29739d348a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::SubmitJob method'
---

# IScheduler::SubmitJob method

Adds the job to the scheduling queue using the job object to identify the job.

## Syntax


```C++
HRESULT SubmitJob(
  [in] ISchedulerJob *job,
  [in] BSTR          username,
  [in] BSTR          password
);
```



## Parameters

<dl> <dt>

*job* \[in\]
</dt> <dd>

An [**ISchedulerJob**](ischedulerjob.md) interface that identifies the job to add to the scheduling queue.

</dd> <dt>

*username* \[in\]
</dt> <dd>

The name of the RunAs user, in the form *domain*\\*username*. The user name is limited to 80 Unicode characters.

If this parameter is **NULL**, the method uses the name in [**ISchedulerJob.UserName**](ischedulerjob-username.md), if set; otherwise, the method uses the owner of the job.

If this parameter is an empty string, the service searches the credentials cache for the credentials to use. If the cache contains the credentials for a single user, those credentials are used. However, if multiple credentials exist in the cache, the user is prompted for the credentials.

</dd> <dt>

*password* \[in\]
</dt> <dd>

The password for the RunAs user. The password is limited to 127 Unicode characters.

If this parameter is **NULL** or empty, the method uses the cached password if cached; otherwise, the user is prompted for the password. If your application is a Windows application, you must call the [**IScheduler::SetInterfaceMode**](ischeduler-setinterfacemode.md) method to specify the parent window for the credentials dialog box.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

If the specified job does not exist in the scheduler, the method adds the job to the scheduler before adding the job to the scheduling queue.

If the submit succeeds, the state of the job is Submitted (see [**JobState**](jobstate.md)). After the job is validated, the job moves to the Queued state. The job moves to the Running state when all required resources are available and the scheduler starts the job.

Tasks are started in the order in which they were added to the job, except if there is a dependency (see the [**ISchedulerTask::DependsOn**](ischedulertask-dependson.md) property).

You can call the **SubmitJob** method on a job that does not contain tasks to reserve resources for the job. If the job's [**RunUntilCanceled**](ischedulerjob-rununtilcanceled.md) property is VARIANT\_TRUE, the job is scheduled and runs indefinitely or until it exceeds the run-time limit set in the job's [**Runtime**](ischedulerjob-runtime.md) property (then the job is canceled). If the **RunUntilCanceled** property is VARIANT\_FALSE, the job moves to the Finished state.

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

[**IScheduler::AddJob**](ischeduler-addjob.md)
</dt> <dt>

[**IScheduler::CreateJob**](ischeduler-createjob.md)
</dt> <dt>

[**IScheduler::CancelJob**](ischeduler-canceljob.md)
</dt> <dt>

[**IScheduler::OpenJob**](ischeduler-openjob.md)
</dt> <dt>

[**IScheduler::SubmitJobById**](ischeduler-submitjob-2.md)
</dt> </dl>

 

 




