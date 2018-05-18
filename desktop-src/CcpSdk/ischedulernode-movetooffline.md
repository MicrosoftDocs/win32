---
Description: 'Determines whether a user requested that the node go offline.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '319da4f5-3d3f-4298-9778-43d4ecb53255'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerNode::MoveToOffline property'
---

# ISchedulerNode::MoveToOffline property

Determines whether a user requested that the node go offline.

This property is read-only.

## Syntax


```C++
HRESULT get_MoveToOffline(
  [out] VARIANT_BOOL *pMoveOffline
);
```



## Property value

Is VARIANT\_TRUE if the user has requested that the node go offline; otherwise VARIANT\_FALSE.

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

[**ISchedulerNode.OfflineTime**](ischedulernode-offlinetime.md)
</dt> <dt>

[**ISchedulerNode.OnlineTime**](ischedulernode-onlinetime.md)
</dt> </dl>

 

 




