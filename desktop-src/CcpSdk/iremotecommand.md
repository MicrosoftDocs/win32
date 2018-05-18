---
Description: 'Defines a command to execute on one or more nodes in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '727434fd-5b71-43e5-b30a-17142903a2d6'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: IRemoteCommand interface
---

# IRemoteCommand interface

Defines a command to execute on one or more nodes in the cluster.

To get this interface, call the [**IScheduler::CreateCommand**](ischeduler-createcommand.md) method.

## Members

The **IRemoteCommand** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IRemoteCommand** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IRemoteCommand** interface has these methods.



| Method                                                              | Description                                                      |
|:--------------------------------------------------------------------|:-----------------------------------------------------------------|
| [**Cancel**](iremotecommand-cancel.md)                             | Cancels the command.<br/>                                  |
| [**Start**](iremotecommand-start.md)                               | Executes the command.<br/>                                 |
| [**StartWithCredentials**](iremotecommand-startwithcredentials.md) | Executes the command using the specified credentials.<br/> |



 

### Properties

The **IRemoteCommand** interface has these properties.



| Property                                                     | Access type          | Description                                                                                                                                                                                                             |
|:-------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CommandLine**](iremotecommand-commandline.md)<br/> | Read-only<br/> | Retrieves the command line to execute.<br/>                                                                                                                                                                       |
| [**Id**](iremotecommand-id.md)<br/>                   | Read-only<br/> | Retrieves the identifier that uniquely identifies the command in the cluster.<br/>                                                                                                                                |
| [**NodeNames**](iremotecommand-nodenames.md)<br/>     | Read-only<br/> | Retrieves the collection of node names on which the command will run or has run.<br/>                                                                                                                             |
| [**ProxyTaskId**](iremotecommand-proxytaskid.md)<br/> | Read-only<br/> | Retrieves the unique task identifier for the proxy task in a remote command job. The proxy task is the task that sends the output and error streams from all of the nodes in a remote command to the client.<br/> |



 

## Remarks

Only cluster administrators can run commands.

Commands are special jobs that run immediately on the specified nodes. You cannot rerun a command.

If you want to receive event notification when the state of the command changes, implement the [**IRemoteCommandEvents**](iremotecommandevents.md) interface. For details, see [Implementing the Event Handlers for Command Events in C++](implementing-the-event-handlers-for-command-events-in-c--.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**IRemoteCommandEvents**](iremotecommandevents.md)
</dt> </dl>

 

 




