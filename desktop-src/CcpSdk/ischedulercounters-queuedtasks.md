---
Description: 'Retrieves the number of tasks that are in the scheduling queue.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '17472b02-ac67-4b12-85fa-e6b9283e1a7a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::QueuedTasks property'
---

# ISchedulerCounters::QueuedTasks property

Retrieves the number of tasks that are in the scheduling queue.

This property is read-only.

## Syntax


```C++
HRESULT get_QueuedTasks(
  [out] long *pQueuedTasks
);
```



## Property value

The number of tasks that are in the scheduling queue.

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

 

 




