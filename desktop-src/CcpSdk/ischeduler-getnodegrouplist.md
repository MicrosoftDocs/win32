---
Description: 'Retrieves a list of node group names defined in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3b52912f-6bdc-4128-a556-45a736513285'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::GetNodeGroupList method'
---

# IScheduler::GetNodeGroupList method

Retrieves a list of node group names defined in the cluster.

## Syntax


```C++
HRESULT GetNodeGroupList(
  [out] IStringCollection **pGroupNames
);
```



## Parameters

<dl> <dt>

*pGroupNames* \[out\]
</dt> <dd>

An [**IStringCollection**](istringcollection.md) interface that contains a collection of node group names.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

If you use the enumerator to enumerate each item in the collection, the item is a VARIANT of type VT\_BSTR. Access the **bstrVal** member for the group name.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::GetNodesInNodeGroup**](ischeduler-getnodesinnodegroup.md)
</dt> <dt>

[**ISchedulerJob.NodeGroups**](ischedulerjob-nodegroup.md)
</dt> <dt>

[**ISchedulerNode.NodeGroups**](ischedulernode-nodegroups.md)
</dt> </dl>

 

 




