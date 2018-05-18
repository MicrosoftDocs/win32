---
Description: 'Determines whether the scheduler automatically calculates the maximum resource value.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f636ddb4-126a-4225-9375-fc34ccd7b1c7'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::AutoCalculateMax property'
---

# ISchedulerJob::AutoCalculateMax property

Determines whether the scheduler automatically calculates the maximum resource value.

This property is read/write.

## Syntax


```C++
HRESULT put_AutoCalculateMax(
  [in]  VARIANT_BOOL autoCalcMax
);

HRESULT get_AutoCalculateMax(
  [out] VARIANT_BOOL *pAutoCalcMax
);
```



## Property value

Set to VARIANT\_TRUE if you want the scheduler to calculate the maximum value; otherwise, VARIANT\_FALSE if you are going to specify the value.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

The value of the [**ISchedulerJob::UnitType**](ischedulerjob-unittype.md) property determines which maximum resource value the scheduler calculates (for example, [**ISchedulerJob::MaximumNumberOfNodes**](ischedulerjob-maximumnumberofnodes.md) or [**ISchedulerJob::MaximumNumberOfCores**](ischedulerjob-maximumnumberofcores.md)).

If you set one of the maximum resource properties, you must set **AutoCalculateMax** to VARIANT\_FALSE; otherwise, the maximum resource value that you specified will be ignored.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob.AutoCalculateMin**](ischedulerjob-autocalculatemin.md)
</dt> <dt>

[**ISchedulerJob.CanGrow**](ischedulerjob-cangrow.md)
</dt> <dt>

[**ISchedulerJob.MaximumNumberOfNodes**](ischedulerjob-maximumnumberofnodes.md)
</dt> <dt>

[**ISchedulerJob.MaximumNumberOfCores**](ischedulerjob-maximumnumberofcores.md)
</dt> <dt>

[**ISchedulerJob.MaximumNumberOfSockets**](ischedulerjob-maximumnumberofsockets.md)
</dt> <dt>

[**JobUnitType**](jobunittype.md)
</dt> </dl>

 

 




