---
Description: 'Retrieves the number of tasks that are running.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'baeac99b-43d2-416d-b90d-f26599e5609b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJobCounters::RunningTaskCount property'
---

# ISchedulerJobCounters::RunningTaskCount property

Retrieves the number of tasks that are running.

This property is read-only.

## Syntax


```C++
HRESULT get_RunningTaskCount(
  [out] long *pRunningTaskCount
);
```



## Property value

The number of tasks that are running.

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

 

 




