---
Description: 'Retrieves the total CPU time used by all tasks in the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3c3fc546-fdfc-4931-9a54-d80592603b6e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJobCounters::TotalCpuTime property'
---

# ISchedulerJobCounters::TotalCpuTime property

Retrieves the total CPU time used by all tasks in the job.

This property is read-only.

## Syntax


```C++
HRESULT get_TotalCpuTime(
  [out] __int64 *pTotalCpuTime
);
```



## Property value

The total CPU time, in milliseconds.

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

 

 




