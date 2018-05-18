---
Description: 'Retrieves the number of tasks that have been canceled.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e91bf5dc-8c6a-422e-8af2-cb7dd6766527'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::CanceledTasks property'
---

# ISchedulerCounters::CanceledTasks property

Retrieves the number of tasks that have been canceled.

This property is read-only.

## Syntax


```C++
HRESULT get_CanceledTasks(
  [out] long *pCanceledTasks
);
```



## Property value

The number of tasks that have been canceled.

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

 

 




