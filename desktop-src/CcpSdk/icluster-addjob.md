---
Description: 'Adds the specified job to the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd77b76ec-bcb2-46e3-a5ea-4ebc2a082dea'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::AddJob method'
---

# ICluster::AddJob method

Adds the specified job to the cluster.

## Syntax


```C++
HRESULT AddJob(
  [in]  IJob *Job,
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*Job* \[in\]
</dt> <dd>

An [**IJob**](ijob.md) interface that identifies the job to add to the cluster.

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

The identifier of the job that was added to the cluster. The identifier is unique within the cluster. Use the identifier to [add tasks](icluster-addtask.md) to the job and to [submit](icluster-submitjob.md) or [retrieve](icluster-getjob.md) the job.

Note that identifiers for jobs that are no longer in the cluster are reused.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

To get an [**IJob**](ijob.md) interface pointer, call the [**ICluster::CreateJob**](icluster-createjob.md) method. You can also call the [**ICluster::GetJob**](icluster-getjob.md) method or one of the list methods to get an existing job to use as a template for adding similar jobs (or the same job) to the cluster.

After you have added the job to the cluster, you must use the [**ICluster::ModifyJob**](icluster-modifyjob.md) or [**ICluster::ModifyJobTerm**](icluster-modifyjobterm.md) method to update the terms of the job.

If the job contains tasks, call the [**ICluster::SubmitJob**](icluster-submitjob.md) method to add the job to the scheduling queue. If the job does not contain tasks, call the [**ICluster::AddTask**](icluster-addtask.md) method to add a task to the job before calling the **SubmitJob** method.

Note that you can call the [**SubmitJob**](icluster-submitjob.md) method on a job that does not contain tasks to reserve resources for the job. If the [**IJob::put\_RunUntilCanceled**](ijob-put-rununtilcanceled.md) method's *pRetVal* parameter is VARIANT\_TRUE, the job is scheduled and runs indefinitely or until it exceeds the run-time limit set in the [**IJob::put\_Runtime**](ijob-put-runtime.md) method (then the job is canceled). If the **put\_RunUntilCanceled** method's *pRetVal* parameter is VARIANT\_FALSE, the job moves to the finished status.

As an alternative to calling both the **AddJob** and [**SubmitJob**](icluster-submitjob.md) methods, you can call the [**ICluster::QueueJob**](icluster-queuejob.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::AddJobs**](icluster-addjobs.md)
</dt> <dt>

[**ICluster::CancelJob**](icluster-canceljob.md)
</dt> <dt>

[**ICluster::ListJobs**](icluster-listjobs.md)
</dt> </dl>

 

 




