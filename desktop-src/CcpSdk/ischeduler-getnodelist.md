---
Description: 'Retrieves a list of nodes in the cluster based on the specified filters.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '6cb0464f-db42-475a-9157-1e713c0db1a1'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::GetNodeList method'
---

# IScheduler::GetNodeList method

Retrieves a list of nodes in the cluster based on the specified filters.

## Syntax


```C++
HRESULT GetNodeList(
  [in]  IFilterCollection    *filterProperties,
  [in]  ISortCollection      *sortProperties,
  [out] ISchedulerCollection **pNodes
);
```



## Parameters

<dl> <dt>

*filterProperties* \[in\]
</dt> <dd>

An [**IFilterCollection**](ifiltercollection.md) interface that contains one or more filter properties used to filter the list of nodes. If **NULL**, the method returns all nodes.

</dd> <dt>

*sortProperties* \[in\]
</dt> <dd>

An [**ISortCollection**](isortcollection.md) interface that contains one or more sort properties used to sort the list of nodes. If **NULL**, the list is not sorted.

</dd> <dt>

*pNodes* \[out\]
</dt> <dd>

An [**ISchedulerCollection**](ischedulercollection.md) interface that contains one or more node objects that match the specified filter criteria. Each item in the collection is a variant of type VT\_DISPATCH. Query the **pdispVal** member for the [**ISchedulerNode**](ischedulernode.md) interface.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

If you specify more than one filter, a logical **AND** is applied to the filters (for example, return nodes that are reachable and have four sockets).

## Examples

For an example, see [Getting a List of Nodes in the Cluster](getting-a-list-of-nodes-in-the-cluster.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::GetNodeIdList**](ischeduler-getnodeidlist.md)
</dt> </dl>

 

 




