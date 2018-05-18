---
Description: 'Retrieves counter information for the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c3f286ca-9d0c-48ea-9a91-fc3e167fa9cf'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::get\_ClusterCounter method'
---

# ICluster::get\_ClusterCounter method

Retrieves counter information for the cluster.

## Syntax


```C++
HRESULT get_ClusterCounter(
  [out]  IClusterCounter **pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IClusterCounter**](iclustercounter.md) interface that contains information about the jobs, tasks, and nodes in the cluster. For example, the counters can indicate the number of jobs that are running or that have finished.

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

[**ICluster::GetJobResourceUsage**](icluster-getjobresourceusage.md)
</dt> </dl>

 

 




