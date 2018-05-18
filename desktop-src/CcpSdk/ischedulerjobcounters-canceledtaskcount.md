---
Description: 'Retrieves the number of tasks that have been canceled.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c0a039b5-081a-4737-aa9e-2296284e38d6'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJobCounters::CanceledTaskCount property'
---

# ISchedulerJobCounters::CanceledTaskCount property

Retrieves the number of tasks that have been canceled.

This property is read-only.

## Syntax


```C++
HRESULT get_CanceledTaskCount(
  [out] long *pCanceledTaskCount
);
```



## Property value

The number of canceled tasks.

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

 

 




