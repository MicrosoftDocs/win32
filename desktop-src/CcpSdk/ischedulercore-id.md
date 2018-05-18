---
Description: 'Retrieves the identifier that uniquely identifies the core.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ee45b7c6-26f7-4c5f-a5cd-f82d2a6f6c4c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCore::Id property'
---

# ISchedulerCore::Id property

Retrieves the identifier that uniquely identifies the core.

This property is read-only.

## Syntax


```C++
HRESULT get_Id(
  [out] long *pId
);
```



## Property value

The identifier that uniquely identifies the core.

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

[**ISchedulerCore**](ischedulercore.md)
</dt> </dl>

 

 




