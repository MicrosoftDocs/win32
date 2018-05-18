---
Description: 'Retrieves the time that the task was submitted.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '77d22989-4c95-40c2-b163-47f978b038e0'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::SubmitTime property'
---

# ISchedulerTask::SubmitTime property

Retrieves the time that the task was submitted.

This property is read-only.

## Syntax


```C++
HRESULT get_SubmitTime(
  [out] DATE *pTime
);
```



## Property value

The time the task was submitted. The value is in Coordinated Universal Time.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Remarks

A task is submitted when its parent job is submitted. You could also call the [**ISchedulerJob::SubmitTask**](ischedulerjob-submittask.md) method to submit a task to a running job.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerTask.ChangeTime**](ischedulertask-changetime.md)
</dt> <dt>

[**ISchedulerTask.CreateTime**](ischedulertask-createtime.md)
</dt> <dt>

[**ISchedulerTask.EndTime**](ischedulertask-endtime.md)
</dt> <dt>

[**ISchedulerTask.StartTime**](ischedulertask-starttime.md)
</dt> </dl>

 

 




