---
Description: 'Determines whether the job resources can grow.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8748c900-8d93-493d-979a-596e4f9f80ec'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::CanGrow property'
---

# ISchedulerJob::CanGrow property

Determines whether the job resources can grow.

This property is read-only.

## Syntax


```C++
HRESULT get_CanGrow(
  [out] VARIANT_BOOL *pCanGrow
);
```



## Property value

If VARIANT\_TRUE, the job resources can grow as more resources become available; otherwise, VARIANT\_FALSE. The default value is VARIANT\_TRUE.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

The server will allocate more resources to job if it determines that the job will benefit from the increase, and if there are more resources available; the server will not grow the resources beyond the maximum requested.

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

[**ISchedulerJob.MaximumNumberOfNodes**](ischedulerjob-maximumnumberofnodes.md)
</dt> <dt>

[**ISchedulerJob.MaximumNumberOfCores**](ischedulerjob-maximumnumberofcores.md)
</dt> <dt>

[**ISchedulerJob.MaximumNumberOfSockets**](ischedulerjob-maximumnumberofsockets.md)
</dt> </dl>

 

 




