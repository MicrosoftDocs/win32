---
Description: 'Defines the counter values related to the status of tasks in the job (for example, the number of tasks that have finished running).'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8ded64be-c1ac-459b-a6df-3e578fbfc449'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ISchedulerJobCounters interface
---

# ISchedulerJobCounters interface

Defines the counter values related to the status of tasks in the job (for example, the number of tasks that have finished running).

To get this interface, call the [**IScheduler::GetCounters**](ischedulerjob-getcounters.md) method.

## Members

The **ISchedulerJobCounters** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ISchedulerJobCounters** also has these types of members:

-   [Properties](#properties)

### Properties

The **ISchedulerJobCounters** interface has these properties.



| Property                                                                              | Access type          | Description                                                                                                                                                                                                       |
|:--------------------------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CanceledTaskCount**](ischedulerjobcounters-canceledtaskcount.md)<br/>       | Read-only<br/> | Retrieves the number of tasks that have been canceled.<br/>                                                                                                                                                 |
| [**CancelingTaskCount**](ischedulerjobcounters-cancelingtaskcount.md)<br/>     | Read-only<br/> | Retrieves the number of tasks being canceled.<br/>                                                                                                                                                          |
| [**ConfiguringTaskCount**](ischedulerjobcounters-configuringtaskcount.md)<br/> | Read-only<br/> | Retrieves the number of tasks being configured.<br/>                                                                                                                                                        |
| [**DispatchingTaskCount**](ischedulerjobcounters-dispatchingtaskcount.md)<br/> | Read-only<br/> | Gets the number of tasks in the job that the scheduler is sending to a node to run.<br/> This property is supported only for Windows HPC Server 2008 R2.<br/>                                         |
| [**FailedTaskCount**](ischedulerjobcounters-failedtaskcount.md)<br/>           | Read-only<br/> | Retrieves the number of tasks that have failed.<br/>                                                                                                                                                        |
| [**FinishedTaskCount**](ischedulerjobcounters-finishedtaskcount.md)<br/>       | Read-only<br/> | Retrieves the number of tasks that have finished.<br/>                                                                                                                                                      |
| [**FinishingTaskCount**](ischedulerjobcounters-finishingtaskcount.md)<br/>     | Read-only<br/> | Gets the number of tasks in the job for which the node is cleaning up the resources that were allocated to the task.<br/> This property is supported only for Windows HPC Server 2008 R2.<br/>        |
| [**QueuedTaskCount**](ischedulerjobcounters-queuedtaskcount.md)<br/>           | Read-only<br/> | Retrieves the number of tasks that are queued and ready to run.<br/>                                                                                                                                        |
| [**RunningTaskCount**](ischedulerjobcounters-runningtaskcount.md)<br/>         | Read-only<br/> | Retrieves the number of tasks that are running.<br/>                                                                                                                                                        |
| [**SubmittedTaskCount**](ischedulerjobcounters-submittedtaskcount.md)<br/>     | Read-only<br/> | Retrieves the number of tasks that have been submitted.<br/>                                                                                                                                                |
| [**TaskCount**](ischedulerjobcounters-taskcount.md)<br/>                       | Read-only<br/> | Retrieves the number of tasks in the job.<br/>                                                                                                                                                              |
| [**TotalCpuTime**](ischedulerjobcounters-totalcputime.md)<br/>                 | Read-only<br/> | Retrieves the total CPU time used by all tasks in the job.<br/>                                                                                                                                             |
| [**TotalKernelTime**](ischedulerjobcounters-totalkerneltime.md)<br/>           | Read-only<br/> | Retrieves the elapsed execution time for kernel-mode instructions (the total time that all tasks in the job spent in kernel-mode).<br/>                                                                     |
| [**TotalMemory**](ischedulerjobcounters-totalmemory.md)<br/>                   | Read-only<br/> | Retrieves the total amount of memory used by the job.<br/>                                                                                                                                                  |
| [**TotalUserTime**](ischedulerjobcounters-totalusertime.md)<br/>               | Read-only<br/> | Retrieves the elapsed execution time for user-mode instructions (the total time that all tasks in the job spent in user-mode).<br/>                                                                         |
| [**ValidatingTaskCount**](ischedulerjobcounters-validatingtaskcount.md)<br/>   | Read-only<br/> | Gets the number of tasks in the job for which the scheduler is determining if the task is correctly configured and can run.<br/> This property is supported only for Windows HPC Server 2008 R2.<br/> |



 

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**ISchedulerCounters**](ischedulercounters.md)
</dt> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerTaskCounters**](ischedulertaskcounters.md)
</dt> </dl>

 

 




