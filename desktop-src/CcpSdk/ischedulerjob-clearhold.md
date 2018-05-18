---
Description: 'Removes the hold on the job by clearing the date and time that the HPC Job Scheduler Service should wait until before running the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'F42775B4-2AD3-444F-8D0C-24DD3DBD280E'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::ClearHold property'
---

# ISchedulerJob::ClearHold property

Removes the hold on the job by clearing the date and time that the HPC Job Scheduler Service should wait until before running the job.

## Syntax

## Property value

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Remarks

If you call this method for a job that is not currently on hold, the method has no effect.

To confirm that the **ISchedulerJob::ClearHold** method succeeded, check the value of the [**ISchedulerJob::HoldUntil**](ischedulerjob-holduntil.md) property.

## Requirements



|                         |                                                                                                                |
|-------------------------|----------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This method was introduced in Windows HPC Server 2008 R2 and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>         |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::HoldUntil**](ischedulerjob-holduntil.md)
</dt> </dl>

 

 




