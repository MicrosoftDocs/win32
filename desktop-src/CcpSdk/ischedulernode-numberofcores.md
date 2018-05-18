---
Description: 'Retrieves the number of cores on the node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '0c4b326c-c25a-4040-a5f1-31239f251112'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerNode::NumberOfCores property'
---

# ISchedulerNode::NumberOfCores property

Retrieves the number of cores on the node.

This property is read-only.

## Syntax


```C++
HRESULT get_NumberOfCores(
  [out] long *pNumCores
);
```



## Property value

The number of cores.

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

[**ISchedulerNode.NumberOfSockets**](ischedulernode-numberofsockets.md)
</dt> </dl>

 

 




