---
Description: 'Determines whether the task is critical for the job. If a task is critical for the job, the job and its tasks stop running and the job is immediately marked as failed if the task fails.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7DDF8089-07AD-4B32-8B26-5582C5724C92'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::FailJobOnFailure property'
---

# ISchedulerTask::FailJobOnFailure property

Determines whether the task is critical for the job. If a task is critical for the job, the job and its tasks stop running and the job is immediately marked as failed if the task fails.

This property is read/write.

## Syntax


```C++
HRESULT put_FailJobOnFailure(
  [in]  VARIANT_BOOL value
);

HRESULT get_FailJobOnFailure(
  [out] VARIANT_BOOL *pValue
);
```



## Property value

Indicates whether the task is critical for the job. **VARIANT\_TRUE** indicates that the task is critical for the job, and that the job and its tasks stop running and the job is marked as failed if the task fails. **VARIANT\_FALSE** indicates that the task is not critical for the job, so that job continues to run the remaining tasks when the task that is not critical fails, and the job is marked as failed only when those remaining tasks finish.

## Error codes

If the method succeeds, the return value is **S\_OK**. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulerjob-errormessage.md) task property.

## Remarks

If you specify a value for the [**FailJobOnFailureCount**](ischedulertask-failjobonfailurecount.md) property, and do not specify a value for the **FailJobOnFailure** property, **FailJobOnFailure** is automatically set to **VARIANT\_TRUE**.

To specify that a job and its tasks should stop running and that job should be marked as failed when any of the tasks in the job fail, use the **FailJobOnFailure** property for the job.

## Requirements



|                         |                                                                                                                                            |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This property was introduced in Windows HPC Server 2008 R2 with Service Pack 1 (SP1) and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>                                     |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**FailJobOnFailureCount**](ischedulertask-failjobonfailurecount.md)
</dt> </dl>

 

 




