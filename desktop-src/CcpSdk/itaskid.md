---
Description: 'Contains the identifiers that uniquely identify the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd4fbac08-31cc-46d7-aa6c-f6910739d340'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ITaskId interface
---

# ITaskId interface

Contains the identifiers that uniquely identify the task.

To create this interface, call the [**IScheduler::CreateTaskId**](ischeduler-createtaskid.md) or [**IScheduler::CreateParametricTaskId**](ischeduler-createparametrictaskid.md) method.

## Members

The **ITaskId** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ITaskId** also has these types of members:

-   [Properties](#properties)

### Properties

The **ITaskId** interface has these properties.



| Property                                              | Access type          | Description                                                                         |
|:------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------|
| [**InstanceId**](itaskid-instanceid.md)<br/>   | Read-only<br/> | Retrieves the instance identifier of a parametric task.<br/>                  |
| [**JobTaskId**](itaskid-jobtaskid.md)<br/>     | Read-only<br/> | Retrieves the sequential identifier that identifies the task in the job.<br/> |
| [**ParentJobId**](itaskid-parentjobid.md)<br/> | Read-only<br/> | Retrieves the identifier that identifies the parent job.<br/>                 |



 

## Remarks

If the job has been added to the scheduler, the task identifier is assigned to the task when you call the [**ISchedulerJob::AddTask**](ischedulerjob-addtask.md) method. Otherwise, the identifier is assigned when you add the job to the scheduler.

## Requirements



|                         |                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.Properties.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**ISchedulerTask.TaskId**](ischedulertask-taskid.md)
</dt> </dl>

 

 




