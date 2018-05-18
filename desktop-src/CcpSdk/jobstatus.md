---
Description: 'Defines the job status constants.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ae1711df-ce2e-430f-8402-3c2987483c0c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: JobStatus enumeration
---

# JobStatus enumeration

Defines the job status constants.

## Syntax


```C++
typedef enum  { 
  JobStatus_NotSubmitted  = 0,
  JobStatus_Queued        = 1,
  JobStatus_Running       = 2,
  JobStatus_Finished      = 3,
  JobStatus_Failed        = 4,
  JobStatus_Cancelled     = 5
} JobStatus;
```



## Constants

<dl> <dt>

<span id="JobStatus_NotSubmitted"></span><span id="jobstatus_notsubmitted"></span><span id="JOBSTATUS_NOTSUBMITTED"></span>**JobStatus\_NotSubmitted**
</dt> <dd>

The job was added to the cluster but not to the scheduling queue. The application called the [**ICluster::AddJob**](icluster-addjob.md) or [**ICluster::AddJobs**](icluster-addjobs.md) method to add the job to the cluster.

</dd> <dt>

<span id="JobStatus_Queued"></span><span id="jobstatus_queued"></span><span id="JOBSTATUS_QUEUED"></span>**JobStatus\_Queued**
</dt> <dd>

The job was added to the scheduling queue. The application called the [**ICluster::SubmitJob**](icluster-submitjob.md), [**ICluster::SubmitJobs**](icluster-submitjobs.md), [**ICluster::QueueJob**](icluster-queuejob.md), or [**ICluster::QueueJobs**](icluster-queuejobs.md) method to add the job to the scheduling queue.

</dd> <dt>

<span id="JobStatus_Running"></span><span id="jobstatus_running"></span><span id="JOBSTATUS_RUNNING"></span>**JobStatus\_Running**
</dt> <dd>

The job is running.

</dd> <dt>

<span id="JobStatus_Finished"></span><span id="jobstatus_finished"></span><span id="JOBSTATUS_FINISHED"></span>**JobStatus\_Finished**
</dt> <dd>

The job successfully finished (all the tasks in the job finished successfully).

</dd> <dt>

<span id="JobStatus_Failed"></span><span id="jobstatus_failed"></span><span id="JOBSTATUS_FAILED"></span>**JobStatus\_Failed**
</dt> <dd>

One or more of the tasks in the job failed or a system error occurred on the compute node. To get a description of the error, call the [**IJob::get\_ErrorMessage**](ijob-get-errormessage.md) method.

</dd> <dt>

<span id="JobStatus_Cancelled"></span><span id="jobstatus_cancelled"></span><span id="JOBSTATUS_CANCELLED"></span>**JobStatus\_Cancelled**
</dt> <dd>

The job was canceled by the application. The application called the [**ICluster::CancelJob**](icluster-canceljob.md) or [**ICluster:: CancelJobs**](icluster-canceljobs.md) method to cancel the job. If the caller provided the reason for canceling the job, then the [**IJob::get\_ErrorMessage**](ijob-get-errormessage.md) method will contain that reason.

</dd> </dl>

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[CCP Enumerations](enumeration-types.md)
</dt> <dt>

[**ICluster::ListJobs**](icluster-listjobs.md)
</dt> <dt>

[**IJob::get\_Status**](ijob-get-status.md)
</dt> </dl>

 

 




