---
Description: 'Retrieves the node groups to which this node belongs.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'aec576cb-e4ee-43ad-8d55-035171e708de'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerNode::NodeGroups property'
---

# ISchedulerNode::NodeGroups property

Retrieves the node groups to which this node belongs.

This property is read-only.

## Syntax


```C++
HRESULT get_NodeGroups(
  [out] IStringCollection **pNodeGroups
);
```



## Property value

An [**IStringCollection**](istringcollection.md) interface that contains a collection of node group names.

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

[**IScheduler::GetNodeGroupList**](ischeduler-getnodegrouplist.md)
</dt> <dt>

[**IScheduler::GetNodesInNodeGroup**](ischeduler-getnodesinnodegroup.md)
</dt> </dl>

 

 




