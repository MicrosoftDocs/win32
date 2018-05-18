---
Description: 'Retrieves the number of nodes that are ready to run jobs.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3728b126-ed65-4fe4-99c7-ba988d1c9bf3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::ReadyNodes property'
---

# ISchedulerCounters::ReadyNodes property

Retrieves the number of nodes that are ready to run jobs.

This property is read-only.

## Syntax


```C++
HRESULT get_ReadyNodes(
  [out] long *pReadyNodes
);
```



## Property value

The number of nodes that are ready to run jobs.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerCounters**](ischedulercounters.md)
</dt> </dl>

 

 




