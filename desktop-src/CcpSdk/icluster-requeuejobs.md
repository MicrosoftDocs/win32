---
Description: 'Queues one or more specified jobs again.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'fd9910c0-f934-4f48-99d8-f9436d06e22c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::RequeueJobs method'
---

# ICluster::RequeueJobs method

Queues one or more specified jobs again.

## Syntax


```C++
HRESULT RequeueJobs(
  [in] IClusterEnumerable *jobIds
);
```



## Parameters

<dl> <dt>

*jobIds* \[in\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains the identifiers of one or more jobs to queue again. The [**ICluster::AddJob**](icluster-addjob.md) method returns the identifier. If you have an instance of the job that has already been added to the cluster, you can call the [**IJob::get\_Id**](ijob-get-id.md) method to get the identifier. The variant type of each item in the collection is VT\_I4. Set the **lVal** member of the variant to the identifier.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

Typically, you call this method if tasks in the jobs have failed for similar reasons, you fixed the cause of the failure, and you want to try running the tasks again. Note that to restart a job, all tasks in the job must have the [**IsRerunnable**](itask-put-isrerunnable.md) property set to true. Canceled tasks are not rerun; only failed tasks are rerun. To rerun canceled tasks, you must call the [**ICluster::RequeueTask**](icluster-requeuetask.md) method.

If you call this method while tasks are running, the tasks are canceled. You cannot call this method for a completed job.

If this method fails to queue a job, all subsequent jobs in the collection are also not queued. Jobs that were queued before the failure remain queued.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::RequeueJob**](icluster-requeuejob.md)
</dt> <dt>

[**ICluster::RequeueTasks**](icluster-requeuetasks.md)
</dt> </dl>

 

 




