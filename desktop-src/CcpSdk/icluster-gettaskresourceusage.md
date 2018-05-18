---
Description: 'Retrieves the resource usage information for the specified task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '0ba15764-2b80-4f52-9ca5-ae256047fb80'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::GetTaskResourceUsage method'
---

# ICluster::GetTaskResourceUsage method

Retrieves the resource usage information for the specified task.

## Syntax


```C++
HRESULT GetTaskResourceUsage(
  [in]  long           jobId,
  [in]  long           taskId,
  [out] IResourceUsage **pRetVal
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

An [**IResourceUsage**](iresourceusage.md) interface that contains information about the amount of resources used by the task.

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

[**ICluster::GetJobResourceUsage**](icluster-getjobresourceusage.md)
</dt> </dl>

 

 




