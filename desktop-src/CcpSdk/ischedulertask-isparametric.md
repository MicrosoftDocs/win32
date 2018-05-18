---
Description: 'Determines whether the task is a parametric task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ba27840a-cd99-4038-ad0a-881d5d99d6d4'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::IsParametric property'
---

# ISchedulerTask::IsParametric property

Determines whether the task is a parametric task.

This property is read/write.

## Syntax


```C++
HRESULT put_IsParametric(
  [in]  VARIANT_BOOL isParametric
);

HRESULT get_IsParametric(
  [out] VARIANT_BOOL *pIsParametric
);
```



## Property value

Set to VARIANT\_TRUE if the task is a parametric task; otherwise, VARIANT\_FALSE. The default is VARIANT\_FALSE.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulerjob-errormessage.md) job property.

## Remarks

For parametric tasks, the Scheduler replaces all occurrences of an asterisk (\*) found in the following task properties, with the instance value:

-   [**CommandLine**](ischedulertask-commandline.md)
-   [**Name**](ischedulertask-name.md)
-   [**StdErrFilePath**](ischedulertask-stderrfilepath.md)
-   [**StdInFilePath**](ischedulertask-stdinfilepath.md)
-   [**StdOutFilePath**](ischedulertask-stdoutfilepath.md)

The total number of instances that a parametric task can generate is 100,000 instances.

When you add or submit the job that contains the parametric task to the Scheduler, the Scheduler adds all the instances of the parametric task to the job. If you change any of the following properties on a parametric task, the Scheduler will rewrite the instances (if you change **IsParametric** to VARIANT\_FALSE, the scheduler will remove the instances):

-   **IsParametric**
-   [**EndValue**](ischedulertask-endvalue.md)
-   [**IncrementValue**](ischedulertask-incrementvalue.md)
-   [**StartValue**](ischedulertask-startvalue.md)

To get the parametric task from the job, call the [**IScheduler::CreateTaskId**](ischeduler-createtaskid.md) method and specify the parametric task identifier. Then call the [**ISchedulerJob::OpenTask**](ischedulerjob-opentask.md) method to get the task. To get an instance of the parametric task, call the [**IScheduler::CreateParametricTaskId**](ischeduler-createparametrictaskid.md) method and specify the instance identifier and parametric task identifier. Then call the **OpenTask** method to get the instance.

## Examples

For an example, see [Creating a Parametric Sweep Task](creating-parametric-sweep-task.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerTask.EndValue**](ischedulertask-endvalue.md)
</dt> <dt>

[**ISchedulerTask.IncrementValue**](ischedulertask-incrementvalue.md)
</dt> <dt>

[**ISchedulerTask.StartValue**](ischedulertask-startvalue.md)
</dt> </dl>

 

 




