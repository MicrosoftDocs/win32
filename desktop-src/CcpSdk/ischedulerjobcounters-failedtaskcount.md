---
Description: 'Retrieves the number of tasks that have failed.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c72615ac-8e1c-4d4c-b0f7-34e01a9f85d8'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJobCounters::FailedTaskCount property'
---

# ISchedulerJobCounters::FailedTaskCount property

Retrieves the number of tasks that have failed.

This property is read-only.

## Syntax


```C++
HRESULT get_FailedTaskCount(
  [out] long *pFailedTaskCount
);
```



## Property value

The number of tasks that have failed.

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

 

 




