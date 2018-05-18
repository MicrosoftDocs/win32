---
Description: 'Gets the previous state of a node when the state of the node changes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'E028BF09-2EE7-45FA-8FBA-478AFA8003A4'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INodeStateEventArg::PreviousState property'
---

# INodeStateEventArg::PreviousState property

Gets the previous state of a node when the state of the node changes.

This property is read-only.

## Syntax


```C++
HRESULT get_PreviousState(
  [out, retval] NodeState *pRetVal
);
```



## Property value

The previous state of a node when the state of the node changes. For possible values, see [**NodeState**](nodestate.md).

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

[**INodeStateEventArg::NewState**](inodestateidcollection-newstate.md)
</dt> <dt>

[**ISchedulerNodeEvents::OnNodeState**](ischedulernodeevents-onnodestate.md)
</dt> </dl>

 

 




