---
Description: 'Defines the parameters that are passed to the ISchedulerNodeReachableEvents::OnNodeReachable event handler when the HPC Node Manager Service on a node becomes reachable or unreachable.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4C570334-8737-457A-9BA4-277D8F8F0318'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: INodeReachableEventArg interface
---

# INodeReachableEventArg interface

Defines the parameters that are passed to the [**ISchedulerNodeReachableEvents::OnNodeReachable**](ischedulernodeevents-onnodestate.md) event handler when the HPC Node Manager Service on a node becomes reachable or unreachable.

## Members

The **INodeReachableEventArg** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **INodeReachableEventArg** also has these types of members:

-   [Properties](#properties)

### Properties

The **INodeReachableEventArg** interface has these properties.



| Property                 | Access type          | Description                                                                                                                           |
|:-------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------|
| **NodeId**<br/>    | Read-only<br/> | Gets the numeric identifier of the node for which the HPC Node Manager Service became reachable or unreachable.<br/>            |
| **Reachable**<br/> | Read-only<br/> | Gets whether the HPC Node Manager Service on the node that the NodeId property identifies became reachable or unreachable.<br/> |



 

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities with Service Pack 1 (SP1).<br/>                                |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



 

 




