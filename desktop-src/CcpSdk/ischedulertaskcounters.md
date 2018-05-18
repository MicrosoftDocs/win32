---
Description: 'Contains counter data for the tasks that are running in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd4477a5d-9ca6-4f22-8719-5d1637393231'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ISchedulerTaskCounters interface
---

# ISchedulerTaskCounters interface

Contains counter data for the tasks that are running in the cluster.

To get this interface, call the [**ISchedulerTask::GetCounters**](ischedulertask-getcounters.md) method.

## Members

The **ISchedulerTaskCounters** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ISchedulerTaskCounters** also has these types of members:

-   [Properties](#properties)

### Properties

The **ISchedulerTaskCounters** interface has these properties.



| Property                                                                     | Access type          | Description                                                                                                                                                             |
|:-----------------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**TotalCpuTime**](ischedulertaskcounters-totalcputime.md)<br/>       | Read-only<br/> | Retrieves the total CPU time used by all tasks that are running in the cluster.<br/>                                                                              |
| [**TotalKernelTime**](ischedulertaskcounters-totalkerneltime.md)<br/> | Read-only<br/> | Retrieves the elapsed execution time for kernel-mode instructions (the total time that all tasks that are running in the cluster have spent in kernel-mode).<br/> |
| [**TotalMemory**](ischedulertaskcounters-totalmemory.md)<br/>         | Read-only<br/> | Retrieves the total memory used by all tasks that are running in the cluster.<br/>                                                                                |
| [**TotalUserTime**](ischedulertaskcounters-totalusertime.md)<br/>     | Read-only<br/> | Retrieves the elapsed execution time for user-mode instructions (the total time that all tasks that are running in the cluster have spent in user-mode).<br/>     |



 

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**ISchedulerCounters**](ischedulercounters.md)
</dt> <dt>

[**ISchedulerJobCounters**](ischedulerjobcounters.md)
</dt> <dt>

[**ISchedulerNodeCounters**](ischedulernodecounters.md)
</dt> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




