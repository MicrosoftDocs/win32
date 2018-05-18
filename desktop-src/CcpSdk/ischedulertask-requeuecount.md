---
Description: 'Retrieves the number of times that the task has been queued again.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9fa86a9f-2651-4c26-8613-236a2f513157'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::RequeueCount property'
---

# ISchedulerTask::RequeueCount property

Retrieves the number of times that the task has been queued again.

This property is read-only.

## Syntax


```C++
HRESULT get_RequeueCount(
  [out] long *pCount
);
```



## Property value

The number of times that the task has been queued again.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Remarks

The count increments each time you call the [**ISchedulerJob::RequeueTask**](ischedulerjob-requeuetask.md) method.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




