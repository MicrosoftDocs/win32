---
Description: 'Provides a line of output from the command. This interface is passed to your implementation of the IRemoteCommandEvents::OnCommandOutput event handler.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'de0a115e-7211-4b40-ade0-cba343bc07c3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ICommandOutputEventArg interface
---

# ICommandOutputEventArg interface

Provides a line of output from the command. This interface is passed to your implementation of the [**IRemoteCommandEvents::OnCommandOutput**](iremotecommandevents-oncommandoutput.md) event handler.

## Members

The **ICommandOutputEventArg** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ICommandOutputEventArg** also has these types of members:

-   [Properties](#properties)

### Properties

The **ICommandOutputEventArg** interface has these properties.



| Property                                                       | Access type          | Description                                                                        |
|:---------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------|
| [**Message**](icommandoutputeventarg-message.md)<br/>   | Read-only<br/> | Retrieves a line of output from the command or an error message string.<br/> |
| [**NodeName**](icommandoutputeventarg-nodename.md)<br/> | Read-only<br/> | Retrieves the name of the node that generated the output.<br/>               |
| [**Type**](icommandoutputeventarg-type.md)<br/>         | Read-only<br/> | Retrieves a value that determines the source of the output.<br/>             |



 

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

[**ICommandRawOutputEventArg**](icommandrawoutputeventarg.md)
</dt> <dt>

[**IRemoteCommandEvents**](iremotecommandevents.md)
</dt> </dl>

 

 




