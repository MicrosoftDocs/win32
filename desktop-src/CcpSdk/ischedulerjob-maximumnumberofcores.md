---
Description: 'Retrieves or sets the maximum number of cores that the scheduler may allocate for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '964bd97a-b62b-4b3b-800c-bfd9a562d01f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::MaximumNumberOfCores property'
---

# ISchedulerJob::MaximumNumberOfCores property

Retrieves or sets the maximum number of cores that the scheduler may allocate for the job.

This property is read/write.

## Syntax


```C++
HRESULT put_MaximumNumberOfCores(
  [in]  long maxCores
);

HRESULT get_MaximumNumberOfCores(
  [out] long *pMaxCores
);
```



## Property value

The maximum number of cores.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

Set this property if the [**ISchedulerJob::UnitType**](ischedulerjob-unittype.md) property is JobUnitType\_Core.

If you set this property, you must set the [**ISchedulerJob::AutoCalculateMax**](ischedulerjob-autocalculatemax.md) property to VARIANT\_FALSE; otherwise, the maximum number of cores that you specified will be ignored.

The Default job template sets the default value to 1.

This property tells the scheduler that the job requires at most *n* cores to run (the scheduler will not allocate more than this number of cores for the job).

The job can run when its minimum resource requirements are met. The scheduler may allocate up to the maximum specified resource limit for the job. The scheduler will allocate more resources to the job or release resources if the [**ISchedulerJob::CanGrow**](ischedulerjob-cangrow.md) or [**ISchedulerJob::CanShrink**](ischedulerjob-canshrink.md) properties are set to VARIANT\_TRUE; otherwise, the job uses the initial allocation for its lifetime.

The property value cannot:

-   Exceed the number of cores in the cluster or the number of cores on the nodes that you requested (with the [**ISchedulerJob::RequestedNodes**](ischedulerjob-requestednodes.md) property).
-   Be less than the value of the [**ISchedulerJob::MinimumNumberOfCores**](ischedulerjob-minimumnumberofcores.md) property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob.MaxCoresPerNode**](ischedulerjob-maxcorespernode.md)
</dt> <dt>

[**ISchedulerJob.MaximumNumberOfNodes**](ischedulerjob-maximumnumberofnodes.md)
</dt> <dt>

[**ISchedulerJob.MaximumNumberOfSockets**](ischedulerjob-maximumnumberofsockets.md)
</dt> <dt>

[**ISchedulerJob.MinimumNumberOfCores**](ischedulerjob-minimumnumberofcores.md)
</dt> </dl>

 

 




