---
Description: 'Sets the earliest date and time until which the HPC Job Scheduler Service should wait until before starting the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'C4AA07FE-9F69-41B1-B1B2-9F87EEF93BC6'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::SetHoldUntil method'
---

# ISchedulerJob::SetHoldUntil method

Sets the earliest date and time until which the HPC Job Scheduler Service should wait until before starting the job.

## Syntax


```C++
HRESULT SetHoldUntil(
  [in] DATE *holdUntil
);
```



## Parameters

<dl> <dt>

*holdUntil* \[in\]
</dt> <dd>

Specifies the earlier date and time in the local time zone until which the HPC Job Scheduler Service should wait before running the job. The date and time must be in the future.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

The HPC Job Scheduler Service only runs the job at the date and time that you specify in the holdUntil parameter if the resources needed for the job are available. If the resources needed for the job are not available at that date and time, the job remains queued until the necessary resources become available.

You can only call this method once you submit the job and it is waiting in the queue. While the job is on hold, HPC Cluster Manager displays the following message for the job:

**The job is pending: This job is being held by the administrator.**

To unset the date and time that the HPC Job Scheduler Service should wait until before running the job, which removes the hold on the job and allows it to run, call the [**ISchedulerJob::ClearHold**](ischedulerjob-clearhold.md) method.

## Requirements



|                         |                                                                                                                |
|-------------------------|----------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This method was introduced in Windows HPC Server 2008 R2 and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>         |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::ClearHold**](ischedulerjob-clearhold.md)
</dt> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




