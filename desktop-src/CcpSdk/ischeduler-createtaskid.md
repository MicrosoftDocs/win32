---
Description: 'Creates a task identifier that identifies a task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '93b37340-95a4-4556-8070-65ed6626d65a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::CreateTaskId method'
---

# IScheduler::CreateTaskId method

Creates a task identifier that identifies a task.

## Syntax


```C++
HRESULT CreateTaskId(
  [in]  long    jobTaskId,
  [out] ITaskId **pId
);
```



## Parameters

<dl> <dt>

*jobTaskId* \[in\]
</dt> <dd>

A sequential, numeric identifier that uniquely identifies the task within the job. Task identifiers begin with "1".

</dd> <dt>

*pId* \[out\]
</dt> <dd>

An [**ITaskId**](itaskid.md) interface identifies a task in a job.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

Use this method to create an identifier that identifies a task or parametric task. To create a task identifier that identifies an instance of a parametric task, call the [**IScheduler::CreateParametricTaskId**](ischeduler-createparametrictaskid.md) method.

## Examples

For an example, see [Cloning a Job](cloning-a-job.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::CreateParametricTaskId**](ischeduler-createparametrictaskid.md)
</dt> </dl>

 

 




