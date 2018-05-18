---
Description: 'Cancels the specified job and provides a message to the user that explains why you canceled the job, and optionally forces the job to stop immediately.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '154974DB-F23B-422C-8F4B-0D584CACBFDC'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::CancelJob\_2 method'
---

# IScheduler::CancelJob\_2 method

Cancels the specified job and provides a message to the user that explains why you canceled the job, and optionally forces the job to stop immediately.

## Syntax


```C++
HRESULT CancelJob_2(
  [in] long         JobId,
  [in] BSTR         Message,
  [in] VARIANT_BOOL isForced    
);
```



## Parameters

<dl> <dt>

*JobId* \[in\]
</dt> <dd>

A long integer that specifies the identifier of the job that you want to cancel.

</dd> <dt>

*Message* \[in\]
</dt> <dd>

A string that specifies a message that describes the reason why you canceled the job. The message is limited to 320 characters, or it can be empty. The message is stored with the job. To get the message, use the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

</dd> <dt>

*isForced* \[in\]
</dt> <dd>

A VARIANT\_BOOL that specifies whether to stop the job immediately without using the grace period for canceling the tasks in the job and without running the Node Release task, if the job contains one.

VARIANT\_TRUE indicates that the method should stop the job immediately without using the grace period for canceling the tasks in the job and without running the Node Release task. VARIANT\_FALSE indicates that the method should not stop the job immediately and should use the grace period for canceling the tasks in the job and run the Node Release task.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Remarks

When you force the job to stop immediately, this method ignores the grace period for canceling the tasks in the job, and it does not run the Node Release task for the job.

This method removes the job from the queue, but the job remains in the scheduler. The TTLCompletedJobs cluster parameter determines when the job is removed from the scheduler after you have canceled the job. For information about the TTLCompletedJobs cluster parameter, see [**IScheduler::SetClusterParameter**](ischeduler-setclusterparameter.md).

To cancel a job, the state of the job must be Configuring, Submitted, Validating, Queued, or Running. If tasks in the job are running when you cancel the job, the tasks are stopped and marked as failed. If you queue the job again, the tasks in the job are treated as follows:

-   Tasks that were finished when you canceled the job stay finished.
-   Tasks that were explicitly canceled before they ran and that are currently in the canceled state stay canceled.
-   All other tasks are queued, including those that failed.

To cancel a command job, the user must be a cluster administrator.

Calling the [**IScheduler::CancelJob**](ischeduler-canceljob.md) method is equivalent to calling the **IScheduler::CancelJob\_2** with the *isForced* parameter set to VARIANT\_FALSE.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::CancelJob**](ischeduler-canceljob.md)
</dt> <dt>

[**IScheduler::AddJob**](ischeduler-addjob.md)
</dt> <dt>

[**IScheduler::CreateJob**](ischeduler-createjob.md)
</dt> <dt>

[**IScheduler::SubmitJob**](ischeduler-submitjob.md)
</dt> <dt>

[**IScheduler::SubmitJobById**](ischeduler-submitjob-2.md)
</dt> </dl>

 

 




