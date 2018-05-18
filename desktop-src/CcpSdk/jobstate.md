---
Description: 'Defines the state of the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2a1e369f-6a76-4b6d-b12b-c06157c45096'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: JobState enumeration
---

# JobState enumeration

Defines the state of the job.

## Syntax


```C++
typedef enum  { 
  JobState_Configuring         = 1,
  JobState_Submitted           = 2,
  JobState_Validating          = 4,
  JobState_ExternalValidation  = 8,
  JobState_Queued              = 16,
  JobState_Running             = 32,
  JobState_Finishing           = 64,
  JobState_Finished            = 128,
  JobState_Failed              = 256,
  JobState_Canceled            = 512,
  JobState_Canceling           = 1024,
  JobState_All                 = 2047
} JobState;
```



## Constants

<dl> <dt>

<span id="JobState_Configuring"></span><span id="jobstate_configuring"></span><span id="JOBSTATE_CONFIGURING"></span>**JobState\_Configuring**
</dt> <dd>

The job is being configured. The job remains in the configuring state until you call the [**IScheduler::SubmitJob**](ischeduler-submitjob.md) method to add the job to the scheduling queue.

</dd> <dt>

<span id="JobState_Submitted"></span><span id="jobstate_submitted"></span><span id="JOBSTATE_SUBMITTED"></span>**JobState\_Submitted**
</dt> <dd>

The job was submitted to the scheduling queue (see [**SubmitJob**](ischeduler-submitjob.md)) and is waiting to be validated.

</dd> <dt>

<span id="JobState_Validating"></span><span id="jobstate_validating"></span><span id="JOBSTATE_VALIDATING"></span>**JobState\_Validating**
</dt> <dd>

The server is determining if the job can run. If the server and external validation filters have successfully validated the job, it is then queued.

</dd> <dt>

<span id="JobState_ExternalValidation"></span><span id="jobstate_externalvalidation"></span><span id="JOBSTATE_EXTERNALVALIDATION"></span>**JobState\_ExternalValidation**
</dt> <dd>

A submission filter is determining if the job can run. For details, see the *SubmissionFilterProgram* cluster parameter in the Remarks section of [**IScheduler::SetClusterParameter**](ischeduler-setclusterparameter.md).

</dd> <dt>

<span id="JobState_Queued"></span><span id="jobstate_queued"></span><span id="JOBSTATE_QUEUED"></span>**JobState\_Queued**
</dt> <dd>

The job passed validation and was added to the scheduling queue.

</dd> <dt>

<span id="JobState_Running"></span><span id="jobstate_running"></span><span id="JOBSTATE_RUNNING"></span>**JobState\_Running**
</dt> <dd>

The job is running.

</dd> <dt>

<span id="JobState_Finishing"></span><span id="jobstate_finishing"></span><span id="JOBSTATE_FINISHING"></span>**JobState\_Finishing**
</dt> <dd>

The server is cleaning up the resources that were allocated to the job.

</dd> <dt>

<span id="JobState_Finished"></span><span id="jobstate_finished"></span><span id="JOBSTATE_FINISHED"></span>**JobState\_Finished**
</dt> <dd>

The job successfully finished (all the tasks in the job finished successfully).

</dd> <dt>

<span id="JobState_Failed"></span><span id="jobstate_failed"></span><span id="JOBSTATE_FAILED"></span>**JobState\_Failed**
</dt> <dd>

One or more of the tasks in the job failed or a system error occurred on the compute node. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) job property.

</dd> <dt>

<span id="JobState_Canceled"></span><span id="jobstate_canceled"></span><span id="JOBSTATE_CANCELED"></span>**JobState\_Canceled**
</dt> <dd>

The job was canceled (see [**IScheduler::CancelJob**](ischeduler-canceljob.md)). If the caller provided the reason for canceling the job, then the [**ErrorMessage**](ischedulerjob-errormessage.md) job property will contain the reason.

</dd> <dt>

<span id="JobState_Canceling"></span><span id="jobstate_canceling"></span><span id="JOBSTATE_CANCELING"></span>**JobState\_Canceling**
</dt> <dd>

The job is being canceled.

</dd> <dt>

<span id="JobState_All"></span><span id="jobstate_all"></span><span id="JOBSTATE_ALL"></span>**JobState\_All**
</dt> <dd>

A mask used to indicate all states.

</dd> </dl>

## Remarks

A job can be in only one state. The states are specified as flags, so you can specify multiple states when filtering jobs. For example, you can retrieve jobs that are in both the Canceled and Finished states.

## Requirements



|                         |                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.Properties.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Enumerations](hpc-enumerations.md)
</dt> <dt>

[**ISchedulerJob.State**](ischedulerjob-state.md)
</dt> <dt>

[**ISchedulerJob.PreviousState**](ischedulerjob-previousstate.md)
</dt> </dl>

 

 




