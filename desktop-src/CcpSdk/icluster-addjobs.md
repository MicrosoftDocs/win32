---
Description: 'Adds one or more specified jobs to the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '015002ec-76fb-46a7-a6b4-bd04ed910d34'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::AddJobs method'
---

# ICluster::AddJobs method

Adds one or more specified jobs to the cluster.

## Syntax


```C++
HRESULT AddJobs(
  [in]  IClusterEnumerable *jobs,
  [out] IClusterEnumerable **pRetVal
);
```



## Parameters

<dl> <dt>

*jobs* \[in\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains one or more [**IJob**](ijob.md) interfaces to the jobs that you want to add to the cluster.

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains the identifiers of the jobs that were added to the cluster. The identifiers in this collection correspond directly to the jobs passed in the *jobs* parameter. Use the identifier to [add tasks](icluster-addtask.md) to the job and to [submit](icluster-submitjob.md) or [retrieve](icluster-getjob.md) the job.

When you enumerate the identifiers in this collection, the identifiers are returned as variants. The variant type is VT\_I4. Use the **lVal** member of the variant to access the identifier.

Note that identifiers for jobs that are no longer in the cluster are reused.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

If you need to add multiple jobs to the cluster, calling this method provides better performance than calling the [**ICluster::AddJob**](icluster-addjob.md) method in a loop.

If this method fails to add one of the jobs to the cluster, none of the jobs are added to the cluster.

For an example that shows how to create the enumerable object for the *jobs* parameter and how to add jobs to it, see the [Submitting a Job to the Scheduling Queue](submitting-a-job-to-the-scheduling-queue.md).

After you have added the job to the cluster, you must use the [**ICluster::ModifyJob**](icluster-modifyjob.md) or [**ICluster::ModifyJobTerm**](icluster-modifyjobterm.md) method to update the terms of the job.

If each job contains at least one task, call the [**ICluster::SubmitJobs**](icluster-submitjobs.md) method to add the jobs to the scheduling queue. If any jobs do not contain at least one task, call the [**ICluster::AddTask**](icluster-addtask.md) method to add at least one task to those jobs before calling the **SubmitJobs** method.

Note that you can call the [**SubmitJobs**](icluster-submitjobs.md) method on jobs that do not contain tasks to reserve resources for the jobs. If the [**IJob::put\_RunUntilCanceled**](ijob-put-rununtilcanceled.md) method's *pRetVal* parameter is VARIANT\_TRUE, the job is scheduled and runs indefinitely or until it exceeds the run-time limit set in the [**IJob::put\_Runtime**](ijob-put-runtime.md) method (then the job is canceled). If the **put\_RunUntilCanceled** method's *pRetVal* parameter is VARIANT\_FALSE, the job moves to the finished status.

As an alternative to calling both the **AddJobs** and [**SubmitJobs**](icluster-submitjobs.md) methods, you can call the [**ICluster::QueueJobs**](icluster-queuejobs.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::AddJob**](icluster-addjob.md)
</dt> <dt>

[**ICluster::CancelJobs**](icluster-canceljob.md)
</dt> <dt>

[**ICluster::ListJobs**](icluster-listjobs.md)
</dt> </dl>

 

 




