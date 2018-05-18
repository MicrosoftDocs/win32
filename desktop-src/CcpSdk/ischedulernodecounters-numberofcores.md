---
Description: 'Retrieves the number of cores on the node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd3a4e91e-d90c-49fb-a440-4ff87ce10bac'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerNodeCounters::NumberOfCores property'
---

# ISchedulerNodeCounters::NumberOfCores property

Retrieves the number of cores on the node.

This property is read-only.

## Syntax


```C++
HRESULT get_NumberOfCores(
  [out] long *pNumberOfCores
);
```



## Property value

The number of cores on the node.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerNodeCounters**](ischedulernodecounters.md)
</dt> </dl>

 

 




