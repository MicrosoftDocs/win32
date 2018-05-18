---
Description: 'Gets the number of tasks in the job that the scheduler is sending to a node to run.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '869AE473-7C72-4038-9F5B-E55DB7D40500'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJobCounters::DispatchingTaskCount property'
---

# ISchedulerJobCounters::DispatchingTaskCount property

Gets the number of tasks in the job that the scheduler is sending to a node to run.

This property is read-only.

## Syntax


```C++
HRESULT get_DispatchingTaskCount(
  [out, retval] long *pRetVal
);
```



## Property value

The number of tasks in the job that the scheduler is sending to a node to run.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJobCounters**](ischedulerjobcounters.md)
</dt> </dl>

 

 




