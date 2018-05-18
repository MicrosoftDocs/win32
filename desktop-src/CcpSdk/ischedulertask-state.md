---
Description: 'Retrieves the state of the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '79060f64-949a-446a-867f-aa7ae7be4b2d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::State property'
---

# ISchedulerTask::State property

Retrieves the state of the task.

This property is read-only.

## Syntax


```C++
HRESULT get_State(
  [out] TaskState *pState
);
```



## Property value

The state of the task. For possible values, see the [**TaskState**](taskstate.md) enumeration.

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

[**ISchedulerTask.PreviousState**](ischedulertask-previousstate.md)
</dt> <dt>

[**ISchedulerJob.State**](ischedulerjob-state.md)
</dt> </dl>

 

 




