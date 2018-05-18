---
Description: 'Retrieves or sets the run-time limit for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '679b5744-05bb-4a56-9ee3-79ce5cfb074b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::Runtime property'
---

# ISchedulerJob::Runtime property

Retrieves or sets the run-time limit for the job.

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

The run-time limit for the job, in seconds. The default value is 0.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) job property.

## Remarks

The wall clock is used to determine the run time. The time is your best guess of how long the job will take; however, it needs to be fairly accurate because it is used to allocate resources. If the job exceeds this time, the job is terminated and its state becomes Canceled.

The sum of all [**ISchedulerTask::Runtime**](ischedulertask-runtime.md) values for the tasks in the job should be less than the run-time value for the job.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob.HasRuntime**](ischedulerjob-hasruntime.md)
</dt> <dt>

[**ISchedulerJob.RunUntilCanceled**](ischedulerjob-rununtilcanceled.md)
</dt> <dt>

[**ISchedulerTask.Runtime**](ischedulertask-runtime.md)
</dt> </dl>

 

 




