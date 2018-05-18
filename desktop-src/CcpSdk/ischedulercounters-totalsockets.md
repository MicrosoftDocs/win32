---
Description: 'Retrieves the total number of sockets in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5c0d249c-f4ec-4849-8ae8-c4f99144b206'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::TotalSockets property'
---

# ISchedulerCounters::TotalSockets property

Retrieves the total number of sockets in the cluster.

This property is read-only.

## Syntax


```C++
HRESULT get_TotalSockets(
  [out] long *pTotalSockets
);
```



## Property value

The total number of sockets in the cluster.

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

 

 




