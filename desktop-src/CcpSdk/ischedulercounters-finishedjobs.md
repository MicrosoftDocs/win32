---
Description: 'Retrieves the number of jobs that have finished running successfully.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9a253890-13ce-4299-ab8a-17b81dcccd27'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::FinishedJobs property'
---

# ISchedulerCounters::FinishedJobs property

Retrieves the number of jobs that have finished running successfully.

This property is read-only.

## Syntax


```C++
HRESULT get_FinishedJobs(
  [out] long *pFinishedJobs
);
```



## Property value

The number of jobs that have finished running successfully.

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

 

 




