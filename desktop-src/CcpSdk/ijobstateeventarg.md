---
Description: 'Provides information related to the state of the job. This interface is passed to your implementation of the ISchedulerJobEvents::OnJobState or IRemoteCommandEvents::OnCommandJobState event handler.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e92b5fe4-48dd-4dc2-8384-f90f06f2c34b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: IJobStateEventArg interface
---

# IJobStateEventArg interface

Provides information related to the state of the job. This interface is passed to your implementation of the [**ISchedulerJobEvents::OnJobState**](ischedulerjobevents-onjobstate.md) or [**IRemoteCommandEvents::OnCommandJobState**](iremotecommandevents-oncommandjobstate.md) event handler.

## Members

The **IJobStateEventArg** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IJobStateEventArg** also has these types of members:

-   [Properties](#properties)

### Properties

The **IJobStateEventArg** interface has these properties.



| Property                                                            | Access type          | Description                                                             |
|:--------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------|
| [**JobId**](ijobstateeventarg-jobid.md)<br/>                 | Read-only<br/> | Retrieves the identifier of the job whose state has changed.<br/> |
| [**NewState**](ijobstateeventarg-newstate.md)<br/>           | Read-only<br/> | Retrieves the state of the job.<br/>                              |
| [**PreviousState**](ijobstateeventarg-previousstate.md)<br/> | Read-only<br/> | Retrieves the previous state of the job.<br/>                     |



 

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

[**IRemoteCommandEvents::OnCommandJobState**](iremotecommandevents-oncommandjobstate.md)
</dt> <dt>

[**ISchedulerJobEvents::OnJobState**](ischedulerjobevents-onjobstate.md)
</dt> </dl>

 

 




