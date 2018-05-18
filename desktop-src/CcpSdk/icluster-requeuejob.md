---
Description: 'Queues the specified job again.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9b4d85ea-b16a-44ae-a20a-e38716c99834'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::RequeueJob method'
---

# ICluster::RequeueJob method

Queues the specified job again.

## Syntax


```C++
HRESULT RequeueJob(
  [in] long jobId
);
```



## Parameters

<dl> <dt>

*jobId* \[in\]
</dt> <dd>

The job identifier. The [**ICluster::AddJob**](icluster-addjob.md) method returns this value. If you have an instance of the job that has already been added to the cluster, you can call the [**IJob::get\_Id**](ijob-get-id.md) method to get the identifier.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

Typically, you call this method if tasks in the job have failed, you fixed the cause of the failure, and you want to try running the tasks again. Note that to restart a job, all tasks in the job must have the [**IsRerunnable**](itask-put-isrerunnable.md) property set to true. Canceled tasks are not rerun; only failed tasks are rerun. To rerun canceled tasks, you must call the [**ICluster::RequeueTask**](icluster-requeuetask.md) method.

If you call this method while tasks are running, the tasks are canceled. You cannot call this method for a completed job.

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

 

 




