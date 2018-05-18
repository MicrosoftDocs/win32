---
Description: 'Retrieves the counter data for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a78fb720-c66d-4809-861d-4ee0f680a58f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::GetCounters method'
---

# ISchedulerJob::GetCounters method

Retrieves the counter data for the job.

## Syntax


```C++
HRESULT GetCounters(
  [out] ISchedulerJobCounters **pCounters
);
```



## Parameters

<dl> <dt>

*pCounters* \[out\]
</dt> <dd>

An [**ISchedulerJobCounters**](ischedulerjobcounters.md) interface that contains the counter data for the job.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




