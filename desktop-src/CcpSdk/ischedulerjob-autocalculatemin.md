---
Description: 'Determines whether the scheduler automatically calculates the minimum resource value.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b77d5741-ad18-400f-b8e5-97bc3b9cf8ae'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::AutoCalculateMin property'
---

# ISchedulerJob::AutoCalculateMin property

Determines whether the scheduler automatically calculates the minimum resource value.

This property is read/write.

## Syntax


```C++
HRESULT put_AutoCalculateMin(
  [in]  VARIANT_BOOL autoCalcMax
);

HRESULT get_AutoCalculateMin(
  [out] VARIANT_BOOL *pAutoCalcMax
);
```



## Property value

Set to VARIANT\_TRUE if you want the scheduler to calculate the minimum value; otherwise, VARIANT\_FALSE if you are going to specify the value.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

The value of the [**ISchedulerJob::UnitType**](ischedulerjob-unittype.md) property determines which minimum resource value the scheduler calculates (for example, [**ISchedulerJob::MinimumNumberOfNodes**](ischedulerjob-minimumnumberofnodes.md) or [**ISchedulerJob::MinimumNumberOfCores**](ischedulerjob-minimumnumberofcores.md)).

If you set one of the minimum resource properties, you must set **AutoCalculateMin** to VARIANT\_FALSE; otherwise, the minimum resource value that you specified will be ignored.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob.AutoCalculateMax**](ischedulerjob-autocalculatemax.md)
</dt> <dt>

[**ISchedulerJob.CanShrink**](ischedulerjob-canshrink.md)
</dt> <dt>

[**ISchedulerJob.MinimumNumberOfNodes**](ischedulerjob-minimumnumberofnodes.md)
</dt> <dt>

[**ISchedulerJob.MinimumNumberOfCores**](ischedulerjob-minimumnumberofcores.md)
</dt> <dt>

[**ISchedulerJob.MinimumNumberOfSockets**](ischedulerjob-minimumnumberofsockets.md)
</dt> <dt>

[**JobUnitType**](jobunittype.md)
</dt> </dl>

 

 




