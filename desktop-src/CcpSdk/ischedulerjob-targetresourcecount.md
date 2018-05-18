---
Description: 'Gets or sets the maximum number of resources that a job can use dynamically, so that the HPC Job Scheduler Service does not allocate more resources than the job can use.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '89D5ADE6-0D9A-4E3C-8798-FFBE03ADB4BF'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::TargetResourceCount property'
---

# ISchedulerJob::TargetResourceCount property

Gets or sets the maximum number of resources that a job can use dynamically, so that the HPC Job Scheduler Service does not allocate more resources than the job can use.

This property is read/write.

## Syntax


```C++
HRESULT put_TargetResourceCount(
  [in]          long pRetVal
);

HRESULT get_TargetResourceCount(
  [out, retval] long *pRetVal
);
```



## Property value

Long integer that specifies the maximum number of resources that a job can use.

The possible values are from the minimum number of resources that are requested for the job through the maximum number of resources that are requested for the job, and 0. Specify 0 to indicate that the resource count should not be adjusted dynamically.

If you specify a value that is outside the range of resources that are requested for the job, and it is not 0, the following behaviors result:

-   An exception occurs.

-   The target maximum resource count for the job does not change.

-   The job continues to run.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Remarks

This property is used mostly by jobs that contain service tasks that run service-oriented architecture (SOA) services. For such jobs, the broker node sets and maintains the value of this property based on the number of outstanding messages for the session.

This property is updated periodically based on the RebalancingInterval cluster parameter. During an adjustment, the broker updates job properties and evaluates the value of the **ISchedulerJob::TargetResourceCount** property for a session, based on the load sampling metrics that are gathered within the adjustment interval. The HPC Job Scheduler Service uses the **ISchedulerJob::TargetResourceCount** property to help determine how many service hosts to allocate to the session.

If a SOA client sets the value of the property for a service job, the broker resets it if allocation adjustment is enabled.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




