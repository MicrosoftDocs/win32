---
Description: 'Identifies the node that is reporting the state change. This interface is passed to your implementation of the IRemoteCommandEvents::OnCommandTaskState event handler.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3c19bd6b-a747-4b35-9a93-4290a90b0a72'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ICommandTaskStateEventArg interface
---

# ICommandTaskStateEventArg interface

Identifies the node that is reporting the state change. This interface is passed to your implementation of the [**IRemoteCommandEvents::OnCommandTaskState**](iremotecommandevents-oncommandtaskstate.md) event handler.

## Members

The **ICommandTaskStateEventArg** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ICommandTaskStateEventArg** also has these types of members:

-   [Properties](#properties)

### Properties

The **ICommandTaskStateEventArg** interface has these properties.



| Property                                                                  | Access type          | Description                                                                                   |
|:--------------------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------------|
| [**ErrorMessage**](icommandtaskstateeventarg-errormessage.md)<br/> | Read-only<br/> | Retrieves the error message for the error that occurred while running the command.<br/> |
| [**ExitCode**](icommandtaskstateeventarg-exitcode.md)<br/>         | Read-only<br/> | Retrieves the exit code that the command set.<br/>                                      |
| [**IsProxy**](icommandtaskstateeventarg-isproxy.md)<br/>           | Read-only<br/> | Determines if the output is coming from a proxy task.<br/>                              |
| [**NodeName**](icommandtaskstateeventarg-nodename.md)<br/>         | Read-only<br/> | Retrieves the name of the node that is running the command.<br/>                        |



 

## Remarks

To get the state change information, query this interface for the [**ITaskStateEventArg**](itaskstateeventarg.md) interface.

## Examples

For an example, see Implementing the [Event Handlers for Command Events in C++](implementing-the-event-handlers-for-command-events-in-c--.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**IJobStateEventArg**](ijobstateeventarg.md)
</dt> <dt>

[**IRemoteCommandEvents**](iremotecommandevents.md)
</dt> </dl>

 

 




