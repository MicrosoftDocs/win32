---
Description: 'Retrieves the number of jobs that failed.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b5781293-9738-4406-b4da-d95ba2af98ba'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::FailedJobs property'
---

# ISchedulerCounters::FailedJobs property

Retrieves the number of jobs that failed.

This property is read-only.

## Syntax


```C++
HRESULT get_FailedJobs(
  [out] long *pFailedJobs
);
```



## Property value

The number of jobs that failed.

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

 

 




