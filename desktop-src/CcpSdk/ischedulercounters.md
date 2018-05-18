---
Description: 'Contains counter information for the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3c6d6218-6bc5-4372-9817-c94bb1351e6c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ISchedulerCounters interface
---

# ISchedulerCounters interface

Contains counter information for the cluster.

To get this interface, call the [**IScheduler::GetCounters**](ischeduler-getcounters.md) method.

## Members

The **ISchedulerCounters** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ISchedulerCounters** also has these types of members:

-   [Properties](#properties)

### Properties

The **ISchedulerCounters** interface has these properties.



| Property                                                                   | Access type          | Description                                                                                                               |
|:---------------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------|
| [**BusyCores**](ischedulercounters-busycores.md)<br/>               | Read-only<br/> | Retrieves the number of cores that are busy running tasks.<br/>                                                     |
| [**CanceledJobs**](ischedulercounters-canceledjobs.md)<br/>         | Read-only<br/> | Retrieves the number jobs that have been canceled.<br/>                                                             |
| [**CanceledTasks**](ischedulercounters-canceledtasks.md)<br/>       | Read-only<br/> | Retrieves the number of tasks that have been canceled.<br/>                                                         |
| [**CancelingJobs**](ischedulercounters-cancelingjobs.md)<br/>       | Read-only<br/> | Retrieves the number of jobs that are in the process of being canceled.<br/>                                        |
| [**CancelingTasks**](ischedulercounters-cancelingtasks.md)<br/>     | Read-only<br/> | Retrieves the number of tasks that are in the process of being canceled.<br/>                                       |
| [**ConfiguringJobs**](ischedulercounters-configuringjobs.md)<br/>   | Read-only<br/> | Retrieves the number of jobs that are being configured.<br/>                                                        |
| [**ConfiguringTasks**](ischedulercounters-configuringtasks.md)<br/> | Read-only<br/> | Retrieves the number of tasks that are being configured.<br/>                                                       |
| [**DrainingNodes**](ischedulercounters-drainingnodes.md)<br/>       | Read-only<br/> | Retrieves the number of nodes that are in the process of removing jobs from the node.<br/>                          |
| [**FailedJobs**](ischedulercounters-failedjobs.md)<br/>             | Read-only<br/> | Retrieves the number of jobs that failed.<br/>                                                                      |
| [**FailedTasks**](ischedulercounters-failedtasks.md)<br/>           | Read-only<br/> | Retrieves the number of tasks that failed.<br/>                                                                     |
| [**FinishedJobs**](ischedulercounters-finishedjobs.md)<br/>         | Read-only<br/> | Retrieves the number of jobs that have finished running successfully.<br/>                                          |
| [**FinishedTasks**](ischedulercounters-finishedtasks.md)<br/>       | Read-only<br/> | Retrieves the number of tasks that have finished running successfully.<br/>                                         |
| [**FinishingJobs**](ischedulercounters-finishingjobs.md)<br/>       | Read-only<br/> | Retrieves the number of jobs for which the server is cleaning up the resources that were allocated to the job.<br/> |
| [**IdleCores**](ischedulercounters-idlecores.md)<br/>               | Read-only<br/> | Retrieves the number of cores that are not allocated to a job.<br/>                                                 |
| [**OfflineCores**](ischedulercounters-offlinecores.md)<br/>         | Read-only<br/> | Retrieves the number of cores that are offline.<br/>                                                                |
| [**OfflineNodes**](ischedulercounters-offlinenodes.md)<br/>         | Read-only<br/> | Retrieves the number of nodes that are offline.<br/>                                                                |
| [**QueuedJobs**](ischedulercounters-queuedjobs.md)<br/>             | Read-only<br/> | Retrieves the number of jobs that are in the scheduling queue.<br/>                                                 |
| [**QueuedTasks**](ischedulercounters-queuedtasks.md)<br/>           | Read-only<br/> | Retrieves the number of tasks that are in the scheduling queue.<br/>                                                |
| [**ReadyNodes**](ischedulercounters-readynodes.md)<br/>             | Read-only<br/> | Retrieves the number of nodes that are ready to run jobs.<br/>                                                      |
| [**RunningJobs**](ischedulercounters-runningjobs.md)<br/>           | Read-only<br/> | Retrieves the number of jobs that are running.<br/>                                                                 |
| [**RunningTasks**](ischedulercounters-runningtasks.md)<br/>         | Read-only<br/> | Retrieves the number of tasks that are running.<br/>                                                                |
| [**SubmittedJobs**](ischedulercounters-submittedjobs.md)<br/>       | Read-only<br/> | Retrieves the number of jobs that have been submitted to the scheduling queue and are awaiting validation.<br/>     |
| [**SubmittedTasks**](ischedulercounters-submittedtasks.md)<br/>     | Read-only<br/> | Retrieves the number of tasks that have been submitted to the scheduling queue and are awaiting validation.<br/>    |
| [**TotalCores**](ischedulercounters-totalcores.md)<br/>             | Read-only<br/> | Retrieves the total number of cores in the cluster.<br/>                                                            |
| [**TotalJobs**](ischedulercounters-totaljobs.md)<br/>               | Read-only<br/> | Retrieves the total number of jobs in the cluster.<br/>                                                             |
| [**TotalNodes**](ischedulercounters-totalnodes.md)<br/>             | Read-only<br/> | Retrieves the total number of nodes in the cluster.<br/>                                                            |
| [**TotalSockets**](ischedulercounters-totalsockets.md)<br/>         | Read-only<br/> | Retrieves the total number of sockets in the cluster.<br/>                                                          |
| [**TotalTasks**](ischedulercounters-totaltasks.md)<br/>             | Read-only<br/> | Retrieves the total number of tasks in the cluster.<br/>                                                            |
| [**UnreachableNodes**](ischedulercounters-unreachablenodes.md)<br/> | Read-only<br/> | Retrieves the total number of node in the cluster that are not reachable.<br/>                                      |
| [**ValidatingJobs**](ischedulercounters-validatingjobs.md)<br/>     | Read-only<br/> | Retrieves the number of jobs being validated.<br/>                                                                  |



 

## Remarks

The counters are a snapshot of the activity in the cluster at the time you retrieved the data. The counter values in the cluster (not this object) will increase or decrease as activity in the cluster occurs.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**ISchedulerJobCounter**](ischedulerjobcounters.md)
</dt> <dt>

[**ISchedulerNodeCounters**](ischedulernodecounters.md)
</dt> <dt>

[**ISchedulerTaskCounters**](ischedulertaskcounters.md)
</dt> </dl>

 

 




