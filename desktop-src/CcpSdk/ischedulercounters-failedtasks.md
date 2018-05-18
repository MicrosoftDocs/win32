---
Description: 'Retrieves the number of tasks that failed.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '056d2326-cdb4-46ae-afe3-c2c0a14094c7'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::FailedTasks property'
---

# ISchedulerCounters::FailedTasks property

Retrieves the number of tasks that failed.

This property is read-only.

## Syntax


```C++
HRESULT get_FailedTasks(
  [out] long *pFailedTasks
);
```



## Property value

The number of tasks that failed.

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

 

 




