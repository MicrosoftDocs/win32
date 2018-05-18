---
Description: 'Retrieves the number of jobs that are in the scheduling queue.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'aa474a21-0f5a-46db-b126-07abf4b11e2e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::QueuedJobs property'
---

# ISchedulerCounters::QueuedJobs property

Retrieves the number of jobs that are in the scheduling queue.

This property is read-only.

## Syntax


```C++
HRESULT get_QueuedJobs(
  [out] long *pQueuedJobs
);
```



## Property value

The number of jobs that are in the scheduling queue.

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

 

 




