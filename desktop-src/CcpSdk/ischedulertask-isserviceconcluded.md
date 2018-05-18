---
Description: 'Gets whether the HPC Job Scheduler Service has concluded starting subtasks for a service task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8CA99CBB-0F89-431F-9653-7F02A96942D6'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::IsServiceConcluded property'
---

# ISchedulerTask::IsServiceConcluded property

Gets whether the HPC Job Scheduler Service has concluded starting subtasks for a service task.

This property is read-only.

## Syntax


```C++
HRESULT get_IsServiceConcluded(
  [out, retval] VARIANT_BOOL *pRetVal
);
```



## Property value

Pointer to a **VARIANT\_BOOL** that indicates whether the HPC Job Scheduler Service has concluded starting subtasks for a service task.

VARIANT\_TRUE indicates that the HPC Job Scheduler Service has concluded starting subtasks for a service task. VARIANT\_FALSE indicates that the HPC Job Scheduler Service has not concluded starting subtasks for a service task, or that the task is not a service task.

## Error codes

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

[**ISchedulerTask::ServiceConclude**](ischedulertask-serviceconclude.md)
</dt> <dt>

[**ISchedulerTask::Type**](ischedulertask-type.md)
</dt> </dl>

 

 




