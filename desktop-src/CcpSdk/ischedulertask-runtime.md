---
Description: 'Retrieves or sets the run-time limit for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'aad95723-02b2-4c62-8064-d7f8b5dbb628'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::Runtime property'
---

# ISchedulerTask::Runtime property

Retrieves or sets the run-time limit for the task.

This property is read/write.

## Syntax


```C++
HRESULT put_Runtime(
  [in]  long limit
);

HRESULT get_Runtime(
  [out] long *pLimit
);
```



## Property value

The run-time limit for the task, in seconds. The default is 0.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Remarks

The wall clock is used to determine the run time. The time is your best guess of how long the task will take; however, it needs to be fairly accurate because it is used to allocate resources. If the task exceeds this time, the task is terminated and its state becomes Failed.

The sum of all **Runtime** values for the tasks in the job should be less than the run-time value for the job (see [**ISchedulerJob.Runtime**](ischedulerjob-runtime.md)). If the task's run-time value is greater than the job's run-time value, then the task will run until it exceeds the job's run-time value. If this occurs, the task is terminated and its state becomes Failed.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerTask.HasRuntime**](ischedulerjob-hasruntime.md)
</dt> <dt>

[**ISchedulerJob.Runtime**](ischedulerjob-runtime.md)
</dt> <dt>

[**ISchedulerJob.RunUntilCanceled**](ischedulerjob-rununtilcanceled.md)
</dt> </dl>

 

 




