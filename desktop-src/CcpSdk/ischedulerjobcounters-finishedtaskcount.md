---
Description: 'Retrieves the number of tasks that have finished.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8601a09b-4684-47be-a8fa-97d8222c2e00'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJobCounters::FinishedTaskCount property'
---

# ISchedulerJobCounters::FinishedTaskCount property

Retrieves the number of tasks that have finished.

This property is read-only.

## Syntax


```C++
HRESULT get_FinishedTaskCount(
  [out] long *pFinishedTaskCount
);
```



## Property value

The number of tasks that have finished.

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

 

 




