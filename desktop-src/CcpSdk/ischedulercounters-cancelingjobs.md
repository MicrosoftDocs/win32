---
Description: 'Retrieves the number of jobs that are in the process of being canceled.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd29d7ae5-3542-4f08-b7fb-96c4c15f0083'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::CancelingJobs property'
---

# ISchedulerCounters::CancelingJobs property

Retrieves the number of jobs that are in the process of being canceled.

This property is read-only.

## Syntax


```C++
HRESULT get_CancelingJobs(
  [out] long *pCancelingJobs
);
```



## Property value

The number of jobs that are in the process of being canceled.

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

 

 




