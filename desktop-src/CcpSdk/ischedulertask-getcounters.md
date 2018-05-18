---
Description: 'Retrieves the counter data for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '771405ae-4e09-4d14-b096-16a9af562f95'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::GetCounters method'
---

# ISchedulerTask::GetCounters method

Retrieves the counter data for the task.

## Syntax


```C++
HRESULT GetCounters(
  [out] ISchedulerTaskCounters **pCounters
);
```



## Parameters

<dl> <dt>

*pCounters* \[out\]
</dt> <dd>

An [**ISchedulerTaskCounters**](ischedulertaskcounters.md) interface that contains the counter data for the task.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




