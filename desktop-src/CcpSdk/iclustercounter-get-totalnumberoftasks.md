---
Description: 'Retrieves the number of tasks in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1ebc9029-3cad-48d7-b3c6-02025eab6297'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IClusterCounter::get\_TotalNumberOfTasks method'
---

# IClusterCounter::get\_TotalNumberOfTasks method

Retrieves the number of tasks in the cluster.

## Syntax


```C++
HRESULT get_TotalNumberOfTasks(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The number of tasks in the cluster.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The count includes those tasks contained in jobs that have been added to the cluster using [**ICluster::AddJob**](icluster-addjob.md), [**ICluster::SubmitJob**](icluster-submitjob.md), or [**ICluster::QueueJob**](icluster-queuejob.md) (or their plural equivalents). The count does not include tasks that are [executed as commands](icluster-executecommand.md).

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IClusterCounter**](iclustercounter.md)
</dt> </dl>

 

 




