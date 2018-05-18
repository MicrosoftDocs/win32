---
Description: 'Retrieves the number of cores that are offline.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'efa46242-64a7-4e24-a682-8e2c4640ecac'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::OfflineCores property'
---

# ISchedulerCounters::OfflineCores property

Retrieves the number of cores that are offline.

This property is read-only.

## Syntax


```C++
HRESULT get_OfflineCores(
  [out] long *pOfflineCores
);
```



## Property value

The number of cores that are offline.

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

 

 




