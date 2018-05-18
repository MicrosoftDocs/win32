---
Description: 'Provides information related to the state of a task in the job. This interface is passed to your implementation of the ISchedulerJobEvents::OnTaskState event handler.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '0915e2ba-6371-41e0-a838-7b966e6c51ce'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ITaskStateEventArg interface
---

# ITaskStateEventArg interface

Provides information related to the state of a task in the job. This interface is passed to your implementation of the [**ISchedulerJobEvents::OnTaskState**](ischedulerjobevents-ontaskstate.md) event handler.

## Members

The **ITaskStateEventArg** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ITaskStateEventArg** also has these types of members:

-   [Properties](#properties)

### Properties

The **ITaskStateEventArg** interface has these properties.



| Property                                                             | Access type          | Description                                                                                    |
|:---------------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------|
| [**JobId**](itaskstateeventarg-jobid.md)<br/>                 | Read-only<br/> | Retrieves the identifier of the job that contains the task whose state has changed.<br/> |
| [**NewState**](itaskstateeventarg-newstate.md)<br/>           | Read-only<br/> | Retrieves the state of the task.<br/>                                                    |
| [**PreviousState**](itaskstateeventarg-previousstate.md)<br/> | Read-only<br/> | Retrieves the previous state of the task.<br/>                                           |
| [**TaskId**](itaskstateeventarg-taskid.md)<br/>               | Read-only<br/> | Retrieves the identifier that uniquely identifies the task in a job.<br/>                |



 

## Examples

For an example, see [Implementing the Event Handlers for Job Events in C++](implementing-the-event-handlers-for-job-events-in-c--.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




