---
Description: 'Determines whether other tasks from the job can run on the node at the same time as this task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9e0cbf89-77da-4d6a-99dc-06fdba2d0e7f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::IsExclusive property'
---

# ISchedulerTask::IsExclusive property

Determines whether other tasks from the job can run on the node at the same time as this task.

This property is read/write.

## Syntax


```C++
HRESULT put_IsExclusive(
  [in]  VARIANT_BOOL isExclusive
);

HRESULT get_IsExclusive(
  [out] VARIANT_BOOL *pIsExclusive
);
```



## Property value

Set to VARIANT\_TRUE if other tasks from the same job cannot run on the node; otherwise, VARIANT\_FALSE. The default is VARIANT\_FALSE.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulerjob-errormessage.md) task property.

## Remarks

If [**ISchedulerJob::IsExclusive**](ischedulerjob-isexclusive.md) is VARIANT\_FALSE, you cannot set this property to VARIANT\_TRUE.

If the task is exclusive, you cannot set [**ISchedulerJob::AutoCalculateMax**](ischedulerjob-autocalculatemax.md) or [**ISchedulerJob::AutoCalculateMin**](ischedulerjob-autocalculatemin.md) to VARIANT\_TRUE.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerJob.IsExclusive**](ischedulerjob-isexclusive.md)
</dt> </dl>

 

 




