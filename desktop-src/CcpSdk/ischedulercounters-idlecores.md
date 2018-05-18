---
Description: 'Retrieves the number of cores that are not allocated to a job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7aed632d-a914-4462-9c3e-1462362f48a0'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::IdleCores property'
---

# ISchedulerCounters::IdleCores property

Retrieves the number of cores that are not allocated to a job.

This property is read-only.

## Syntax


```C++
HRESULT get_IdleCores(
  [out] long *pIdleCores
);
```



## Property value

The number of cores that are not allocated to a job.

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

 

 




