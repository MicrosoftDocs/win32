---
Description: 'Determines whether the job resources can shrink.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3ec4f6a9-940e-40ff-9916-f9e49e0f0909'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::CanShrink property'
---

# ISchedulerJob::CanShrink property

Determines whether the job resources can shrink.

This property is read-only.

## Syntax


```C++
HRESULT get_CanShrink(
  [out] VARIANT_BOOL *pCanShrink
);
```



## Property value

If VARIANT\_TRUE, the server releases extra resources when they are no longer needed by the job; otherwise, VARIANT\_FALSE. The default value is VARIANT\_TRUE.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

The server will remove resources from job if it determines that the job no longer needs the resources; the server will not shrink the resources beyond the minimum requested.

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

[**ISchedulerJob.MinimumNumberOfNodes**](ischedulerjob-minimumnumberofnodes.md)
</dt> <dt>

[**ISchedulerJob.MinimumNumberOfCores**](ischedulerjob-minimumnumberofcores.md)
</dt> <dt>

[**ISchedulerJob.MinimumNumberOfSockets**](ischedulerjob-minimumnumberofsockets.md)
</dt> </dl>

 

 




