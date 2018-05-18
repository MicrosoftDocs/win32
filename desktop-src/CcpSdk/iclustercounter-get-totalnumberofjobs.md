---
Description: 'Retrieves the number of jobs in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '6787f2db-3f01-44ce-90a4-74cf9963e0c9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IClusterCounter::get\_TotalNumberOfJobs method'
---

# IClusterCounter::get\_TotalNumberOfJobs method

Retrieves the number of jobs in the cluster.

## Syntax


```C++
HRESULT get_TotalNumberOfJobs(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The number of jobs in the cluster.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The count includes jobs that are added to the cluster using [**ICluster::AddJob**](icluster-addjob.md), [**ICluster::SubmitJob**](icluster-submitjob.md), or [**ICluster::QueueJob**](icluster-queuejob.md) (or their plural equivalents).

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IClusterCounter**](iclustercounter.md)
</dt> </dl>

 

 




