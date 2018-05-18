---
Description: 'Determines whether the server thinks the node is reachable.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1d312ce8-826f-4ab6-8083-dd2f0497bcb7'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerNode::Reachable property'
---

# ISchedulerNode::Reachable property

Determines whether the server thinks the node is reachable.

This property is read-only.

## Syntax


```C++
HRESULT get_Reachable(
  [out] VARIANT_BOOL *pIsReachable
);
```



## Property value

Is VARIANT\_TRUE if the node is reachable; otherwise, VARIANT\_FALSE.

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
</dt> <dt>

[**ISchedulerNode.MoveToOffline**](ischedulernode-movetooffline.md)
</dt> </dl>

 

 




