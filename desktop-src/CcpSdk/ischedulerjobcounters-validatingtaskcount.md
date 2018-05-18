---
Description: 'Gets the number of tasks in the job for which the scheduler is determining if the task is correctly configured and can run.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '21D1E4B5-A01C-4B68-AF29-EDAED9929FC0'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJobCounters::ValidatingTaskCount property'
---

# ISchedulerJobCounters::ValidatingTaskCount property

Gets the number of tasks in the job for which the scheduler is determining if the task is correctly configured and can run.

This property is read-only.

## Syntax


```C++
HRESULT get_ValidatingTaskCount(
  [out, retval] long *pRetVal
);
```



## Property value

The number of tasks in the job for which the scheduler is determining if the task is correctly configured and can run.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJobCounters**](ischedulerjobcounters.md)
</dt> </dl>

 

 




