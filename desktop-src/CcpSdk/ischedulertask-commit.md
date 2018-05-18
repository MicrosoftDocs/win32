---
Description: 'Commits the local task changes to the server.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b8a08d30-fb64-4dbe-a9ed-e2b99413a4c7'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::Commit method'
---

# ISchedulerTask::Commit method

Commits the local task changes to the server.

## Syntax


```C++
HRESULT Commit();
```



## Parameters

This method has no parameters.

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Remarks

All changes made to the task are made locally. Call this method to apply your changes to the server.

To make changes to a task, the task and job must be in the Configuring state; you cannot make changes to the task after the job has been submitted.

## Examples

For an example, see [Cloning a Job](cloning-a-job.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerTask::Refresh**](ischedulertask-refresh.md)
</dt> <dt>

[**ISchedulerJob::Commit**](ischedulerjob-commit.md)
</dt> </dl>

 

 




