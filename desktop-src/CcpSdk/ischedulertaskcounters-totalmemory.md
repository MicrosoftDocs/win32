---
Description: 'Retrieves the total memory used by all tasks that are running in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '63e1242f-30c5-4154-916e-d4c954c1d9c1'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTaskCounters::TotalMemory property'
---

# ISchedulerTaskCounters::TotalMemory property

Retrieves the total memory used by all tasks that are running in the cluster.

This property is read-only.

## Syntax


```C++
HRESULT get_TotalMemory(
  [out] __int64 pTotalMemory
);
```



## Property value

The total memory, in bytes, used by all tasks.

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

 

 




