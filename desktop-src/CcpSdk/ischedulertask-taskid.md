---
Description: 'Retrieves the identifiers that uniquely identify the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '23f98790-4b8f-46e8-b6d8-6e02617ccf25'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::TaskId property'
---

# ISchedulerTask::TaskId property

Retrieves the identifiers that uniquely identify the task.

This property is read-only.

## Syntax


```C++
HRESULT get_TaskId(
  [out] ITaskId **pId
);
```



## Property value

An [**ITaskId**](itaskid.md) interface that uniquely identifies the task.

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
</dt> </dl>

 

 




