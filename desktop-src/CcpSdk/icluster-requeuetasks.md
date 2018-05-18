---
Description: 'Queues one or more specified tasks again.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '112981dd-d0f7-4fb9-b0ce-31732585030b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::RequeueTasks method'
---

# ICluster::RequeueTasks method

Queues one or more specified tasks again.

## Syntax


```C++
HRESULT RequeueTasks(
  [in] long               jobId,
  [in] IClusterEnumerable *taskIds
);
```



## Parameters

<dl> <dt>

*jobId* \[in\]
</dt> <dd>

The job identifier. The [**ICluster::AddJob**](icluster-addjob.md) method returns this value. If you have an instance of the job that has already been added to the cluster, you can call the [**IJob::get\_Id**](ijob-get-id.md) method to get the identifier.

</dd> <dt>

*taskIds* \[in\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains the identifiers of one or more tasks to queue again. The [**ITask::get\_Id**](itask-get-id.md) method returns the task identifier value. The variant type of each item in the collection is VT\_I4. Set the **lVal** member of the variant to the identifier.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

Typically, you call this method if the tasks failed for similar reasons, you fixed the cause of the failure, and you want to try running the tasks again.

If you call this method while tasks are running, the tasks are canceled. You cannot call this method for completed tasks.

If the method fails to queue a task, all subsequent tasks in the job are also not queued. Tasks that were queued before the failure remain queued.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::RequeueJobs**](icluster-requeuejobs.md)
</dt> <dt>

[**ICluster::RequeueTask**](icluster-requeuetask.md)
</dt> </dl>

 

 




