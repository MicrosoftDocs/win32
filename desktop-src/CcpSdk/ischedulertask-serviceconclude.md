---
Description: 'Directs the HPC Job Scheduler Service to stop starting subtasks for a service task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '0250D3FF-E5F2-43E9-9E3E-2E6C5469DA79'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::ServiceConclude method'
---

# ISchedulerTask::ServiceConclude method

Directs the HPC Job Scheduler Service to stop starting subtasks for a service task.

## Syntax


```C++
HRESULT ServiceConclude(
  [in] VARIANT_BOOL cancelSubTasks
);
```



## Parameters

<dl> <dt>

*cancelSubTasks* \[in\]
</dt> <dd>

**VARIANT\_BOOL** that specifies whether the HPC Job Scheduler Service should cancel subtasks of the service task that are already running.

VARIANT\_TRUE specifies that the HPC Job Scheduler Service should cancel subtasks of the service task that are already running. VARIANT\_FALSE specifies that the HPC Job Scheduler Service should not cancel subtasks of the service task that are already running.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerTask::IsServiceConcluded**](ischedulertask-isserviceconcluded.md)
</dt> <dt>

[**ISchedulerTask::Type**](ischedulertask-type.md)
</dt> </dl>

 

 




