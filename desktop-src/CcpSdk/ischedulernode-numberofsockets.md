---
Description: 'Retrieves the number of sockets on the node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '51cfdd73-128c-4034-8181-1b914e285e10'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerNode::NumberOfSockets property'
---

# ISchedulerNode::NumberOfSockets property

Retrieves the number of sockets on the node.

This property is read-only.

## Syntax


```C++
HRESULT get_NumberOfSockets(
  [out] long *pNumSockets
);
```



## Property value

The number of sockets.

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

[**ISchedulerNode.NumberOfCores**](ischedulernode-numberofcores.md)
</dt> </dl>

 

 




