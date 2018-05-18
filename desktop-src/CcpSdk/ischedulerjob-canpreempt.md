---
Description: 'Determines whether another job can preempt this job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b47687a7-dd70-4ad6-953a-3632c54e132a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::CanPreempt property'
---

# ISchedulerJob::CanPreempt property

Determines whether another job can preempt this job.

This property is read/write.

## Syntax


```C++
HRESULT put_CanPreempt(
  [in]  VARIANT_BOOL canPreempt
);

HRESULT get_CanPreempt(
  [out] VARIANT_BOOL *pCanPreempt
);
```



## Property value

Set to VARIANT\_TRUE if another job can preempt this job; otherwise, VARIANT\_FALSE.

The Default job template sets the default value to VARIANT\_FALSE.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

For details on job preemption, see the PreemptionType configuration parameter in [**IScheduler::SetClusterParameter**](ischeduler-setclusterparameter.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob.Priority**](ischedulerjob-priority.md)
</dt> </dl>

 

 




