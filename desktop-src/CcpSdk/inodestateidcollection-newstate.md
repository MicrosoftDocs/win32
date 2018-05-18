---
Description: 'Gets the new state of a node when the state of the node changes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '37BD212F-2E61-4B38-9B8E-00B6F36D0435'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INodeStateEventArg::NewState property'
---

# INodeStateEventArg::NewState property

Gets the new state of a node when the state of the node changes.

This property is read-only.

## Syntax


```C++
HRESULT get_NewState(
  [out, retval] NodeState *pRetVal
);
```



## Property value

The new state of a node when the state of the node changes. For possible values, see [**NodeState**](nodestate.md).

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**INodeStateEventArg**](inodestateeventarg.md)
</dt> <dt>

[**NodeState**](nodestate.md)
</dt> <dt>

[**INodeStateEventArg::nodeId**](inodestateidcollection-nodeid.md)
</dt> <dt>

[**INodeStateEventArg::PreviousState**](inodestateidcollection-previousstate.md)
</dt> <dt>

[**ISchedulerNodeEvents::OnNodeState**](ischedulernodeevents-onnodestate.md)
</dt> </dl>

 

 




