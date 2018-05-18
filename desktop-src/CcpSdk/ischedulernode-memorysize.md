---
Description: 'Retrieves the size of memory.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'fc8c517f-6b00-4478-a73e-bbbebf9c9c6c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerNode::MemorySize property'
---

# ISchedulerNode::MemorySize property

Retrieves the size of memory.

This property is read-only.

## Syntax


```C++
HRESULT get_MemorySize(
  [out] __int64 *pSize
);
```



## Property value

The size of memory, in megabytes.

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

[**ISchedulerNode.CpuSpeed**](ischedulernode-cpuspeed.md)
</dt> </dl>

 

 




