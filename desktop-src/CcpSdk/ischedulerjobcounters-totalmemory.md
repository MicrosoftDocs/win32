---
Description: 'Retrieves the total amount of memory used by the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '0ec305eb-e5b7-454b-91bf-35b0472f03b7'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJobCounters::TotalMemory property'
---

# ISchedulerJobCounters::TotalMemory property

Retrieves the total amount of memory used by the job.

This property is read-only.

## Syntax


```C++
HRESULT get_TotalMemory(
  [out] __int64 *pTotalMemory
);
```



## Property value

The total amount of memory, in bytes, used by the job.

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

 

 




