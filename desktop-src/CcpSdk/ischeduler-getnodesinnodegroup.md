---
Description: 'Retrieves the list of nodes in the specified node group.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c6cd9f79-2ff0-4e27-b714-502ba82b4d05'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::GetNodesInNodeGroup method'
---

# IScheduler::GetNodesInNodeGroup method

Retrieves the list of nodes in the specified node group.

## Syntax


```C++
HRESULT GetNodesInNodeGroup(
  [in]  BSTR              pGroupName,
  [out] IStringCollection **pNodeNames
);
```



## Parameters

<dl> <dt>

*pGroupName* \[in\]
</dt> <dd>

A node group name.

</dd> <dt>

*pNodeNames* \[out\]
</dt> <dd>

An [**IStringCollection**](istringcollection.md) interface that contains the collection of node names in the group.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

To retrieve the available node group names, call the [**IScheduler::GetNodeGroupList**](ischeduler-getnodegrouplist.md) method.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::GetNodeGroupList**](ischeduler-getnodegrouplist.md)
</dt> <dt>

[**ISchedulerJob.NodeGroups**](ischedulerjob-nodegroup.md)
</dt> <dt>

[**ISchedulerNode.NodeGroups**](ischedulernode-nodegroups.md)
</dt> </dl>

 

 




