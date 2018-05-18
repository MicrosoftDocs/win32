---
Description: 'Provides information that is related to changes in the state of a node. This interface is passed to your implementation of the ISchedulerNodeEvents::OnNodeState event handler.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'B031469E-E5B5-41AE-8601-6D41D5D4CB88'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: INodeStateEventArg interface
---

# INodeStateEventArg interface

Provides information that is related to changes in the state of a node. This interface is passed to your implementation of the [**ISchedulerNodeEvents::OnNodeState**](ischedulernodeevents-onnodestate.md) event handler.

## Members

The **INodeStateEventArg** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **INodeStateEventArg** also has these types of members:

-   [Properties](#properties)

### Properties

The **INodeStateEventArg** interface has these properties.



| Property                                                                 | Access type          | Description                                                                       |
|:-------------------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------|
| [**NewState**](inodestateidcollection-newstate.md)<br/>           | Read-only<br/> | Gets the new state of a node when the state of the node changes. <br/>      |
| [**NodeId**](inodestateidcollection-nodeid.md)<br/>               | Read-only<br/> | Gets the numeric identifier of the node for which the state changed.<br/>   |
| [**PreviousState**](inodestateidcollection-previousstate.md)<br/> | Read-only<br/> | Gets the previous state of a node when the state of the node changes. <br/> |



 

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerNodeEvents::OnNodeState**](ischedulernodeevents-onnodestate.md)
</dt> </dl>

 

 




