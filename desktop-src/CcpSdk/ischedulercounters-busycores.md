---
Description: 'Retrieves the number of cores that are busy running tasks.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '6036c077-3e7c-45ab-b0bb-bbb885b4975f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::BusyCores property'
---

# ISchedulerCounters::BusyCores property

Retrieves the number of cores that are busy running tasks.

This property is read-only.

## Syntax


```C++
HRESULT get_BusyCores(
  [out] long *pBusyCores
);
```



## Property value

The number of cores that are busy running tasks.

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

 

 




