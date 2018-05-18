---
Description: 'Retrieves the number of cores on the node that are idle.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4c8f5c65-e7dc-4768-84e4-d01ff050289e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerNodeCounters::IdleCoreCount property'
---

# ISchedulerNodeCounters::IdleCoreCount property

Retrieves the number of cores on the node that are idle.

This property is read-only.

## Syntax


```C++
HRESULT get_IdleCoreCount(
  [out] long *pIdleCoreCount
);
```



## Property value

The number of cores on the node that are idle.

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

 

 




