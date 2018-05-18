---
Description: 'Retrieves the total CPU time used by all tasks that are running in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f29cd463-0406-4d55-93e6-def3e5a64b95'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTaskCounters::TotalCpuTime property'
---

# ISchedulerTaskCounters::TotalCpuTime property

Retrieves the total CPU time used by all tasks that are running in the cluster.

This property is read-only.

## Syntax


```C++
HRESULT get_TotalCpuTime(
  [out] __int64 pTotalCpuTime
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

[**ISchedulerTaskCounters**](ischedulertaskcounters.md)
</dt> </dl>

 

 




