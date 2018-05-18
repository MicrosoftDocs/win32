---
Description: 'Retrieves the number of tasks in the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7abe9883-9711-42d8-9423-48c7389b4b60'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJobCounters::TaskCount property'
---

# ISchedulerJobCounters::TaskCount property

Retrieves the number of tasks in the job.

This property is read-only.

## Syntax


```C++
HRESULT get_TaskCount(
  [out] long *pTaskCount
);
```



## Property value

The number of tasks in the job.

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

 

 




