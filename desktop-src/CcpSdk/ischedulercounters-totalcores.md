---
Description: 'Retrieves the total number of cores in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '321dddee-2e39-4aa4-b921-5373a99d3dd8'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::TotalCores property'
---

# ISchedulerCounters::TotalCores property

Retrieves the total number of cores in the cluster.

This property is read-only.

## Syntax


```C++
HRESULT get_TotalCores(
  [out] long *pTotalCores
);
```



## Property value

The total number of cores in the cluster.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerCounters**](ischedulercounters.md)
</dt> </dl>

 

 




