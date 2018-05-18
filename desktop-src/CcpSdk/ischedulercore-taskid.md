---
Description: 'Retrieves the identifier of the task running on the core.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1df461a7-2a30-45b7-b7b3-b753b2a22c36'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCore::TaskId property'
---

# ISchedulerCore::TaskId property

Retrieves the identifier of the task running on the core.

This property is read-only.

## Syntax


```C++
HRESULT get_TaskId(
  [out] ITaskId **pTaskId
);
```



## Property value

An [**ITaskId**](itaskid.md) interface that contains the identifiers that uniquely identify the task running on the core. The identifiers are zero if there is no task running on the core.

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

 

 




