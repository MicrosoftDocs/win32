---
Description: 'Gets the numeric identifier of the node for which the state changed.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '068709DE-D3CC-4864-AA6C-A7C004011E7A'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INodeStateEventArg::NodeId property'
---

# INodeStateEventArg::NodeId property

Gets the numeric identifier of the node for which the state changed.

> [!Note]  
> The name of this parameter has changed, for Service Pack 1, from "nodeId" to "NodeId."

 

This property is read-only.

## Syntax


```C++
HRESULT get_NodeId(
  [out, retval] long *pRetVal
);
```



## Property value

Pointer to a long integer that indicates the numeric identifier of the node for which the state changed.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Remarks

To get information about the node for which the state changed, use the [**IScheduler::OpenNode**](ischeduler-opennode.md) method and set the *id* parameter set to a value that this property returns to get an [**ISchedulerNode**](ischedulernode.md) interface for the node.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**INodeStateEventArg**](inodestateeventarg.md)
</dt> <dt>

[**INodeStateEventArg::NewState**](inodestateidcollection-newstate.md)
</dt> <dt>

[**INodeStateEventArg::PreviousState**](inodestateidcollection-previousstate.md)
</dt> <dt>

[**ISchedulerNodeEvents::OnNodeState**](ischedulernodeevents-onnodestate.md)
</dt> <dt>

[**IScheduler::OpenNode**](ischeduler-opennode.md)
</dt> </dl>

 

 




