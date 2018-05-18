---
Description: 'Retrieves the number of tasks that are queued and ready to run.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a4a8f92e-d7e3-4267-a155-e016939dbec9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJobCounters::QueuedTaskCount property'
---

# ISchedulerJobCounters::QueuedTaskCount property

Retrieves the number of tasks that are queued and ready to run.

This property is read-only.

## Syntax


```C++
HRESULT get_QueuedTaskCount(
  [out] long *pQueuedTaskCount
);
```



## Property value

The number of tasks that are queued.

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

 

 




