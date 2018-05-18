---
Description: 'Retrieves the state information for each core on the node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7153a029-2511-4c71-adbe-4530687f2cf0'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerNode::GetCores method'
---

# ISchedulerNode::GetCores method

Retrieves the state information for each core on the node.

## Syntax


```C++
HRESULT GetCores(
  [out] ISchedulerCollection **pCores
);
```



## Parameters

<dl> <dt>

*pCores* \[out\]
</dt> <dd>

An [**ISchedulerCollection**](ischedulercollection.md) interface that contains a collection of core objects. Each item in the collection is a variant of type VT\_DISPATCH. Query the **pdispVal** member of the variant for the [**ISchedulerCore**](ischedulercore.md) interface.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The core information is a snapshot of the core at the time the call was made.

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

 

 




