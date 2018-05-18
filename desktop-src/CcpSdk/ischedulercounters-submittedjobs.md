---
Description: 'Retrieves the number of jobs that have been submitted to the scheduling queue and are awaiting validation.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '397f0a13-a180-492d-b8c9-bbaf82037f44'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::SubmittedJobs property'
---

# ISchedulerCounters::SubmittedJobs property

Retrieves the number of jobs that have been submitted to the scheduling queue and are awaiting validation.

This property is read-only.

## Syntax


```C++
HRESULT get_SubmittedJobs(
  [out] long *pSubmittedJobs
);
```



## Property value

The number of jobs that have been submitted to the scheduling queue and are awaiting validation.

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

 

 




