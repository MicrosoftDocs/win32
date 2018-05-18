---
Description: 'Retrieves the elapsed execution time for kernel-mode instructions (the total time that all tasks that are running in the cluster have spent in kernel-mode).'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'bd3f816c-654a-4cfb-962a-336ba81d0fbb'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTaskCounters::TotalKernelTime property'
---

# ISchedulerTaskCounters::TotalKernelTime property

Retrieves the elapsed execution time for kernel-mode instructions (the total time that all tasks that are running in the cluster have spent in kernel-mode).

This property is read-only.

## Syntax


```C++
HRESULT get_TotalKernelTime(
  [out] __int64 pTotalKernelTime
);
```



## Property value

The total kernel-mode time, in milliseconds.

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

 

 




