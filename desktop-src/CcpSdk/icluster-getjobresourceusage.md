---
Description: 'Retrieves the resource usage information for the specified job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'bca29da0-bba5-4d87-8684-bc8f323e4c63'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::GetJobResourceUsage method'
---

# ICluster::GetJobResourceUsage method

Retrieves the resource usage information for the specified job.

## Syntax


```C++
HRESULT GetJobResourceUsage(
  [in]  long           jobId,
  [out] IResourceUsage **pRetVal
);
```



## Parameters

<dl> <dt>

*jobId* \[in\]
</dt> <dd>

The job identifier. The [**IJob::get\_Id**](ijob-get-id.md) and [**ICluster::AddJob**](icluster-addjob.md) methods return this value.

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IResourceUsage**](iresourceusage.md) interface that contains information about the amount of resources used by the job.

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

[**ICluster::GetJobCounter**](icluster-getjobcounter.md)
</dt> <dt>

[**ICluster::GetTaskResourceUsage**](icluster-gettaskresourceusage.md)
</dt> </dl>

 

 




