---
Description: 'Retrieves the state of the core.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ea5a39bd-2490-4191-b24c-a26289e790ed'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCore::State property'
---

# ISchedulerCore::State property

Retrieves the state of the core.

This property is read-only.

## Syntax


```C++
HRESULT get_State(
  [out] SchedulerStateProcessor *pState
);
```



## Property value

The state of the core. For possible values, see the [**SchedulerCoreState**](schedulercorestate.md) enumeration.

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

 

 




