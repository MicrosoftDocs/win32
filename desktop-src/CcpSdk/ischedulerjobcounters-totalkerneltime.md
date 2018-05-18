---
Description: 'Retrieves the elapsed execution time for kernel-mode instructions (the total time that all tasks in the job spent in kernel-mode).'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '36f50a02-864c-41e9-bf53-8a0bfaf4920f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJobCounters::TotalKernelTime property'
---

# ISchedulerJobCounters::TotalKernelTime property

Retrieves the elapsed execution time for kernel-mode instructions (the total time that all tasks in the job spent in kernel-mode).

This property is read-only.

## Syntax


```C++
HRESULT get_TotalKernelTime(
  [out] __int64 *pTotalKernelTime
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

[**ISchedulerJobCounters**](ischedulerjobcounters.md)
</dt> </dl>

 

 




