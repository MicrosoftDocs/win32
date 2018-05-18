---
Description: 'Retrieves the total number of jobs in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd8f98b5f-16da-4241-916e-988862917b01'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::TotalJobs property'
---

# ISchedulerCounters::TotalJobs property

Retrieves the total number of jobs in the cluster.

This property is read-only.

## Syntax


```C++
HRESULT get_TotalJobs(
  [out] long *pTotalJobs
);
```



## Property value

The total number of jobs in the cluster.

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

 

 




