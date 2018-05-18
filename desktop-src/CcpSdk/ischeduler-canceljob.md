---
Description: 'Cancels the specified job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b576ec2f-df8e-4378-a927-b33b80ff2f0a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::CancelJob method'
---

# IScheduler::CancelJob method

Cancels the specified job.

## Syntax


```C++
HRESULT CancelJob(
  [in] long jobId,
  [in] BSTR message
);
```



## Parameters

<dl> <dt>

*jobId* \[in\]
</dt> <dd>

The job to cancel. The scheduler assigns the identifier when you call the [**IScheduler::AddJob**](ischeduler-addjob.md) method to add the job to the scheduler. To get the identifier, access the [**ISchedulerJob.Id**](ischedulerjob-id.md) property.

</dd> <dt>

*message* \[in\]
</dt> <dd>

A message that describes the reason why the job was canceled. The message is limited to 320 Unicode characters. Can be empty.

The message is stored with the job. To get the message, access the [**ISchedulerJob.ErrorMessage**](ischedulerjob-errormessage.md) property.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The job is removed from the queue but remains in the scheduler. The TTLCompletedJobs cluster parameter (for details, see the Remarks section of [**IScheduler::SetClusterParameter**](ischeduler-setclusterparameter.md)) determines when the job is removed from the scheduler after it has been canceled.

To cancel a job, the state of the job must be configuring, submitted, validating, queued, or running. If the job is running tasks when the job is canceled, the tasks are stopped and marked as failed. If you queue the job again, the tasks in the job are treated as follows:

-   Tasks that were finished when the job was canceled stay finished.
-   Tasks that were explicitly canceled before they ran and that are currently in the canceled state stay canceled.
-   All other tasks are queued, including those that failed.

To cancel a command job, the user must be running as an administrator.

This method honors all cancelation grace periods for currently running tasks, and runs any node release task that exists for the job on all nodes currently allocated to the job.

To stop the job immediately in Windows HPC Server 2008 R2 without using the grace period for canceling the tasks in the job and without running any node release task that the job includes, use the [**IScheduler::CancelJob\_2**](ischeduler-canceljob-2.md) method. Calling the **IScheduler::CancelJob** method is equivalent to calling the **IScheduler::CancelJob\_2** method with the *isForced* parameter set to VARIANT\_FALSE.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::CancelJob\_2**](ischeduler-canceljob-2.md)
</dt> <dt>

[**IScheduler::AddJob**](ischeduler-addjob.md)
</dt> <dt>

[**IScheduler::CreateJob**](ischeduler-createjob.md)
</dt> <dt>

[**IScheduler::SubmitJob**](ischeduler-submitjob.md)
</dt> <dt>

[**IScheduler::OpenJob**](ischeduler-openjob.md)
</dt> </dl>

 

 




