---
Description: 'Retrieves the number of tasks that are running.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e48c2430-7530-4908-9be6-81b4aede4410'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::RunningTasks property'
---

# ISchedulerCounters::RunningTasks property

Retrieves the number of tasks that are running.

This property is read-only.

## Syntax


```C++
HRESULT get_RunningTasks(
  [out] long *pRunningTasks
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

[**ISchedulerCounters**](ischedulercounters.md)
</dt> </dl>

 

 




