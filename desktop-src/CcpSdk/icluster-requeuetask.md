---
Description: 'Queues the specified task again.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '76f87323-910f-442e-834b-e0aac96f4300'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::RequeueTask method'
---

# ICluster::RequeueTask method

Queues the specified task again.

## Syntax


```C++
HRESULT RequeueTask(
  [in] long jobId,
  [in] long taskId
);
```



## Parameters

<dl> <dt>

*jobId* \[in\]
</dt> <dd>

The job identifier. The [**ICluster::AddJob**](icluster-addjob.md) method returns this value. If you have an instance of the job that has already been added to the cluster, you can call the [**IJob::get\_Id**](ijob-get-id.md) method to get the identifier.

</dd> <dt>

*taskId* \[in\]
</dt> <dd>

The task identifier. The [**ITask::get\_Id**](itask-get-id.md) method returns this value.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

Typically, you call this method if the task failed, you fixed the cause of the failure, and you want to try running the task again.

If you call this method while the task is running, the task is canceled. You cannot call this method for a completed task.

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

 

 




