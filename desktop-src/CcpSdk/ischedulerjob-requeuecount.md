---
Description: 'Retrieves the number of times that the job has been queued again.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9370d17c-45f0-4e1b-98e0-0a1d9ee81174'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::RequeueCount property'
---

# ISchedulerJob::RequeueCount property

Retrieves the number of times that the job has been queued again.

This property is read-only.

## Syntax


```C++
HRESULT get_RequeueCount(
  [out] long *pCount
);
```



## Property value

The number of times that the job has been queued again.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

The count is incremented each time you call the [**IScheduler::ConfigureJob**](ischeduler-configurejob.md) method.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




