---
Description: 'Retrieves counter information for a specified job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7ae2ce16-ed5d-4c3a-8b6a-16db9a54d8f2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::GetJobCounter method'
---

# ICluster::GetJobCounter method

Retrieves counter information for a specified job.

## Syntax


```C++
HRESULT GetJobCounter(
  [in]  long        jobId,
  [out] IJobCounter **pRetVal
);
```



## Parameters

<dl> <dt>

*jobId* \[in\]
</dt> <dd>

The job identifier. The [**ICluster::AddJob**](icluster-addjob.md) method returns this value. If you have an instance of the job that has already been added to the cluster, you can call the [**IJob::get\_Id**](ijob-get-id.md) method to get the identifier.

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IJobCounter**](ijobcounter.md) interface that contains information about the tasks in the job. For example, this parameter can indicate the number of tasks that are running or have finished.

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

[**ICluster::get\_ClusterCounter**](icluster-get-clustercounter.md)
</dt> <dt>

[**ICluster::GetJobResourceUsage**](icluster-getjobresourceusage.md)
</dt> </dl>

 

 




