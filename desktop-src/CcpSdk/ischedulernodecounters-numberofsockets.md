---
Description: 'Retrieves the number of sockets on the node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5ffd2c79-5551-4b29-b4a1-cd4ffc2518c6'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerNodeCounters::NumberOfSockets property'
---

# ISchedulerNodeCounters::NumberOfSockets property

Retrieves the number of sockets on the node.

This property is read-only.

## Syntax


```C++
HRESULT get_NumberOfSockets(
  [out] long *pNumberOfSockets
);
```



## Property value

The number of sockets on the node.

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

 

 




