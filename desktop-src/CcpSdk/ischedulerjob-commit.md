---
Description: 'Commits to the server any local changes to the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'aa71f614-aa4c-45a5-9d64-21da07a747ff'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::Commit method'
---

# ISchedulerJob::Commit method

Commits to the server any local changes to the job.

## Syntax


```C++
HRESULT Commit();
```



## Parameters

This method has no parameters.

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

All changes made to the job are made locally. Call this method to apply your changes (to the job's properties) to the server. To commit updates, the job must have been previously added to the scheduler.

If the user changed a property value that the template marks as read-only, the property value is silently set to the template's default value. If the user set a property value that is outside the range of the template's constraint on that property, the method fails.

For details on the properties that you can update in the different states, see [Updating a Job](updating-a-job.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::Refresh**](ischedulerjob-refresh.md)
</dt> <dt>

[**ISchedulerTask::Commit**](ischedulertask-commit.md)
</dt> </dl>

 

 




