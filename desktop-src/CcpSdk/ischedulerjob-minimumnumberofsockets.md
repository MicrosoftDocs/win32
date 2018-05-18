---
Description: 'Retrieves or sets the minimum number of sockets that the job requires to run.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '228a4573-5038-447c-95e5-a8bc07667311'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::MinimumNumberOfSockets property'
---

# ISchedulerJob::MinimumNumberOfSockets property

Retrieves or sets the minimum number of sockets that the job requires to run.

This property is read/write.

## Syntax


```C++
HRESULT put_MinimumNumberOfSockets(
  [in]  long minSockets
);

HRESULT get_MinimumNumberOfSockets(
  [out] long *pMinSockets
);
```



## Property value

The minimum number of sockets.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

Set this property if the [**ISchedulerJob::UnitType**](ischedulerjob-unittype.md) job property is JobUnitType\_Socket.

If you set this property, you must set the [**ISchedulerJob::AutoCalculateMin**](ischedulerjob-autocalculatemin.md) property to VARIANT\_FALSE; otherwise, the minimum number of sockets that you specified will be ignored.

The Default job template sets the default value to 1.

This property tells the scheduler that the job requires at least *n* sockets to run (the scheduler will not allocate less than this number of sockets for the job).

The job can run when its minimum resource requirements are met. The scheduler may allocate up to the maximum specified resource limit for the job. The scheduler will allocate more resources to the job or release resources if the [**ISchedulerJob::CanGrow**](ischedulerjob-cangrow.md) or [**ISchedulerJob::CanShrink**](ischedulerjob-canshrink.md) properties are set to VARIANT\_TRUE; otherwise, the job uses the initial allocation for its lifetime.

The value cannot exceed the value of the [**ISchedulerJob::MaximumNumberOfSockets**](ischedulerjob-maximumnumberofsockets.md) property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob.MaximumNumberOfSockets**](ischedulerjob-maximumnumberofsockets.md)
</dt> <dt>

[**ISchedulerJob.MinimumNumberOfNodes**](ischedulerjob-minimumnumberofnodes.md)
</dt> <dt>

[**ISchedulerJob.MinimumNumberOfCores**](ischedulerjob-minimumnumberofcores.md)
</dt> </dl>

 

 




