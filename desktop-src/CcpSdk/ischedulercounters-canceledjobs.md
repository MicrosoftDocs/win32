---
Description: 'Retrieves the number jobs that have been canceled.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1e933af0-ee03-4de2-a306-e30828f0df46'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::CanceledJobs property'
---

# ISchedulerCounters::CanceledJobs property

Retrieves the number jobs that have been canceled.

This property is read-only.

## Syntax


```C++
HRESULT get_CanceledJobs(
  [out] long *pCanceledJobs
);
```



## Property value

The number jobs that have been canceled.

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

 

 




