---
Description: 'Retrieves the number of jobs for which the server is cleaning up the resources that were allocated to the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b8831690-8ece-4126-a8e4-23caf718974d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::FinishingJobs property'
---

# ISchedulerCounters::FinishingJobs property

Retrieves the number of jobs for which the server is cleaning up the resources that were allocated to the job.

This property is read-only.

## Syntax


```C++
HRESULT get_FinishingJobs(
  [out] long *pFinishingJobs
);
```



## Property value

The number of jobs for which the server is cleaning up the resources that were allocated to the job.

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

 

 




