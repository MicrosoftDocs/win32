---
Description: 'Retrieves the number of tasks that are in the process of being canceled.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a96186f5-5982-4033-b701-869152a27c7d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::CancelingTasks property'
---

# ISchedulerCounters::CancelingTasks property

Retrieves the number of tasks that are in the process of being canceled.

This property is read-only.

## Syntax


```C++
HRESULT get_CancelingTasks(
  [out] long *pCancelingTasks
);
```



## Property value

The number of tasks that are in the process of being canceled.

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

 

 




