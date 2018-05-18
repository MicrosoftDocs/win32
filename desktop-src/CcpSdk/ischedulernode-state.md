---
Description: 'Retrieves the current state of the node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '50958549-a8aa-49d9-9052-2c60e761cdd0'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerNode::State property'
---

# ISchedulerNode::State property

Retrieves the current state of the node.

This property is read-only.

## Syntax


```C++
HRESULT get_State(
  [out] NodeState *pState
);
```



## Property value

The state of the node. For possible values, see the [**NodeState**](nodestate.md) enumeration.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Examples

For an example, see [Getting a List of Nodes in the Cluster](getting-a-list-of-nodes-in-the-cluster.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerNode**](ischedulernode.md)
</dt> </dl>

 

 




