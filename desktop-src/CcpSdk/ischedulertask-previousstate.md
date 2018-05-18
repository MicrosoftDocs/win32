---
Description: 'Retrieves the previous state of the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a79679b0-8f0e-4469-8ccf-bd91a0891cf0'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::PreviousState property'
---

# ISchedulerTask::PreviousState property

Retrieves the previous state of the task.

This property is read-only.

## Syntax


```C++
HRESULT get_PreviousState(
  [out] TaskState *pState
);
```



## Property value

The previous state of the job. For possible values, see the [**TaskState**](taskstate.md) enumeration.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerTask.State**](ischedulertask-state.md)
</dt> </dl>

 

 




