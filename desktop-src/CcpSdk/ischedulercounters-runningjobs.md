---
Description: 'Retrieves the number of jobs that are running.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8c83ead9-fdc9-4698-a8ee-14f6e87e82fa'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::RunningJobs property'
---

# ISchedulerCounters::RunningJobs property

Retrieves the number of jobs that are running.

This property is read-only.

## Syntax


```C++
HRESULT get_RunningJobs(
  [out] long *pRunningJobs
);
```



## Property value

The number of jobs that are running.

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

 

 




