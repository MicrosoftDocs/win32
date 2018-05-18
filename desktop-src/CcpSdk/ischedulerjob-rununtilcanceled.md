---
Description: 'Determines whether the server reserves resources for the job until the job is canceled (even if the job has no active tasks).'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '147166a1-5d27-452b-a277-b2d5e702cfc6'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::RunUntilCanceled property'
---

# ISchedulerJob::RunUntilCanceled property

Determines whether the server reserves resources for the job until the job is canceled (even if the job has no active tasks).

This property is read/write.

## Syntax


```C++
HRESULT put_RunUntilCanceled(
  [in]  VARIANT_BOOL runUntilCanceled
);

HRESULT get_RunUntilCanceled(
  [out] VARIANT_BOOL *pRunUntilCanceled
);
```



## Property value

Set to VARIANT\_TRUE to reserve resources for the job; otherwise, VARIANT\_FALSE.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property

## Remarks

The Default job template sets the default value to VARIANT\_FALSE.

You cannot set this property to VARIANT\_TRUE if [**ISchedulerJob::AutoCalculateMax**](ischedulerjob-autocalculatemax.md) and [**ISchedulerJob::AutoCalculateMin**](ischedulerjob-autocalculatemin.md) are also set to VARIANT\_TRUE.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob.HasRuntime**](ischedulerjob-hasruntime.md)
</dt> <dt>

[**ISchedulerJob.Runtime**](ischedulerjob-runtime.md)
</dt> </dl>

 

 




