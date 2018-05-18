---
Description: 'Retrieves the total number of tasks in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'db99fd88-0f67-431d-9dcc-9a23025c57e2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::TotalTasks property'
---

# ISchedulerCounters::TotalTasks property

Retrieves the total number of tasks in the cluster.

This property is read-only.

## Syntax


```C++
HRESULT get_TotalTasks(
  [out] long *pTotalTasks
);
```



## Property value

The total number of tasks in the cluster.

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

 

 




