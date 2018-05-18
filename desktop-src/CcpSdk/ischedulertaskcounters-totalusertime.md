---
Description: 'Retrieves the elapsed execution time for user-mode instructions (the total time that all tasks that are running in the cluster have spent in user-mode).'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3107e0df-9030-4268-b499-0b7f423d3cae'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTaskCounters::TotalUserTime property'
---

# ISchedulerTaskCounters::TotalUserTime property

Retrieves the elapsed execution time for user-mode instructions (the total time that all tasks that are running in the cluster have spent in user-mode).

This property is read-only.

## Syntax


```C++
HRESULT get_TotalUserTime(
  [out] __int64 pTotalUserTime
);
```



## Property value

The total user-mode time, in milliseconds.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTaskCounters**](ischedulertaskcounters.md)
</dt> </dl>

 

 




