---
Description: 'Retrieves a task from the specified job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a0eb70ee-fb01-48f5-a5fa-6f53a0444053'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::GetTask method'
---

# ICluster::GetTask method

Retrieves a task from the specified job.

## Syntax


```C++
HRESULT GetTask(
  [in]  long  jobId,
  [in]  long  taskId,
  [out] ITask **pRetVal
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

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**ITask**](itask.md) interface that represents the specified task.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::AddTask**](icluster-addtask.md)
</dt> <dt>

[**ICluster::CancelTask**](icluster-canceltask.md)
</dt> <dt>

[**ICluster::GetJob**](icluster-getjob.md)
</dt> <dt>

[**ICluster::ListTasks**](icluster-listtasks.md)
</dt> <dt>

[**IJob::GetTask**](ijob-gettask.md)
</dt> </dl>

 

 




