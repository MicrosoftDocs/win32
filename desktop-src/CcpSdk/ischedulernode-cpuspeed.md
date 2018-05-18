---
Description: 'Retrieves the processor speed of the node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3c32b891-87c3-4c12-a3d9-4ce65b73c7ce'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerNode::CpuSpeed property'
---

# ISchedulerNode::CpuSpeed property

Retrieves the processor speed of the node.

This property is read-only.

## Syntax


```C++
HRESULT get_CpuSpeed(
  [out] long *pCpuSpeed
);
```



## Property value

The processor speed, in megahertz (MHz).

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

[**ISchedulerNode.MemorySize**](ischedulernode-memorysize.md)
</dt> </dl>

 

 




