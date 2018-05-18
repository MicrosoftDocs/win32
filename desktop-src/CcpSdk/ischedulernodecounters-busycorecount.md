---
Description: 'Retrieves the number of cores on the node that are busy processing jobs.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'caf63e47-ce7c-4033-87de-e194c9391698'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerNodeCounters::BusyCoreCount property'
---

# ISchedulerNodeCounters::BusyCoreCount property

Retrieves the number of cores on the node that are busy processing jobs.

This property is read-only.

## Syntax


```C++
HRESULT get_BusyCoreCount(
  [out] long *pBusyCoreCount
);
```



## Property value

The number of cores on the node that are busy.

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

 

 




