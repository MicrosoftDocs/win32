---
Description: 'Retrieves the elapsed execution time for user-mode instructions (the total time that all tasks in the job spent in user-mode).'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a59fa128-60c2-4d78-a47c-2764e38b7680'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJobCounters::TotalUserTime property'
---

# ISchedulerJobCounters::TotalUserTime property

Retrieves the elapsed execution time for user-mode instructions (the total time that all tasks in the job spent in user-mode).

This property is read-only.

## Syntax


```C++
HRESULT get_TotalUserTime(
  [out] __int64 *pTotalUserTime
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

[**ISchedulerJobCounters**](ischedulerjobcounters.md)
</dt> </dl>

 

 




