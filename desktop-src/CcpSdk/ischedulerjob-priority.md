---
Description: 'Retrieves or sets the job priority.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e76b06f0-5aae-4441-bb68-fcd443b4368c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::Priority property'
---

# ISchedulerJob::Priority property

Retrieves or sets the job priority.

This property is read/write.

## Syntax


```C++
HRESULT put_Priority(
  [in]  JobPriority priority
);

HRESULT get_Priority(
  [out] JobPriority *pPriority
);
```



## Property value

The job priority. For possible values, see the [**JobPriority**](jobpriority-hpc.md) enumeration.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

The Default job template sets the default value to JobPriority\_Normal.

Server resources are allocated to jobs based on job priority, except for backfill jobs. Jobs can be preempted if the [**ISchedulerJob::CanPreempt**](ischedulerjob-canpreempt.md) property is VARIANT\_TRUE; otherwise, jobs run until they finish, fail, or are canceled.

Within a job, tasks receive resources based on the order in which they were added to the job. If a resource is available, the task will run.

In Windows HPC Server 2008 R2, you can use the [**ISchedulerJob::ExpandedPriority**](ischedulerjob-expandedpriority.md) property to set priority values over a scale of 4000 values instead of 5 values. If you set the values of both the **ISchedulerJob::Priority** and **ISchedulerJob::ExpandedPriority** properties, the property that you set last determines the priority of the job. When you set the value of one of these properties, the value of the other property is automatically updated to the equivalent value.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::ExpandedPriority**](ischedulerjob-expandedpriority.md)
</dt> </dl>

 

 




