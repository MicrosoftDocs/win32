---
Description: 'Determines whether the task can run again after a failure.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '770e0505-a7b4-4836-9365-759356fa10f9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::IsRerunnable property'
---

# ISchedulerTask::IsRerunnable property

Determines whether the task can run again after a failure.

This property is read/write.

## Syntax


```C++
HRESULT put_IsRerunnable(
  [in]  VARIANT_BOOL rerun
);

HRESULT get_IsRerunnable(
  [out] VARIANT_BOOL *pRerun
);
```



## Property value

Set to VARIANT\_TRUE if the task can run again after a failure; otherwise, VARIANT\_FALSE. The default is VARIANT\_TRUE.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulerjob-errormessage.md) task property.

## Remarks

If this value is VARIANT\_FALSE, you cannot call the [**ISchedulerJob::RequeueTask**](ischedulerjob-requeuetask.md) method to run the task again.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




