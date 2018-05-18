---
Description: 'Retrieves the number of cores on the node that are offline.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '6f5a40de-93df-4cb9-99ff-5f6c7d703841'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerNodeCounters::OfflineCoreCount property'
---

# ISchedulerNodeCounters::OfflineCoreCount property

Retrieves the number of cores on the node that are offline.

This property is read-only.

## Syntax


```C++
HRESULT get_OfflineCoreCount(
  [out] long *pOfflineCoreCount
);
```



## Property value

The number of cores on the node that are offline.

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

 

 




