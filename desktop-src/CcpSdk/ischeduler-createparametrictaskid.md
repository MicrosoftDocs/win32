---
Description: 'Creates a task identifier that identifies an instance of a parametric task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b5c4dc1a-7d73-46d4-8962-06310fd0e4f9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::CreateParametricTaskId method'
---

# IScheduler::CreateParametricTaskId method

Creates a task identifier that identifies an instance of a parametric task.

## Syntax


```C++
HRESULT CreateParametricTaskId(
  [in]  long    jobTaskId,
  [in]  long    instanceId,
  [out] ITaskId **pTaskId
);
```



## Parameters

<dl> <dt>

*jobTaskId* \[in\]
</dt> <dd>

A sequential, numeric identifier that uniquely identifies the parametric task within the job. Task identifiers begin with "1".

</dd> <dt>

*instanceId* \[in\]
</dt> <dd>

A sequential, numeric identifier that uniquely identifies the instance of a parametric task.

</dd> <dt>

*pTaskId* \[out\]
</dt> <dd>

An [**ITaskId**](itaskid.md) interface that identifies the instance of a parametric task.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

To create a task identifier object that identifies a task or parametric task, call the [**IScheduler::CreateTaskId**](ischeduler-createtaskid.md) method.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::CreateTaskId**](ischeduler-createtaskid.md)
</dt> </dl>

 

 




