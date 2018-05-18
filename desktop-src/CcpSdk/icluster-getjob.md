---
Description: 'Retrieves a job from the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'cfcde76b-b161-4e99-b156-cc2d54856f62'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::GetJob method'
---

# ICluster::GetJob method

Retrieves a job from the cluster.

## Syntax


```C++
HRESULT GetJob(
  [in]  long jobId,
  [out] IJob **pRetVal
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

An [**IJob**](ijob.md) interface that represents the specified job.

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

[**ICluster::AddJob**](icluster-addjob.md)
</dt> <dt>

[**ICluster::CancelJob**](icluster-canceljob.md)
</dt> <dt>

[**ICluster::CreateJob**](icluster-createjob.md)
</dt> <dt>

[**ICluster::GetTask**](icluster-gettask.md)
</dt> <dt>

[**ICluster::ListJobs**](icluster-listjobs.md)
</dt> </dl>

 

 




