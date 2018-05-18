---
Description: 'Provides the output from the command as a byte blob. This interface is passed to your implementation of the IRemoteCommandEvents::OnCommandRawOutput event handler.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8ac93535-2a5b-44c0-8d04-39b771dbf9a6'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ICommandRawOutputEventArg interface
---

# ICommandRawOutputEventArg interface

Provides the output from the command as a byte blob. This interface is passed to your implementation of the [**IRemoteCommandEvents::OnCommandRawOutput**](iremotecommandevents-oncommandrawoutput.md) event handler.

## Members

The **ICommandRawOutputEventArg** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ICommandRawOutputEventArg** also has these types of members:

-   [Properties](#properties)

### Properties

The **ICommandRawOutputEventArg** interface has these properties.



| Property                                                          | Access type          | Description                                                            |
|:------------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------|
| [**NodeName**](icommandrawoutputeventarg-nodename.md)<br/> | Read-only<br/> | Retrieves the name of the node that generated the output.<br/>   |
| [**Output**](icommandrawoutputeventarg-output.md)<br/>     | Read-only<br/> | Retrieves the output from the command as a byte blob.<br/>       |
| [**Type**](icommandrawoutputeventarg-type.md)<br/>         | Read-only<br/> | Retrieves a value that determines the source of the output.<br/> |



 

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

[**ICommandOutputEventArg**](icommandoutputeventarg.md)
</dt> <dt>

[**IRemoteCommandEvents**](iremotecommandevents.md)
</dt> </dl>

 

 




