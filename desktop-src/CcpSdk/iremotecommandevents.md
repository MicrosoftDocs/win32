---
Description: 'Implement this interface if you want to receive event notification when the state of the command changes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2fe1f6d3-5c8d-41bb-925b-2e29b2aae65a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: IRemoteCommandEvents interface
---

# IRemoteCommandEvents interface

Implement this interface if you want to receive event notification when the state of the command changes.

## Members

The **IRemoteCommandEvents** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IRemoteCommandEvents** also has these types of members:

-   [Methods](#methods)

### Methods

The **IRemoteCommandEvents** interface has these methods.



| Method                                                                | Description                                                                                                            |
|:----------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------|
| [**OnCommandJobState**](iremotecommandevents-oncommandjobstate.md)   | Is called when the job that contains the command changes.<br/>                                                   |
| [**OnCommandOutput**](iremotecommandevents-oncommandoutput.md)       | Is called each time the command generates a line of output or an error occurs.<br/>                              |
| [**OnCommandRawOutput**](iremotecommandevents-oncommandrawoutput.md) | Is called each time the command generates output or an error occurs. The output is returned as a byte blob.<br/> |
| [**OnCommandTaskState**](iremotecommandevents-oncommandtaskstate.md) | Is called when the state of the command changes.<br/>                                                            |



 

## Remarks

You must implement all methods in this interface. You will receive notification for each event—you cannot specify the types of events you want to receive. You cannot rely on the order in which you receive the events. The order of events is indeterminate. For details on implementing this interface, see [Implementing the Event Handlers for Command Events in C++](implementing-the-event-handlers-for-command-events-in-c--.md).

## Examples

For an example, see [Executing Commands](executing-commands.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**IRemoteCommand**](iremotecommand.md)
</dt> </dl>

 

 




