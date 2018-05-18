---
Description: 'Retrieves the number of jobs that are being configured.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b0810f02-5553-45f8-bf57-02963e40dd81'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::ConfiguringJobs property'
---

# ISchedulerCounters::ConfiguringJobs property

Retrieves the number of jobs that are being configured.

This property is read-only.

## Syntax


```C++
HRESULT get_ConfiguringJobs(
  [out] long *pConfiguringJobs
);
```



## Property value

The number of jobs that are being configured.

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

 

 




