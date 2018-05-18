---
Description: 'Retrieves a list of identifiers for the nodes in the cluster based on the specified filters.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3acb1c09-58a3-4591-b8e4-ad4d76051946'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::GetNodeIdList method'
---

# IScheduler::GetNodeIdList method

Retrieves a list of identifiers for the nodes in the cluster based on the specified filters.

## Syntax


```C++
HRESULT GetNodeIdList(
  [in]  IFilterCollection *filterProperties,
  [in]  ISortCollection   *sortProperties,
  [out] IIntCollection    **pNodeIds
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

*pNodeIds* \[out\]
</dt> <dd>

An [**IIntCollection**](iintcollection.md) interface that contains one or more node identifiers that match the specified filter criteria.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

If you specify more than one filter, a logical **AND** is applied to the filters (for example, return nodes that are reachable and have four sockets).

If you use the enumerator to enumerate each item in the collection, the item is a VARIANT of type VT\_I4. Query the **lVal** member for the job identifier.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::GetNodeList**](ischeduler-getnodelist.md)
</dt> <dt>

[**IScheduler::OpenNode**](ischeduler-opennode.md)
</dt> </dl>

 

 




