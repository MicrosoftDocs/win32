---
Description: 'Gets or sets the priority of the job by using the expanded range of priority values in Windows&\#160;HPC&\#160;Server&\#160;2008&\#160;R2.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'C547E230-6F8A-49DE-96FB-995CC043E097'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::ExpandedPriority property'
---

# ISchedulerJob::ExpandedPriority property

Gets or sets the priority of the job by using the expanded range of priority values in Windows HPC Server 2008 R2.

This property is read/write.

## Syntax


```C++
HRESULT put_ExpandedPriority(
  [in]          long pRetVal
);

HRESULT get_ExpandedPriority(
  [out, retval] long *pRetVal
);
```



## Property value

A long integer between 0 and 4000 that specifies the priority for the job, where 0 is the lowest priority and 4000 is the highest.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Remarks

If you set the value of the **ISchedulerJob::ExpandedPriority** property to a value less than 0 or a value greater than 4000, an exception occurs.

If you set the values of both the **ISchedulerJob::ExpandedPriority** and [**ISchedulerJob::Priority**](ischedulerjob-priority.md) properties, the property that you set last determines the priority of the job. When you set the value of one of these properties, the value of the other property is automatically updated to the equivalent value.

The Default job template sets the default value to 2000.

The job template for the job determines the values that a user can set for **ISchedulerJob::ExpandedPriority** without administrative privileges. A cluster administrator cannot submit a job with an **ISchedulerJob::ExpandedPriority** that the job template does not allow, but when the job is in the Queued or Running state, the cluster administrator can set **ISchedulerJob::ExpandedPriority** to any value between 0 and 4000, even if the job template does not allow that expanded priority.

Server resources are allocated to jobs based on job priority, except for backfill jobs. Jobs can be preempted if the [**ISchedulerJob::CanPreempt**](ischedulerjob-canpreempt.md) property is VARIANT\_TRUE; otherwise, jobs run until they finish, fail, or are canceled.

Within a job, tasks receive resources based on the order in which they were added to the job. If a resource is available, the task will run.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::Priority**](ischedulerjob-priority.md)
</dt> </dl>

 

 




