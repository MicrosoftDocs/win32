---
Description: 'Retrieves the number of jobs being validated.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ab7cd694-6511-4443-a44c-facb4853b98a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::ValidatingJobs property'
---

# ISchedulerCounters::ValidatingJobs property

Retrieves the number of jobs being validated.

This property is read-only.

## Syntax


```C++
HRESULT get_ValidatingJobs(
  [out] long *pValidatingJobs
);
```



## Property value

The number of jobs being validated.

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

 

 




