---
Description: 'Retrieves the number of tasks that have been submitted to the scheduling queue and are awaiting validation.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'caec2670-0a52-4cd1-b3a3-9ac4b770106a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::SubmittedTasks property'
---

# ISchedulerCounters::SubmittedTasks property

Retrieves the number of tasks that have been submitted to the scheduling queue and are awaiting validation.

This property is read-only.

## Syntax


```C++
HRESULT get_SubmittedTasks(
  [out] long *pSubmittedTasks
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

 

 




